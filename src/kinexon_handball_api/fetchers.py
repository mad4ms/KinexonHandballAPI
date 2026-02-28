from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional, TypedDict

import yaml

DEFAULT_SEASON = "2025-26"


class TeamEntry(TypedDict):
    id: int
    name: str


@lru_cache(maxsize=1)
def _load_teams_config() -> Dict[str, Any]:
    """Load teams configuration from YAML file."""
    config_path = Path(__file__).parent / "config" / "teams.yaml"

    if not config_path.exists():
        raise FileNotFoundError(f"Teams config file not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict):
        raise ValueError("Teams config must be a mapping at the top level.")

    return data


def _get_current_season(config: Dict[str, Any]) -> str:
    """Return configured current season with a stable fallback."""
    value = config.get("current_season")
    return value if isinstance(value, str) and value else DEFAULT_SEASON


def _validate_teams(season: str, teams: Any) -> List[TeamEntry]:
    if not isinstance(teams, list):
        raise ValueError(
            f"Season '{season}' teams must be a list, got {type(teams).__name__}."
        )
    normalized: List[TeamEntry] = []
    for entry in teams:
        if not isinstance(entry, dict):
            raise ValueError(
                f"Season '{season}' team entries must be mappings, got {type(entry).__name__}."
            )
        team_id = entry.get("id")
        name = entry.get("name")
        if not isinstance(team_id, int) or not isinstance(name, str):
            raise ValueError(
                f"Season '{season}' team entries must include int 'id' and str 'name'."
            )
        normalized.append({"id": team_id, "name": name})
    return normalized


def fetch_team_ids(season: Optional[str] = None) -> List[TeamEntry]:
    """
    Return the list of Kinexon team IDs for a specific season.

    Args:
        season: Season in format "YYYY-YY" (e.g., "2025-26").
                If None, uses current season from config.

    Returns:
        List of team dictionaries with 'id' and 'name' keys.

    How to get the Team IDs, as they are not available via the API:
    - Go to the Kinexon Cloud web app.
    - Click on the "Team" selection dropdown.
    - Click user -> profile
    - Switch to "Teams" tab.
    - The IDs next to the name are the team IDs.
    - Copy the IDs and names into config/teams.yaml for a new season.
    """
    config = _load_teams_config()

    if season is None:
        season = _get_current_season(config)

    teams = config.get("seasons", {}).get(season)
    if teams is None:
        available_seasons = list(config.get("seasons", {}).keys())
        raise ValueError(
            f"Season '{season}' not found. Available seasons: {available_seasons}"
        )
    return _validate_teams(season, teams)


def get_available_seasons() -> List[str]:
    """Get list of available seasons."""
    config = _load_teams_config()
    return list(config.get("seasons", {}).keys())


def get_current_season() -> str:
    """Get the current season from config."""
    config = _load_teams_config()
    return _get_current_season(config)
