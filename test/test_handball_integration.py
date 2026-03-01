import os
from typing import cast

import httpx
import pytest
from dotenv import load_dotenv

from kinexon_handball_api.handball import HandballAPI

load_dotenv()

REQUIRED_ENV_VARS = (
    "ENDPOINT_KINEXON_API",
    "USERNAME_KINEXON_SESSION",
    "PASSWORD_KINEXON_SESSION",
    "USERNAME_KINEXON_MAIN",
    "PASSWORD_KINEXON_MAIN",
    "ENDPOINT_KINEXON_SESSION",
    "ENDPOINT_KINEXON_MAIN",
    "API_KEY_KINEXON",
)


def _missing_env_vars() -> list[str]:
    return [name for name in REQUIRED_ENV_VARS if not os.getenv(name)]


pytestmark = pytest.mark.skipif(
    _missing_env_vars(),
    reason="Missing integration env vars.",
)


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        pytest.skip(f"Missing env var: {name}")
    return cast(str, value)


def _require_int_env(name: str) -> int:
    return int(_require_env(name))


def _make_api() -> HandballAPI:
    api = HandballAPI(
        base_url=_require_env("ENDPOINT_KINEXON_API"),
        username_basic=_require_env("USERNAME_KINEXON_SESSION"),
        password_basic=_require_env("PASSWORD_KINEXON_SESSION"),
        username_main=_require_env("USERNAME_KINEXON_MAIN"),
        password_main=_require_env("PASSWORD_KINEXON_MAIN"),
        endpoint_session=_require_env("ENDPOINT_KINEXON_SESSION"),
        endpoint_main=_require_env("ENDPOINT_KINEXON_MAIN"),
        api_key=_require_env("API_KEY_KINEXON"),
        connect_on_init=False,
    )
    api.connect()
    return api


@pytest.mark.integration
def test_get_available_metrics_and_events_live() -> None:
    api = _make_api()
    try:
        result = api.get_available_metrics_and_events()
        assert result is not None
    finally:
        api.close()


@pytest.mark.integration
def test_get_team_players_live() -> None:
    api = _make_api()
    try:
        team_id = _require_int_env("KINEXON_TEAM_ID")
        result = api.get_team_players(team_id)
        assert result is not None
    finally:
        api.close()


@pytest.mark.integration
def test_download_positions_csv_partial_live() -> None:
    api = _make_api()
    try:
        session_id = _require_env("KINEXON_SESSION_ID")
        try:
            data = api.download_positions_csv_via_custom(
                session_id,
                show_progress=False,
                max_bytes=1024,
                timeout=60.0,
            )
            assert len(data) <= 1024  # noqa: PLR2004
        except httpx.TimeoutException:
            pytest.skip("Download timed out before first bytes arrived.")
    finally:
        api.close()
