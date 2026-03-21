import sys
from types import SimpleNamespace
from typing import Any

import httpx
import pytest

from kinexon_handball_api.statistics_center import (
    StatisticsCenterAPI,
    StatisticsCenterAPIError,
)


def _make_api(transport: httpx.BaseTransport) -> StatisticsCenterAPI:
    api = StatisticsCenterAPI(username="user", password="pass")
    api._http_client.close()
    api._http_client = httpx.Client(transport=transport)
    return api


def test_login_extracts_jwt_from_object() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/auth/login"):
            return httpx.Response(200, json={"jwt": "token-123"})
        return httpx.Response(404)

    api = _make_api(httpx.MockTransport(handler))
    try:
        assert api.login() == "token-123"
        assert api.jwt == "token-123"
    finally:
        api.close()


def test_login_extracts_jwt_from_list() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/auth/login"):
            return httpx.Response(200, json=[{"jwt": "token-from-list"}])
        return httpx.Response(404)

    api = _make_api(httpx.MockTransport(handler))
    try:
        assert api.login() == "token-from-list"
    finally:
        api.close()


def test_list_endpoints_uses_bearer_token() -> None:
    auth_headers: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        auth_headers.append(request.headers.get("Authorization", ""))

        if request.url.path.endswith("/auth/login") and request.method == "POST":
            return httpx.Response(200, json={"jwt": "token-abc"})
        if request.url.path.endswith("/endpoints") and request.method == "GET":
            return httpx.Response(200, json=[{"id": "1", "type": "events"}])
        return httpx.Response(404)

    api = _make_api(httpx.MockTransport(handler))
    try:
        endpoints = api.list_endpoints()
        assert endpoints[0]["id"] == "1"
        assert "Bearer token-abc" in auth_headers
    finally:
        api.close()


def test_create_and_delete_are_disabled_in_read_only_mode() -> None:
    api = StatisticsCenterAPI(username="user", password="pass")
    try:
        with pytest.raises(StatisticsCenterAPIError, match="create_endpoint"):
            api.create_endpoint({"type": "live_events", "identifier": "*"})

        with pytest.raises(StatisticsCenterAPIError, match="delete_endpoint"):
            api.delete_endpoint("endpoint-id")
    finally:
        api.close()


def test_get_websocket_url_from_https_interface_url() -> None:
    api = StatisticsCenterAPI(
        username="user",
        password="pass",
        interfaces_api_url="https://hbl.kinexon.com/statistics-center/interfaces-api",
    )
    try:
        assert api.get_websocket_url() == "wss://hbl.kinexon.com:5002"
    finally:
        api.close()


def test_connect_websocket_registers_handlers(monkeypatch: Any) -> None:
    state: dict[str, Any] = {}

    class FakeSocketClient:
        def __init__(self) -> None:
            self.handlers: dict[str, Any] = {}

        def on(self, name: str, callback: Any) -> None:
            self.handlers[name] = callback

        def connect(
            self, url: str, headers: dict[str, str], transports: list[str]
        ) -> None:
            state["url"] = url
            state["headers"] = headers
            state["transports"] = transports

        def send(self, payload: dict[str, Any]) -> None:
            state["payload"] = payload

    monkeypatch.setitem(
        sys.modules, "socketio", SimpleNamespace(Client=FakeSocketClient)
    )

    api = StatisticsCenterAPI(username="user", password="pass")
    try:

        def msg_handler(data: Any) -> Any:
            return data

        def err_handler(error: Any) -> Any:
            return error

        def conn_handler() -> None:
            return None

        socket_client = api.connect_websocket(
            on_message=msg_handler,
            on_error=err_handler,
            on_connect=conn_handler,
            jwt="jwt-xyz",
        )

        assert state["headers"]["Authorization"] == "Bearer jwt-xyz"
        assert state["url"] == "wss://hbl.kinexon.com:5002"
        assert socket_client.handlers["message"] is msg_handler
        assert socket_client.handlers["error"] is err_handler
        assert socket_client.handlers["connect"] is conn_handler

        api.subscribe(
            socket_client,
            subscription_type="live_events",
            identifier="match-1",
        )
        assert state["payload"]["type"] == "live_events"
        assert state["payload"]["identifier"] == "match-1"
    finally:
        api.close()
