import logging
import pytest

logger = logging.getLogger(__name__)


@pytest.mark.integration
def test_session_ids(client):
    """Integration smoke test: fetch session IDs for all teams."""
    teams = client.get_team_ids()
    assert isinstance(teams, list)
    assert teams, "Expected at least one team"

    logger.info("Fetched %s teams.", len(teams))

    for team in teams:
        assert "id" in team
        assert "name" in team

        sessions = client.get_session_ids(
            team["id"], "2025-08-01", "2026-07-31"
        )
        assert isinstance(sessions, list)

        logger.info(
            "Team %s (%s): %s sessions",
            team["id"],
            team["name"],
            len(sessions),
        )

        for session in sessions:
            assert "session_id" in session
            assert "description" in session
            assert "start_session" in session
