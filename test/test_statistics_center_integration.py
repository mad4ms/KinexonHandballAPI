import contextlib
import os
import threading
import time
from typing import Literal, cast

import pytest
from dotenv import load_dotenv

from kinexon_handball_api.statistics_center import StatisticsCenterAPI

load_dotenv()

REQUIRED_ENV_VARS = (
    "KINEXON_STATISTICS_CENTER_USERNAME",
    "KINEXON_STATISTICS_CENTER_PASSWORD",
)

ALLOWED_TYPES = {"matches", "stats", "events", "live_events"}


def _missing_env_vars() -> list[str]:
    return [name for name in REQUIRED_ENV_VARS if not os.getenv(name)]


pytestmark = pytest.mark.skipif(
    _missing_env_vars(),
    reason="Missing Statistics Center integration env vars.",
)


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        pytest.skip(f"Missing env var: {name}")
    return cast(str, value)


def _env_ws_type() -> Literal["matches", "stats", "events", "live_events"]:
    ws_type = os.getenv("KINEXON_STATISTICS_CENTER_WS_TYPE", "matches")
    if ws_type not in ALLOWED_TYPES:
        pytest.skip(
            "Invalid KINEXON_STATISTICS_CENTER_WS_TYPE. "
            "Allowed values: matches, stats, events, live_events."
        )
    return cast(Literal["matches", "stats", "events", "live_events"], ws_type)


def _make_api() -> StatisticsCenterAPI:
    return StatisticsCenterAPI(
        username=_require_env("KINEXON_STATISTICS_CENTER_USERNAME"),
        password=_require_env("KINEXON_STATISTICS_CENTER_PASSWORD"),
        interfaces_api_url=os.getenv(
            "KINEXON_STATISTICS_CENTER_INTERFACES_API_URL",
            "https://hbl.kinexon.com/statistics-center/interfaces-api",
        ),
        outputs_push_url=os.getenv(
            "KINEXON_STATISTICS_CENTER_OUTPUTS_PUSH_URL",
            "https://hbl.kinexon.com/statistics-center/outputs-push",
        ),
        timeout=float(os.getenv("KINEXON_STATISTICS_CENTER_TIMEOUT", "20")),
    )


@pytest.mark.integration
def test_statistics_center_list_endpoints_live() -> None:
    api = _make_api()
    try:
        endpoints = api.list_endpoints()
        assert isinstance(endpoints, list)
    finally:
        api.close()


@pytest.mark.integration
def test_statistics_center_websocket_subscribe_live() -> None:
    api = _make_api()
    socket_client = None
    connected = threading.Event()
    errors: list[object] = []

    def on_connect() -> None:
        connected.set()

    def on_error(error: object) -> None:
        errors.append(error)

    try:
        jwt = api.login()
        assert jwt

        socket_client = api.connect_websocket(
            jwt=jwt,
            on_connect=on_connect,
            on_error=on_error,
            transports=["websocket"],
        )

        assert connected.wait(timeout=10)

        api.subscribe(
            socket_client,
            subscription_type=_env_ws_type(),
            identifier=os.getenv(
                "KINEXON_STATISTICS_CENTER_WS_IDENTIFIER", "2019_2020"
            ),
        )

        time.sleep(1.0)
        assert not errors
    finally:
        if socket_client is not None:
            with contextlib.suppress(Exception):
                socket_client.disconnect()
        api.close()
