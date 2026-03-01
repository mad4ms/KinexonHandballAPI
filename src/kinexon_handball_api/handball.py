"""Handball API wrapper for Kinexon API.
Provides convenience methods using generated kinexon_client functions.
"""

from __future__ import annotations

import contextlib
import logging
from datetime import datetime
from typing import Any, TypeVar, cast

import httpx
from kinexon_client.api.available_metrics_and_events import (
    get_public_v1_statistics_list,
)
from kinexon_client.api.events import (
    get_public_v_1_events_event_type_player_players_time_entity_type_time_entity_identifier,
)
from kinexon_client.api.exports import (
    get_public_v1_export_positions_session_by_time_entity_identifier,
)
from kinexon_client.api.players import get_public_v1_teams_by_team_id_players
from kinexon_client.api.sessions_and_phases import (
    get_public_v1_teams_by_team_id_sessions_and_phases,
)
from kinexon_client.types import UNSET
from tqdm import tqdm

from kinexon_handball_api.api import KinexonAPI
from kinexon_handball_api.fetchers import TeamEntry, fetch_team_ids

logger = logging.getLogger(__name__)

T = TypeVar("T")


def _bool_str(value: bool) -> str:
    return "true" if value else "false"


class HandballAPI(KinexonAPI):
    """High-level wrapper around Kinexon handball endpoints."""

    @staticmethod
    def _require_value(name: str, value: Any) -> None:
        if value is None or value == "":
            raise ValueError(f"{name} must be provided.")

    @staticmethod
    def _handle_response(
        response: Any,
        context: str,
        default: T,
        *,
        ok_statuses: set[int] | None = None,
    ) -> T:
        """Validate a generated response and return parsed payload or fallback."""
        allowed = ok_statuses or {200}
        if response.status_code not in allowed:
            content = getattr(response, "content", None)
            raise RuntimeError(f"{context}: HTTP {response.status_code}: {content!r}")
        if response.parsed is not None:
            return cast(T, response.parsed)
        return default

    @staticmethod
    def _to_iso(value: datetime | str) -> str:
        return value.isoformat() if isinstance(value, datetime) else value

    def get_team_ids(self, season: str | None = None) -> list[TeamEntry]:
        """Return team IDs for a season (or default season behavior)."""
        return fetch_team_ids(season)

    def get_events_for_session(
        self,
        event_type: str = "detected_shot_handball",
        players: str = "in-entity",
        session_id: str = "latest",
    ) -> Any:
        self._require_value("session_id", session_id)
        resp = get_public_v_1_events_event_type_player_players_time_entity_type_time_entity_identifier.sync_detailed(  # noqa: E501
            event_type=event_type,
            players=players,
            time_entity_type="session",
            time_entity_identifier=session_id,
            client=self.client,
        )
        return self._handle_response(resp, "events_for_session", {})

    def get_available_metrics_and_events(self) -> Any:
        resp = get_public_v1_statistics_list.sync_detailed(client=self.client)
        return self._handle_response(resp, "available_metrics_and_events", {})

    def get_sessions_for_team(
        self,
        team_id: int,
        start: datetime | str,
        end: datetime | str,
    ) -> Any:
        self._require_value("team_id", team_id)
        resp = get_public_v1_teams_by_team_id_sessions_and_phases.sync_detailed(
            team_id=team_id,
            min_=self._to_iso(start),
            max_=self._to_iso(end),
            client=self.client,
        )
        return self._handle_response(resp, "sessions_for_team", {})

    def get_team_players(self, team_id: int) -> Any:
        self._require_value("team_id", team_id)
        resp = get_public_v1_teams_by_team_id_players.sync_detailed(
            team_id=team_id,
            client=self.client,
        )
        return self._handle_response(resp, "team_players", {})

    def get_positions_csv(
        self,
        session_id: str,
        update_rate: int = 20,
        group_by_ts: bool = True,
        players: str | None = None,
    ) -> str:
        self._require_value("session_id", session_id)
        resp = get_public_v1_export_positions_session_by_time_entity_identifier.sync_detailed(  # noqa: E501
            time_entity_identifier=session_id,
            client=self.client,
            update_rate=update_rate,
            group_by_timestamp=group_by_ts,
            players=players or UNSET,
        )
        return self._handle_response(resp, "positions_csv", "")

    def download_positions_csv_via_custom(  # noqa: PLR0913, PLR0912
        self,
        session_id: str,
        *,
        update_rate: int = 20,
        compress_output: bool = False,
        use_local_frame_imu: bool = False,
        center_origin: bool = False,
        group_by_timestamp: bool = False,
        players: str | None = None,
        max_bytes: int | None = None,
        chunk_size: int = 1024 * 1024,
        show_progress: bool = True,
        timeout: float | None = None,
    ) -> bytes:
        """Download positions CSV via streaming custom request.

        If max_bytes is set, the download stops after that many bytes.
        """
        self._require_value("session_id", session_id)

        max_bytes_remaining = max_bytes if max_bytes and max_bytes > 0 else None

        params: dict[str, Any] = {
            "updateRate": update_rate,
            "compressOutput": _bool_str(compress_output),
            "useLocalFrameIMU": _bool_str(use_local_frame_imu),
            "centerOrigin": _bool_str(center_origin),
            "groupByTimestamp": _bool_str(group_by_timestamp),
        }
        if players:
            params["players"] = players

        headers = {"Accept": "text/csv"}
        if compress_output:
            headers["Accept-Encoding"] = "gzip, zip"

        url = f"/public/v1/export/positions/session/{session_id}"
        resp = self.make_custom_request(
            "GET",
            url,
            params=params,
            headers=headers,
            stream=True,
            timeout=timeout,
        )

        try:
            resp.raise_for_status()
            total = int(resp.headers.get("Content-Length", "0")) or None
            buf = bytearray()

            if show_progress:
                with tqdm(
                    total=total,
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
                    desc=f"Downloading file for session {session_id}",
                ) as bar:
                    for chunk in resp.iter_bytes(chunk_size=chunk_size):
                        if chunk:
                            if max_bytes_remaining is None:
                                buf.extend(chunk)
                                bar.update(len(chunk))
                            else:
                                take = min(len(chunk), max_bytes_remaining)
                                if take:
                                    buf.extend(chunk[:take])
                                    bar.update(take)
                                    max_bytes_remaining -= take
                                if max_bytes_remaining == 0:
                                    break
            else:
                for chunk in resp.iter_bytes(chunk_size=chunk_size):
                    if chunk:
                        if max_bytes_remaining is None:
                            buf.extend(chunk)
                        else:
                            take = min(len(chunk), max_bytes_remaining)
                            if take:
                                buf.extend(chunk[:take])
                                max_bytes_remaining -= take
                            if max_bytes_remaining == 0:
                                break
        except httpx.HTTPStatusError as exc:
            text = ""
            with contextlib.suppress(Exception):
                text = resp.text
            raise RuntimeError(f"HTTP {resp.status_code}: {text}") from exc
        finally:
            resp.close()

        logger.debug("Downloaded %d bytes for session %s", len(buf), session_id)
        return bytes(buf)
