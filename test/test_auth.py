import base64

import httpx
import pytest
from kinexon_client import Client

from kinexon_handball_api.api import APIRequestError, KinexonAPI


def _make_api(transport: httpx.BaseTransport) -> KinexonAPI:
    client = Client(
        base_url="https://example.test",
        headers={"api-key": "test-key"},
        raise_on_unexpected_status=True,
    )
    httpx_client = httpx.Client(
        base_url="https://example.test",
        transport=transport,
    )
    client.set_httpx_client(httpx_client)

    api = KinexonAPI(
        base_url="https://example.test",
        username_basic="basic-user",
        password_basic="basic-pass",
        username_main="main-user",
        password_main="main-pass",
        endpoint_session="/session",
        endpoint_main="/login",
        api_key="test-key",
        connect_on_init=False,
    )
    api.client = client
    return api


def _basic_auth_header(username: str, password: str) -> str:
    raw = f"{username}:{password}".encode()
    return "Basic " + base64.b64encode(raw).decode("ascii")


def test_authenticate_success_sets_basic_auth() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if request.url.path == "/session":
            return httpx.Response(302, headers={"Location": "/"})
        if request.url.path == "/login":
            return httpx.Response(200, json={"ok": True})
        return httpx.Response(404)

    api = _make_api(httpx.MockTransport(handler))

    assert api.authenticate() is True
    assert [r.url.path for r in requests] == ["/session", "/login"]

    expected = _basic_auth_header("basic-user", "basic-pass")
    assert requests[0].headers.get("Authorization") == expected


def test_authenticate_raises_on_session_failure() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/session":
            return httpx.Response(401, text="nope")
        return httpx.Response(404)

    api = _make_api(httpx.MockTransport(handler))

    with pytest.raises(APIRequestError):
        api.authenticate()


def test_authenticate_raises_on_main_login_failure() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/session":
            return httpx.Response(302, headers={"Location": "/"})
        if request.url.path == "/login":
            return httpx.Response(403, text="nope")
        return httpx.Response(404)

    api = _make_api(httpx.MockTransport(handler))

    with pytest.raises(APIRequestError):
        api.authenticate()
