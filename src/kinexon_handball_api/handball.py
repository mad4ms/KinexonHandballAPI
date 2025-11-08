"""
Handball API wrapper for Kinexon API.
Provides convenience methods using generated kinexon_client functions.

Author: Michael Adams, 2025
"""

from typing import Any, Dict, List, Optional
import logging
import httpx
from pathlib import Path
from tqdm import tqdm
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


def _bool_str(v: bool) -> str:
    return "true" if v else "false"


class HandballAPI(KinexonAPI):
    """
    High-level wrapper around Kinexon handball endpoints.
    """

    def get_available_metrics_and_events(self) -> Any:
        resp = get_public_v1_statistics_list.sync_detailed(
            client=self.client,
        )
        if resp.status_code != 200:
            raise RuntimeError(f"HTTP {resp.status_code}: {resp.content!r}")
        return resp.parsed or {}

    def get_team_ids(
        self, season: Optional[str] = None
    ) -> List[Dict[str, int]]:
        """
        Fetch the list of team IDs from the Kinexon API.
        Returns:
            List[Dict[str, int]]: List of team IDs and names.
        """
        return fetch_team_ids(season)

    def get_sessions_for_team(self, team_id: int, start: str, end: str) -> Any:
        resp = (
            get_public_v1_teams_by_team_id_sessions_and_phases.sync_detailed(
                team_id=team_id,
                min_=start,
                max_=end,
                client=self.client,
            )
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

    def download_positions_csv_via_custom(
        self,
        session_id: str,
        *,
        update_rate: int = 20,
        compress_output: bool = False,
        use_local_frame_imu: bool = False,
        center_origin: bool = False,
        group_by_timestamp: bool = False,
        players: Optional[str] = None,
        chunk_size: int = 1024 * 1024,
        show_progress: bool = True,
    ) -> bytes:
        """
        Mirrors legacy _fetch_game_csv_data behavior using the base make_custom_request.

        Returns the CSV bytes (optionally compressed depending on API settings).
        """

        # Legacy semantics: booleans as lowercase strings
        def b(x: bool) -> str:
            return "true" if x else "false"

        params: Dict[str, Any] = {
            "updateRate": update_rate,
            "compressOutput": b(compress_output),
            "useLocalFrameIMU": b(use_local_frame_imu),
            "centerOrigin": b(center_origin),
            "groupByTimestamp": b(group_by_timestamp),
        }
        if players:
            params["players"] = players

        headers = {"Accept": "text/csv"}

        # NOTE: public path (matches the generated client variant)
        url = f"/public/v1/export/positions/session/{session_id}"

        # Request with streaming enabled
        resp = self.make_custom_request(
            "GET",
            url,
            params=params,
            headers=headers,
            stream=True,
        )

        # Raise early for non-200
        try:
            resp.raise_for_status()
        except httpx.HTTPStatusError as e:
            text = ""
            try:
                text = resp.text
            except Exception:
                pass
            raise RuntimeError(f"HTTP {resp.status_code}: {text}") from e

        # Progress: use Content-Length when available
        total = int(resp.headers.get("Content-Length", "0")) or None
        buf = bytearray()

        if show_progress and tqdm is not None:
            with tqdm(
                total=total,
                unit="B",
                unit_scale=True,
                unit_divisor=1024,
                desc="Downloading CSV",
            ) as bar:
                for chunk in resp.iter_bytes(chunk_size=chunk_size):
                    if chunk:
                        buf.extend(chunk)
                        bar.update(len(chunk))
        else:
            for chunk in resp.iter_bytes(chunk_size=chunk_size):
                if chunk:
                    buf.extend(chunk)

        resp.close()
        return bytes(buf)


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
        username_basic=os.getenv(
            "USERNAME_KINEXON_SESSION", "your_username_here"
        ),
        password_basic=os.getenv(
            "PASSWORD_KINEXON_SESSION", "your_password_here"
        ),
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

    print("Team IDs:", len(ids_team))

    print(
        f"Team Players for team {ids_team[0]['id']}:",
        api.get_team_players(team_id=ids_team[0]["id"]),
    )

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
            len(sessions),
        )

        # 2) call the custom downloader (mirrors your legacy semantics)
        csv_bytes = api.download_positions_csv_via_custom(
            session_id=sessions[0].session_id,
            update_rate=20,
            compress_output=True,  # True -> often returns gzip-compressed CSV
            use_local_frame_imu=False,
            center_origin=False,
            group_by_timestamp=False,
            players=None,  # or "123,456,789"
            chunk_size=512 * 1024,  # 512 KB chunks
            show_progress=True,  # requires tqdm installed; otherwise ignored
        )

        # 3) write to disk (name accordingly if compressed)
        out_path = "positions.csv.gz" if True else "positions.csv"
        with open(out_path, "wb") as f:
            f.write(csv_bytes)
        print(f"Wrote {len(csv_bytes):,} bytes to {out_path}")
