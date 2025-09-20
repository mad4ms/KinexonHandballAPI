"""
Handball API wrapper for Kinexon API.
Provides convenience methods using generated kinexon_client functions.

Author: Michael Adams, 2025
"""

from typing import Any, Dict, List, Optional

from kinexon_client.api.available_metrics_and_events import (
    get_public_v1_statistics_list,
)

# Import generated API functions
from kinexon_client.api.exports import (
    get_public_v1_export_positions_session_by_time_entity_identifier,
)
from kinexon_client.api.players import get_public_v1_teams_by_team_id_players
from kinexon_client.api.sessions_and_phases import (
    get_public_v1_teams_by_team_id_sessions_and_phases,
)
from kinexon_client.types import UNSET

from kinexon_handball_api.api import KinexonAPI
from kinexon_handball_api.fetchers import fetch_team_ids


class HandballAPI(KinexonAPI):
    """
    High-level wrapper around Kinexon DataCore handball endpoints.
    """

    def get_available_metrics_and_events(self) -> Any:
        resp = get_public_v1_statistics_list.sync_detailed(
            client=self.client,
        )
        if resp.status_code != 200:
            raise RuntimeError(f"HTTP {resp.status_code}: {resp.content!r}")
        return resp.parsed or {}

    def get_team_ids(self, season: Optional[str] = None) -> List[Dict[str, int]]:
        """
        Fetch the list of team IDs from the Kinexon API.
        Returns:
            List[Dict[str, int]]: List of team IDs and names.
        """
        return fetch_team_ids(season)

    def get_sessions_for_team(self, team_id: int, start: str, end: str) -> Any:
        resp = get_public_v1_teams_by_team_id_sessions_and_phases.sync_detailed(
            team_id=team_id,
            min_=start,
            max_=end,
            client=self.client,
        )
        if resp.status_code != 200:
            raise RuntimeError(f"HTTP {resp.status_code}: {resp.content!r}")
        return resp.parsed or {}

    def get_team_players(self, team_id: int) -> Any:
        resp = get_public_v1_teams_by_team_id_players.sync_detailed(
            team_id=team_id,
            client=self.client,
        )
        if resp.status_code != 200:
            raise RuntimeError(f"HTTP {resp.status_code}: {resp.content!r}")
        return resp.parsed or {}

    def get_positions_csv(
        self,
        session_id: str,
        update_rate: int = 20,
        group_by_ts: bool = True,
        players: Optional[str] = None,
    ) -> str:
        return get_public_v1_export_positions_session_by_time_entity_identifier.sync(
            time_entity_identifier=session_id,
            client=self.client,
            update_rate=update_rate,
            group_by_timestamp=group_by_ts,
            players=players or UNSET,
        )


if __name__ == "__main__":
    import os
    from datetime import datetime

    from dotenv import load_dotenv

    load_dotenv()

    api = HandballAPI(
        base_url=os.getenv(
            "ENDPOINT_KINEXON_SESSION", "https://hbl-cloud.kinexon.com/api"
        ),
        api_key=os.getenv("API_KEY_KINEXON", "your_api_key_here"),
        username_basic=os.getenv("USERNAME_KINEXON_SESSION", "your_username_here"),
        password_basic=os.getenv("PASSWORD_KINEXON_SESSION", "your_password_here"),
        username_main=os.getenv("USERNAME_KINEXON_MAIN", "your_username_here"),
        password_main=os.getenv("PASSWORD_KINEXON_MAIN", "your_password_here"),
        endpoint_session=os.getenv(
            "ENDPOINT_KINEXON_SESSION",
            "https://hbl-cloud.kinexon.com/api/session",
        ),
        endpoint_main=os.getenv(
            "ENDPOINT_KINEXON_MAIN",
            "https://hbl-cloud.kinexon.com/api",
        ),
        timeout=10000,
    )
    avail = api.get_available_metrics_and_events()
    # print("Available metrics and events:", len(avail))

    ids_team = fetch_team_ids()

    print("Team IDs:", ids_team)

    print(api.get_team_players(team_id=ids_team[0]["id"]))

    if ids_team:
        team_id = ids_team[0]["id"]
        sessions = api.get_sessions_for_team(
            team_id=team_id,
            start=datetime.fromisoformat("2024-08-01T00:00:00+00:00"),
            end=datetime.fromisoformat("2025-08-01T00:00:00+00:00"),
        )
        # print session ids and names
        print(
            f"Sessions for team {team_id}:",
            [(s.session_id, s.description) for s in sessions],
        )

        api.get_positions_csv(
            session_id=sessions[0].session_id,
            update_rate=20,
            group_by_ts=True,
            players=None,
        )
