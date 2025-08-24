import pytest
import requests
import requests_mock

from kinexon_handball_api.client import KinexonClient
from kinexon_handball_api.config import Settings
from kinexon_handball_api.exceptions import KinexonAPIError

import pytest
from kinexon_handball_api.config import Settings


@pytest.fixture
def settings(monkeypatch):
    # Session credentials
    monkeypatch.setenv("USERNAME_KINEXON_SESSION", "user_sess")
    monkeypatch.setenv("PASSWORD_KINEXON_SESSION", "pass_sess")
    monkeypatch.setenv("ENDPOINT_KINEXON_SESSION", "https://api.test/session")

    # Main login credentials
    monkeypatch.setenv("USERNAME_KINEXON_MAIN", "user_main")
    monkeypatch.setenv("PASSWORD_KINEXON_MAIN", "pass_main")
    monkeypatch.setenv("ENDPOINT_KINEXON_MAIN", "https://api.test/login")

    # API endpoint + key
    monkeypatch.setenv("ENDPOINT_KINEXON_API", "https://api.test/api")
    monkeypatch.setenv("API_KEY_KINEXON", "test_api_key")

    # SSL toggle
    monkeypatch.setenv("VERIFY_SSL_KINEXON", "false")

    return Settings()


@pytest.fixture
def client(settings):
    with requests_mock.Mocker() as m:
        # Mock session login
        m.get("https://api.test/session", status_code=200, json={"ok": True})
        # Mock main login
        m.post(
            "https://api.test/login", status_code=200, json={"token": "abc"}
        )
        yield KinexonClient(settings)


def test_authentication_failure_session(requests_mock, settings):
    # Settings enthält jetzt alle Dummy-Umgebungsvariablen
    from kinexon_handball_api.client import KinexonClient, KinexonAPIError

    # Mock Session endpoint mit 401
    requests_mock.get(
        "https://api.test/session", status_code=401, text="Unauthorized"
    )

    with pytest.raises(KinexonAPIError):
        KinexonClient(settings)


def test_authentication_failure_main(settings):
    with requests_mock.Mocker() as m:
        m.get("https://api.test/session", status_code=200)
        m.post("https://api.test/login", status_code=403, text="Forbidden")
        with pytest.raises(KinexonAPIError) as excinfo:
            KinexonClient(settings)
        assert "Main login failed" in str(excinfo.value)


def test_request_json_response(client, requests_mock):
    url = "https://api.test/api/test-json"
    requests_mock.get(url, json={"hello": "world"})
    result = client._request("GET", url)
    assert result == {"hello": "world"}


def test_request_text_response(client, requests_mock):
    url = "https://api.test/api/test-text"
    requests_mock.get(
        url, text="plain text", headers={"Content-Type": "text/plain"}
    )
    result = client._request("GET", url)
    assert result == "plain text"


def test_request_bytes_response(client, requests_mock):
    url = "https://api.test/api/test-bytes"
    requests_mock.get(
        url,
        content=b"binarydata",
        headers={"Content-Type": "application/octet-stream"},
    )
    result = client._request("GET", url)
    assert result == b"binarydata"


def test_request_http_error(client, requests_mock):
    url = "https://api.test/api/fail"
    requests_mock.get(url, status_code=500, text="Server Error")
    with pytest.raises(KinexonAPIError) as excinfo:
        client._request("GET", url)
    assert "API request failed" in str(excinfo.value)


def test_get_session_ids(client, requests_mock):
    url = "https://api.test/api/teams/42/sessions-and-phases"
    mock_data = [
        {
            "session_id": "s1",
            "description": "Training",
            "start_session": "2025-08-01",
        }
    ]
    requests_mock.get(url, json=mock_data)
    result = client.get_session_ids(42, "2025-08-01", "2025-08-31")
    assert result == mock_data
    assert result[0]["session_id"] == "s1"


def test_get_available_metrics_and_events(client, requests_mock):
    url = "https://api.test/api/statistics/list"
    mock_data = {"metrics": ["speed"], "events": ["goal"]}
    requests_mock.get(url, json=mock_data)
    result = client.get_available_metrics_and_events()
    assert "metrics" in result
    assert "events" in result


def test_export_positions(client, requests_mock):
    url = "https://api.test/api/export/positions/session/s123"
    requests_mock.get(
        url, content=b"id,x,y\n1,0,0", headers={"Content-Type": "text/csv"}
    )
    result = client.export_positions("s123")
    assert isinstance(result, (bytes, bytearray))
    assert b"id,x,y" in result
