import logging
import pytest

# Configure logging for this test file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@pytest.mark.integration
def test_extract_game(client):
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

        # first item of sessions
        first_session = sessions[0] if sessions else None

        if first_session:
            client.get_position_data_by_session_id(first_session["session_id"])

        break


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     pytest.main(["-v", __file__])
