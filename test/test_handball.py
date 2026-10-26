from collections.abc import Callable
from pathlib import Path

import httpx
import pytest
from kinexon_client import Client

from kinexon_handball_api.handball import HandballAPI

CSV = b"ts in ms;game time in s;x in m\n1;0;0.5\n2;1;0.6\n"

Handler = Callable[[httpx.Request], httpx.Response]


def _make_api(handler: Handler) -> HandballAPI:
    client = Client(base_url="https://example.test", raise_on_unexpected_status=True)
    client.set_httpx_client(
        httpx.Client(
            base_url="https://example.test", transport=httpx.MockTransport(handler)
        )
    )
    api = HandballAPI(
        base_url="https://example.test",
        username_basic="u",
        password_basic="p",
        username_main="u",
        password_main="p",
        endpoint_session="/session",
        endpoint_main="/login",
        api_key="k",
        connect_on_init=False,
    )
    api.client = client
    return api


def _recording(
    body: bytes | object, seen: list[httpx.Request], status: int = 200
) -> Handler:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        if isinstance(body, bytes):
            return httpx.Response(status, content=body)
        return httpx.Response(status, json=body)

    return handler


def test_inertial_export_url_params_and_sample() -> None:
    seen: list[httpx.Request] = []
    api = _make_api(_recording(CSV, seen))
    data = api.download_inertial_csv_via_custom(
        "3478", use_local_frame_imu=True, max_bytes=10, show_progress=False
    )
    assert data == CSV[:10]
    request = seen[0]
    assert request.url.path == "/public/v1/export/inertial/session/3478"
    assert request.url.params["useLocalFrameIMU"] == "true"
    assert "centerOrigin" not in request.url.params


def test_positions_export_keeps_its_params() -> None:
    seen: list[httpx.Request] = []
    api = _make_api(_recording(CSV, seen))
    assert api.download_positions_csv_via_custom("7", show_progress=False) == CSV
    assert seen[0].url.path == "/public/v1/export/positions/session/7"
    assert seen[0].url.params["groupByTimestamp"] == "false"


def test_export_to_file_is_atomic(tmp_path: Path) -> None:
    api = _make_api(_recording(CSV, []))
    target = tmp_path / "inertial.csv"
    assert api.download_export_to_file("inertial", "3478", target) == len(CSV)
    assert target.read_bytes() == CSV
    assert not list(tmp_path.glob("*.part"))


def test_failed_export_leaves_no_file(tmp_path: Path) -> None:
    api = _make_api(_recording(b"broken", [], status=500))
    target = tmp_path / "positions.csv"
    with pytest.raises(RuntimeError, match="HTTP 500"):
        api.download_export_to_file("positions", "3478", target)
    assert not list(tmp_path.iterdir())


def test_json_endpoints_build_the_documented_urls() -> None:
    seen: list[httpx.Request] = []
    api = _make_api(_recording([{"id": 1}], seen))
    api.get_events("change_of_orientation", "3478")
    api.get_events("sprint", "5864", time_entity_type="phase", players="in-team-13")
    api.get_event_counts("3478")
    api.get_sensor_assignment("3478")
    api.get_player_statistics(
        2589, "5864", time_entity_type="phase", fields=["speed_max"]
    )
    api.get_session_categories("3478")
    assert [r.url.path for r in seen] == [
        "/public/v1/events/change_of_orientation/player/in-entity/session/3478",
        "/public/v1/events/sprint/player/in-team-13/phase/5864",
        "/public/v1/events/count-per-event-type/player/in-entity/session/3478",
        "/public/v1/sensor-assignment/3478",
        "/public/v1/statistics/player/2589/phase/5864",
        "/public/v1/statistics/3478/categories",
    ]
    assert seen[4].url.params["fields"] == "speed_max"


def test_json_error_carries_the_body() -> None:
    message = {"message": "Type of x is invalid"}
    api = _make_api(_recording(message, [], status=400))
    with pytest.raises(RuntimeError, match=r"HTTP 400.*invalid"):
        api.get_events("x", "3478")
