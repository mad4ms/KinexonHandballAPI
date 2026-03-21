"""Wrapper for Kinexon Statistics Center REST and websocket APIs."""

from __future__ import annotations

from collections.abc import Callable
from importlib import import_module
from typing import Any, Literal
from urllib.parse import urlsplit

import httpx

SubscriptionType = Literal["matches", "stats", "events", "live_events"]
HTTP_OK = 200


class StatisticsCenterAPIError(Exception):
    """Exception raised for Statistics Center request errors."""


class StatisticsCenterAPI:
    """Client wrapper for Statistics Center login, push endpoints, and websocket."""

    def __init__(  # noqa: PLR0913
        self,
        *,
        username: str,
        password: str,
        interfaces_api_url: str = "https://hbl.kinexon.com/statistics-center/interfaces-api",
        outputs_push_url: str = "https://hbl.kinexon.com/statistics-center/outputs-push",
        timeout: float = 10.0,
        verify_ssl: bool = True,
    ) -> None:
        self.username = username
        self.password = password
        self.interfaces_api_url = interfaces_api_url.rstrip("/")
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
        jwt = self._extract_jwt(payload)
        if not jwt:
            raise StatisticsCenterAPIError(
                "Statistics Center login response has no jwt."
            )
        self._jwt = jwt
        return jwt

    @staticmethod
    def _extract_jwt(payload: Any) -> str | None:
        if isinstance(payload, dict):
            value = payload.get("jwt")
            return value if isinstance(value, str) else None

        if isinstance(payload, list) and payload:
            first = payload[0]
            if isinstance(first, dict):
                value = first.get("jwt")
                return value if isinstance(value, str) else None

        return None

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

        ws_scheme = "wss" if parsed.scheme == "https" else "ws"
        return f"{ws_scheme}://{parsed.hostname}:5002"

    def connect_websocket(
        self,
        *,
        jwt: str | None = None,
        on_message: Callable[[Any], None] | None = None,
        on_error: Callable[[Any], None] | None = None,
        on_connect: Callable[[], None] | None = None,
        transports: list[str] | None = None,
    ) -> Any:
        """Create and connect a python-socketio client with Authorization header."""
        try:
            socketio = import_module("socketio")
        except ImportError as exc:
            raise StatisticsCenterAPIError(
                "python-socketio is required for websocket support. "
                "Install with: pip install 'python-socketio[client]'"
            ) from exc

        token = jwt or self.login()
        sio_client = socketio.Client()

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
