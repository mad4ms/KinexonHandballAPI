import os
from typing import cast

import pytest
from dotenv import load_dotenv
from kinexon_handball_api.api import KinexonAPI

load_dotenv()  # Load .env file for integration test credentials


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        pytest.skip(f"Missing env var: {name}")
    return cast(str, value)


@pytest.mark.integration  # type: ignore[misc]
def test_authenticate_live() -> None:
    api = KinexonAPI(
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

    try:
        api.connect()
        assert api.client is not None
    finally:
        api.close()
