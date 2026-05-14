import json as _json
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
        assert api.get_websocket_url() == "ws://hbl.kinexon.com:5002"
    finally:
        api.close()


def test_outputs_rest_url_derived_from_interfaces_url() -> None:
    api = StatisticsCenterAPI(username="u", password="p")
    assert api.outputs_rest_url == (
        "https://hbl.kinexon.com/statistics-center/outputs-rest"
    )
    api.close()


def test_outputs_rest_url_unchanged_when_no_interfaces_suffix() -> None:
    api = StatisticsCenterAPI(
        username="u",
        password="p",
        interfaces_api_url="https://example.com/api",
    )
    assert api.outputs_rest_url == "https://example.com/api"
    api.close()


def _make_rest_api(
    handler: Any,
    jwt: str = "tok",
) -> StatisticsCenterAPI:
    api = StatisticsCenterAPI(username="u", password="p")
    api._http_client.close()
    api._http_client = httpx.Client(transport=httpx.MockTransport(handler))
    api._jwt = jwt
    return api


def test_get_with_retry_returns_on_200() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if "/games" in request.url.path:
            return httpx.Response(200, json=[{"match_id": "1"}])
        return httpx.Response(404)

    api = _make_rest_api(handler)
    resp = api._get_with_retry("/games")
    assert resp.json() == [{"match_id": "1"}]
    api.close()


def test_get_with_retry_refreshes_on_401() -> None:
    call_count = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        if "/auth/login" in request.url.path:
            return httpx.Response(200, json={"jwt": "new-token"})
        call_count["n"] += 1
        if call_count["n"] == 1:
            return httpx.Response(401)
        return httpx.Response(200, json=[])

    api = _make_rest_api(handler)
    resp = api._get_with_retry("/games")
    assert resp.status_code == 200  # noqa: PLR2004
    assert call_count["n"] == 2  # noqa: PLR2004
    api.close()


def test_get_games_returns_list() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if "/games" in request.url.path:
            return httpx.Response(200, json=[{"match_id": "42"}])
        return httpx.Response(404)

    api = _make_rest_api(handler)
    games = api.get_games(season="2025_2026")
    assert games == [{"match_id": "42"}]
    api.close()


def test_get_stats_returns_list() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if "/stats/99" in request.url.path:
            return httpx.Response(200, json=[{"player_id": 1}])
        return httpx.Response(404)

    api = _make_rest_api(handler)
    stats = api.get_stats(99)
    assert stats[0]["player_id"] == 1
    api.close()


def test_get_events_passes_event_type_param() -> None:
    received_params: dict[str, str] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        if "/events/55" in request.url.path:
            received_params.update(dict(request.url.params))
            return httpx.Response(200, json=[{"id": 1}])
        return httpx.Response(404)

    api = _make_rest_api(handler)
    events = api.get_events(55, event_type="shot")
    assert events == [{"id": 1}]
    assert received_params.get("event") == "shot"
    api.close()


def test_connect_websocket_with_match_id_auto_subscribes(monkeypatch: Any) -> None:
    sent: list[str] = []

    class FakeSio:
        def __init__(self, **_: Any) -> None:
            self.handlers: dict[str, Any] = {}

        def on(self, name: str, cb: Any) -> None:
            self.handlers[name] = cb

        def connect(self, url: str, **_: Any) -> None:
            # simulate "Connected" message
            self.handlers["message"]("Connected")

        def send(self, payload: Any) -> None:
            sent.append(payload)

    monkeypatch.setitem(sys.modules, "socketio", SimpleNamespace(Client=FakeSio))
    api = StatisticsCenterAPI(username="u", password="p")
    api._jwt = "tok"
    api.connect_websocket(match_id="62090316")
    api.close()

    parsed = [_json.loads(s) for s in sent]
    types_sent = {m["type"] for m in parsed}
    assert "live_events" in types_sent
    assert "events" in types_sent
    shot_filter = next(m for m in parsed if m["type"] == "events")
    assert shot_filter.get("filter") == {"event": "shot"}
    assert all(m["identifier"] == "62090316" for m in parsed)


def test_connect_websocket_registers_handlers(monkeypatch: Any) -> None:
    state: dict[str, Any] = {}

    class FakeSocketClient:
        def __init__(self, **_: Any) -> None:
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
        assert state["url"] == "ws://hbl.kinexon.com:5002"
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
