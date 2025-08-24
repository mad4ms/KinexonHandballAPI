import pytest
import logging

from kinexon_handball_api.config import Settings
from kinexon_handball_api.client import KinexonClient

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def settings() -> Settings:
    """Provide Kinexon API settings from environment."""
    return Settings()


@pytest.fixture(scope="session")
def client(settings: Settings) -> KinexonClient:
    """Authenticated KinexonClient instance for integration tests."""
    client = KinexonClient(settings)
    logger.info("KinexonClient authenticated successfully.")
    return client
