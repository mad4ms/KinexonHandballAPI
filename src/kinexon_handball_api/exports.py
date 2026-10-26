"""Streaming CSV exports of a session: positions and inertial (IMU) data.

Kinexon builds an export on request and answers with a chunked body without
``Content-Length``; a full game is ~160 MB of positions and takes minutes.
``stream_export`` hands every chunk to a sink, so callers can collect bytes
or write straight to disk without holding the file in memory twice.
"""

from __future__ import annotations

import contextlib
import os
from collections.abc import Callable
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal

import httpx
from tqdm import tqdm

if TYPE_CHECKING:
    from kinexon_handball_api.api import KinexonAPI

ExportKind = Literal["positions", "inertial"]


def _bool_str(value: bool) -> str:
    return "true" if value else "false"


def export_params(  # noqa: PLR0913
    *,
    update_rate: int = 20,
    compress_output: bool = False,
    use_local_frame_imu: bool = False,
    players: str | None = None,
    center_origin: bool | None = None,
    group_by_timestamp: bool | None = None,
) -> dict[str, Any]:
    """Query parameters of an export; the last two exist only for positions."""
    params: dict[str, Any] = {
        "updateRate": update_rate,
        "compressOutput": _bool_str(compress_output),
        "useLocalFrameIMU": _bool_str(use_local_frame_imu),
    }
    if center_origin is not None:
        params["centerOrigin"] = _bool_str(center_origin)
    if group_by_timestamp is not None:
        params["groupByTimestamp"] = _bool_str(group_by_timestamp)
    if players:
        params["players"] = players
    return params


def stream_export(  # noqa: PLR0913
    api: KinexonAPI,
    kind: ExportKind,
    session_id: str,
    params: dict[str, Any],
    sink: Callable[[bytes], object],
    *,
    max_bytes: int | None = None,
    chunk_size: int = 1024 * 1024,
    show_progress: bool = True,
    timeout: float | None = None,
) -> int:
    """Stream one export into ``sink``; return the number of bytes delivered.

    With ``max_bytes`` the download stops after that many bytes (a sample).
    """
    headers = {"Accept": "text/csv"}
    if params.get("compressOutput") == "true":
        headers["Accept-Encoding"] = "gzip, zip"
    resp = api.make_custom_request(
        "GET",
        f"/public/v1/export/{kind}/session/{session_id}",
        params=params,
        headers=headers,
        stream=True,
        timeout=timeout,
    )
    remaining = max_bytes if max_bytes and max_bytes > 0 else None
    written = 0
    try:
        resp.raise_for_status()
        with tqdm(
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
            desc=f"{kind} export of session {session_id}",
            disable=not show_progress,
        ) as bar:
            for received in resp.iter_bytes(chunk_size=chunk_size):
                chunk = received if remaining is None else received[:remaining]
                if remaining is not None:
                    remaining -= len(chunk)
                if chunk:
                    sink(chunk)
                    written += len(chunk)
                    bar.update(len(chunk))
                if remaining == 0:
                    break
    except httpx.HTTPStatusError as exc:
        text = ""
        with contextlib.suppress(Exception):
            text = resp.read().decode(errors="replace")
        raise RuntimeError(f"HTTP {resp.status_code}: {text}") from exc
    finally:
        resp.close()
    return written


def stream_export_to_file(
    api: KinexonAPI,
    kind: ExportKind,
    session_id: str,
    params: dict[str, Any],
    path: str | Path,
    **options: Any,
) -> int:
    """Stream one export to ``path`` via a ``.part`` file renamed at the end."""
    target = Path(path)
    partial = target.with_name(target.name + ".part")
    try:
        with partial.open("wb") as handle:
            written = stream_export(
                api, kind, session_id, params, handle.write, **options
            )
        os.replace(partial, target)
    finally:
        partial.unlink(missing_ok=True)
    return written
