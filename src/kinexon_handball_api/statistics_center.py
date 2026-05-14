"""Wrapper for Kinexon Statistics Center REST and websocket APIs."""

from __future__ import annotations

import contextlib
import json
import os
import re
import threading
import time
from collections.abc import Callable
from importlib import import_module
from typing import Any, Literal
from urllib.parse import urlsplit

import httpx
from statistics_center_client.models import Games, LoginSuccess

SubscriptionType = Literal["matches", "stats", "events", "live_events"]
HTTP_OK = 200
HTTP_UNAUTHORIZED = 401
_DEFAULT_INTERFACES_URL = "https://hbl.kinexon.com/statistics-center/interfaces-api"
_DEFAULT_OUTPUTS_PUSH_URL = "https://hbl.kinexon.com/statistics-center/outputs-push"


class StatisticsCenterAPIError(Exception):
    """Exception raised for Statistics Center request errors."""


class StatisticsCenterAPI:
    """Client wrapper for Statistics Center login, REST data, push endpoints, and WS."""

    def __init__(  # noqa: PLR0913
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        interfaces_api_url: str | None = None,
        outputs_push_url: str = _DEFAULT_OUTPUTS_PUSH_URL,
        timeout: float = 15.0,
        verify_ssl: bool = True,
    ) -> None:
        self.username = username or os.environ["KINEXON_STATISTICS_CENTER_USERNAME"]
        self.password = password or os.environ["KINEXON_STATISTICS_CENTER_PASSWORD"]
        self.interfaces_api_url = (
            interfaces_api_url
            or os.getenv("KINEXON_STATISTICS_CENTER_URL")
            or _DEFAULT_INTERFACES_URL
        ).rstrip("/")
        self.outputs_push_url = outputs_push_url.rstrip("/")
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self._jwt: str | None = None
        self._http_client = httpx.Client(
            timeout=httpx.Timeout(timeout),
            verify=verify_ssl,
        )

    def close(self) -> None:
        self._http_client.close()

    def __enter__(self) -> StatisticsCenterAPI:
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()

    @property
    def jwt(self) -> str | None:
        return self._jwt

    @property
    def outputs_rest_url(self) -> str:
        """Base URL for outputs-rest data endpoints."""
        return re.sub(r"/interfaces-api$", "/outputs-rest", self.interfaces_api_url)

    def login(self, *, force_refresh: bool = False) -> str:
        """Authenticate against /auth/login and return a JWT."""
        if self._jwt and not force_refresh:
            return self._jwt

        url = f"{self.interfaces_api_url}/auth/login"
        response = self._http_client.post(
            url,
            json={"name": self.username, "password": self.password},
            headers={"Content-Type": "application/json"},
        )

        if response.status_code != HTTP_OK:
            raise StatisticsCenterAPIError(
                "Statistics Center login failed: "
                f"{response.status_code} {response.text}"
            )

        payload = response.json()
        raw = payload[0] if isinstance(payload, list) and payload else payload
        if not isinstance(raw, dict):
            raise StatisticsCenterAPIError(
                "Statistics Center login response has no jwt."
            )
        result = LoginSuccess.from_dict(raw)
        jwt = result.jwt if isinstance(result.jwt, str) else None
        if not jwt:
            raise StatisticsCenterAPIError(
                "Statistics Center login response has no jwt."
            )
        self._jwt = jwt
        return jwt

    def _get_with_retry(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
    ) -> httpx.Response:
        """GET from outputs-rest, refreshing the JWT once on 401."""
        url = f"{self.outputs_rest_url}{path}"
        token = self._jwt or self.login()
        response = self._http_client.get(
            url,
            headers={"Authorization": f"Bearer {token}"},
            params=params,
        )
        if response.status_code == HTTP_UNAUTHORIZED:
            token = self.login(force_refresh=True)
            response = self._http_client.get(
                url,
                headers={"Authorization": f"Bearer {token}"},
                params=params,
            )
        if response.status_code != HTTP_OK:
            raise StatisticsCenterAPIError(
                f"Statistics Center GET {path} failed: "
                f"{response.status_code} {response.text}"
            )
        return response

    def get_games(self, season: str = "") -> list[Games]:
        """Return all matches for the given season from /games."""
        params = {"season": season} if season else None
        payload = self._get_with_retry("/games", params=params).json()
        if not isinstance(payload, list):
            raise StatisticsCenterAPIError("Expected list from /games")
        return [Games.from_dict(g) for g in payload if isinstance(g, dict)]

    def get_stats(self, match_id: str | int) -> list[dict[str, Any]]:
        """Return player statistics for a match from /stats/{match_id}."""
        payload = self._get_with_retry(f"/stats/{match_id}").json()
        if not isinstance(payload, list):
            raise StatisticsCenterAPIError(f"Expected list from /stats/{match_id}")
        return payload

    def get_events(
        self,
        match_id: str | int,
        event_type: str = "",
    ) -> list[dict[str, Any]]:
        """Return events for a match from /events/{match_id}.

        Pass event_type (e.g. "shot") to filter by event type.
        """
        params = {"event": event_type} if event_type else None
        payload = self._get_with_retry(f"/events/{match_id}", params=params).json()
        if not isinstance(payload, list):
            raise StatisticsCenterAPIError(f"Expected list from /events/{match_id}")
        return payload

    def get_games_via_websocket(
        self,
        season: str,
        timeout_s: float = 10.0,
        verbose: bool = False,
    ) -> list[Games]:
        """Discover matches for a season via the WebSocket matches stream.

        Connects, sends a matches subscription, waits up to timeout_s for the
        response, then disconnects. Returns the list of game dicts (empty on
        timeout or error).
        """
        try:
            socketio = import_module("socketio")
        except ImportError as exc:
            raise StatisticsCenterAPIError(
                "python-socketio is required for websocket support."
            ) from exc

        done = threading.Event()
        games: list[Games] = []
        token = self._jwt or self.login()
        sio = socketio.Client(
            reconnection=False,
            logger=verbose,
            engineio_logger=verbose,
        )

        @sio.on("message")
        def _on_message(data: Any) -> None:
            nonlocal games
            if isinstance(data, str):
                if data == "Connected":
                    sio.send(
                        json.dumps(
                            {
                                "subscription": 1,
                                "type": "matches",
                                "identifier": season,
                            }
                        )
                    )
                    return
                try:
                    data = json.loads(data)
                except Exception:
                    return
            if isinstance(data, dict) and data.get("type") == "matches":
                payload = data.get("payload")
                if isinstance(payload, list):
                    games = [Games.from_dict(r) for r in payload if isinstance(r, dict)]
                done.set()

        @sio.on("connect_error")
        def _on_error(error: Any) -> None:
            done.set()

        try:
            sio.connect(
                self.get_websocket_url(),
                transports=["polling", "websocket"],
                headers={"Authorization": f"Bearer {token}"},
            )
            end = time.time() + timeout_s
            while not done.is_set() and time.time() < end:
                time.sleep(0.1)
        finally:
            with contextlib.suppress(Exception):
                sio.disconnect()

        return games

    def list_endpoints(self, *, jwt: str | None = None) -> list[dict[str, Any]]:
        token = jwt or self.login()
        response = self._http_client.get(
            f"{self.outputs_push_url}/endpoints",
            headers=self._auth_headers(token),
        )
        self._raise_on_bad_status(response, "list endpoints")

        payload = response.json()
        if isinstance(payload, list):
            return payload
        raise StatisticsCenterAPIError("Unexpected response format for endpoints list.")

    def create_endpoint(
        self,
        endpoint: dict[str, Any],
        *,
        jwt: str | None = None,
    ) -> dict[str, Any]:
        del endpoint, jwt
        raise StatisticsCenterAPIError("create_endpoint is disabled in read-only mode.")

    def delete_endpoint(self, endpoint_id: str, *, jwt: str | None = None) -> bool:
        del endpoint_id, jwt
        raise StatisticsCenterAPIError("delete_endpoint is disabled in read-only mode.")

    @staticmethod
    def _auth_headers(jwt: str) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {jwt}",
            "Content-Type": "application/json",
        }

    @staticmethod
    def _raise_on_bad_status(response: httpx.Response, action: str) -> None:
        if response.status_code != HTTP_OK:
            raise StatisticsCenterAPIError(
                f"Statistics Center {action} failed: "
                f"{response.status_code} {response.text}"
            )

    def get_websocket_url(self) -> str:
        """Build websocket URL from the interfaces API host."""
        parsed = urlsplit(self.interfaces_api_url)
        if not parsed.hostname:
            raise StatisticsCenterAPIError(
                "Cannot derive websocket host from interfaces_api_url."
            )
        return f"ws://{parsed.hostname}:5002"

    def connect_websocket(  # noqa: PLR0913
        self,
        *,
        match_id: str | int | None = None,
        subscribe_types: list[str] | None = None,
        jwt: str | None = None,
        on_message: Callable[[Any], None] | None = None,
        on_error: Callable[[Any], None] | None = None,
        on_connect: Callable[[], None] | None = None,
        transports: list[str] | None = None,
        verbose: bool = False,
    ) -> Any:
        """Create and connect a python-socketio client.

        When match_id is provided, automatically subscribes to each type in
        subscribe_types (default: ["live_events", "events"]) on connect.
        The "events" subscription includes filter: {"event": "shot"}.
        """
        try:
            socketio = import_module("socketio")
        except ImportError as exc:
            raise StatisticsCenterAPIError(
                "python-socketio is required for websocket support. "
                "Install with: pip install 'python-socketio[client]'"
            ) from exc

        token = jwt or self.login()
        sio_client = socketio.Client(logger=verbose, engineio_logger=verbose)

        if match_id is not None:
            _subscribe_types = subscribe_types or ["live_events", "events"]
            _match_str = str(match_id)

            def _auto_subscribe(data: Any) -> None:
                if data == "Connected":
                    for sub_type in _subscribe_types:
                        msg: dict[str, Any] = {
                            "subscription": 1,
                            "type": sub_type,
                            "identifier": _match_str,
                        }
                        if sub_type == "events":
                            msg["filter"] = {"event": "shot"}
                        sio_client.send(json.dumps(msg))
                if on_message is not None:
                    on_message(data)

            sio_client.on("message", _auto_subscribe)
        else:
            if on_connect is not None:
                sio_client.on("connect", on_connect)
            if on_message is not None:
                sio_client.on("message", on_message)

        if on_error is not None:
            sio_client.on("error", on_error)

        sio_client.connect(
            self.get_websocket_url(),
            headers={"Authorization": f"Bearer {token}"},
            transports=transports or ["polling", "websocket"],
        )
        return sio_client

    @staticmethod
    def subscribe(
        websocket_client: Any,
        *,
        subscription_type: SubscriptionType,
        identifier: str,
        subscription: int = 1,
        filter: dict[str, Any] | None = None,
    ) -> None:
        payload: dict[str, Any] = {
            "subscription": subscription,
            "type": subscription_type,
            "identifier": identifier,
        }
        if filter:
            payload["filter"] = filter

        websocket_client.send(payload)
