import logging
import pytest

logger = logging.getLogger(__name__)


@pytest.mark.integration
def test_api_status(client):
    """Integration smoke test: authenticate and fetch available metrics/events."""
    metrics = client.get_available_metrics_and_events()

    assert isinstance(metrics, dict)
    assert "metrics" in metrics
    assert "events" in metrics

    logger.info(
        "Fetched %s metrics and %s events.",
        len(metrics.get("metrics", [])),
        len(metrics.get("events", [])),
    )
