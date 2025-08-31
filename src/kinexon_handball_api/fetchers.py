from pathlib import Path
from typing import Dict, List, Optional

import yaml


def _load_teams_config() -> Dict:
    """Load teams configuration from YAML file."""
    config_path = Path(__file__).parent / "config" / "teams.yaml"

    if not config_path.exists():
        raise FileNotFoundError(f"Teams config file not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def fetch_team_ids(season: Optional[str] = None) -> List[Dict[str, int]]:
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
        season = config.get("current_season", "2025-26")

    teams = config.get("seasons", {}).get(season)
    if teams is None:
        available_seasons = list(config.get("seasons", {}).keys())
        raise ValueError(
            f"Season '{season}' not found. Available seasons: {available_seasons}"
        )

    return teams


def get_available_seasons() -> List[str]:
    """Get list of available seasons."""
    config = _load_teams_config()
    return list(config.get("seasons", {}).keys())


def get_current_season() -> str:
    """Get the current season from config."""
    config = _load_teams_config()
    return config.get("current_season", "2025-26")
