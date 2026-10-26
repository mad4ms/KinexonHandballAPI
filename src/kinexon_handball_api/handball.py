"""Handball API wrapper for Kinexon API.
Provides convenience methods using generated kinexon_client functions.
"""

from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path
from typing import Any, TypeVar, cast

import httpx
from kinexon_client.api.available_metrics_and_events import (
    get_public_v1_statistics_list,
)
from kinexon_client.api.events import get_public_v1_events_by_event_type_player
from kinexon_client.api.exports import (
    get_public_v1_export_positions_session_by_time_entity_identifier,
)
from kinexon_client.api.players import get_public_v1_teams_by_team_id_players
from kinexon_client.api.sessions_and_phases import (
    get_public_v1_teams_by_team_id_sessions_and_phases,
)
from kinexon_client.types import UNSET

from kinexon_handball_api.api import KinexonAPI
from kinexon_handball_api.exports import (
    ExportKind,
    export_params,
    stream_export,
    stream_export_to_file,
)
from kinexon_handball_api.fetchers import TeamEntry, fetch_team_ids

logger = logging.getLogger(__name__)

T = TypeVar("T")


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
        resp = get_public_v1_events_by_event_type_player.sync_detailed(
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

        # Convert strings to datetime objects if necessary
        if isinstance(start, str):
            start = datetime.fromisoformat(start)
        if isinstance(end, str):
            end = datetime.fromisoformat(end)

        resp = get_public_v1_teams_by_team_id_sessions_and_phases.sync_detailed(
            team_id=team_id,
            min_=start,
            max_=end,
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

    def download_positions_csv_via_custom(  # noqa: PLR0913
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
        """Download the positions CSV of a session; ``max_bytes`` stops early."""
        self._require_value("session_id", session_id)
        params = export_params(
            update_rate=update_rate,
            compress_output=compress_output,
            use_local_frame_imu=use_local_frame_imu,
            players=players,
            center_origin=center_origin,
            group_by_timestamp=group_by_timestamp,
        )
        return self._download(
            "positions", session_id, params, max_bytes=max_bytes,
            chunk_size=chunk_size, show_progress=show_progress, timeout=timeout,
        )  # fmt: skip

    def download_inertial_csv_via_custom(  # noqa: PLR0913
        self,
        session_id: str,
        *,
        update_rate: int = 20,
        compress_output: bool = False,
        use_local_frame_imu: bool = False,
        players: str | None = None,
        max_bytes: int | None = None,
        chunk_size: int = 1024 * 1024,
        show_progress: bool = True,
        timeout: float | None = None,
    ) -> bytes:
        """Download the inertial (IMU) CSV of a session; ``max_bytes`` stops early.

        Columns include game time, x/y/z, heart rate, RR intervals,
        accelerometer, gyroscope and orientation quaternion per sensor.
        """
        self._require_value("session_id", session_id)
        params = export_params(
            update_rate=update_rate,
            compress_output=compress_output,
            use_local_frame_imu=use_local_frame_imu,
            players=players,
        )
        return self._download(
            "inertial", session_id, params, max_bytes=max_bytes,
            chunk_size=chunk_size, show_progress=show_progress, timeout=timeout,
        )  # fmt: skip

    def download_export_to_file(  # noqa: PLR0913
        self,
        kind: ExportKind,
        session_id: str,
        path: str | Path,
        *,
        update_rate: int = 20,
        use_local_frame_imu: bool = False,
        players: str | None = None,
        max_bytes: int | None = None,
        show_progress: bool = False,
        timeout: float | None = None,
    ) -> int:
        """Stream a ``positions`` or ``inertial`` export to ``path``; return bytes.

        The file is written as ``<path>.part`` and renamed when complete, so the
        export is never held in memory.
        """
        self._require_value("session_id", session_id)
        params = export_params(
            update_rate=update_rate,
            use_local_frame_imu=use_local_frame_imu,
            players=players,
        )
        return stream_export_to_file(
            self, kind, session_id, params, path,
            max_bytes=max_bytes, show_progress=show_progress, timeout=timeout,
        )  # fmt: skip

    def _download(  # noqa: PLR0913
        self,
        kind: ExportKind,
        session_id: str,
        params: dict[str, Any],
        *,
        max_bytes: int | None,
        chunk_size: int,
        show_progress: bool,
        timeout: float | None,
    ) -> bytes:
        buf = bytearray()
        stream_export(
            self, kind, session_id, params, buf.extend,
            max_bytes=max_bytes, chunk_size=chunk_size,
            show_progress=show_progress, timeout=timeout,
        )  # fmt: skip
        logger.debug(
            "Downloaded %d bytes of %s for session %s", len(buf), kind, session_id
        )
        return bytes(buf)

    # -- JSON endpoints of a session, phase or player ------------------------

    def _get_json(self, url: str, params: dict[str, Any] | None = None) -> Any:
        try:
            resp = self.make_custom_request(
                "GET", url, params=params, headers={"Accept": "application/json"}
            )
        except httpx.HTTPStatusError as exc:
            raise RuntimeError(
                f"{url}: HTTP {exc.response.status_code}: {exc.response.text}"
            ) from exc
        return resp.json()

    def get_events(
        self,
        event_type: str,
        time_entity_id: str,
        *,
        time_entity_type: str = "session",
        players: str = "in-entity",
    ) -> list[dict[str, Any]]:
        """Events of one type for a session or phase, as plain dicts.

        Some types exist beyond ``get_available_metrics_and_events()``, e.g.
        ``change_of_orientation``; ``get_event_counts`` shows what a session has.
        """
        self._require_value("time_entity_id", time_entity_id)
        url = (
            f"/public/v1/events/{event_type}/player/{players}"
            f"/{time_entity_type}/{time_entity_id}"
        )
        return cast(list[dict[str, Any]], self._get_json(url))

    def get_event_counts(
        self,
        time_entity_id: str,
        *,
        time_entity_type: str = "session",
        players: str = "in-entity",
    ) -> dict[str, int]:
        """Number of events per event type in a session or phase."""
        self._require_value("time_entity_id", time_entity_id)
        url = (
            f"/public/v1/events/count-per-event-type/player/{players}"
            f"/{time_entity_type}/{time_entity_id}"
        )
        return cast(dict[str, int], self._get_json(url))

    def get_sensor_assignment(self, session_id: str) -> list[dict[str, Any]]:
        """Which sensor each player (with number, position, team) wore in a session."""
        self._require_value("session_id", session_id)
        return cast(
            list[dict[str, Any]],
            self._get_json(f"/public/v1/sensor-assignment/{session_id}"),
        )

    def get_player_statistics(
        self,
        player_id: int,
        time_entity_id: str,
        *,
        time_entity_type: str = "session",
        fields: list[str] | None = None,
    ) -> list[dict[str, Any]]:
        """All metrics (or ``fields``) of one player for a session or a phase (half)."""
        self._require_value("player_id", player_id)
        self._require_value("time_entity_id", time_entity_id)
        url = (
            f"/public/v1/statistics/player/{player_id}"
            f"/{time_entity_type}/{time_entity_id}"
        )
        params = {"fields": ",".join(fields)} if fields else None
        return cast(list[dict[str, Any]], self._get_json(url, params))

    def get_session_categories(self, session_id: str) -> dict[str, Any]:
        """Category thresholds (speed, acceleration, jump, ...) of a session."""
        self._require_value("session_id", session_id)
        return cast(
            dict[str, Any],
            self._get_json(f"/public/v1/statistics/{session_id}/categories"),
        )
