# Kinexon Handball API

A Python wrapper for Kinexon Handball that performs session + main authentication, injects an API key, and wraps a generated OpenAPI client. It provides simple helpers for common handball endpoints (metrics/events, sessions, players, position exports).

## Requirements
- Python 3.13+
- Package manager uv
- Valid Kinexon credentials (session and main usernames/passwords, API key, endpoints)

## Installation
```bash
git clone https://github.com/mad4ms/KinexonHandballAPI.git
cd KinexonHandballAPI
uv pip install -e .
```

## Configuration
Provide credentials via environment variables. A `.env` file is supported (python-dotenv).

Example `.env`:
```env
# API key header
API_KEY_KINEXON=your_api_key

# Session auth (step 1)
USERNAME_KINEXON_SESSION=your_session_username
PASSWORD_KINEXON_SESSION=your_session_password
ENDPOINT_KINEXON_SESSION=https://hbl-cloud.kinexon.com/api/session

# Main auth (step 2)
USERNAME_KINEXON_MAIN=your_main_username
PASSWORD_KINEXON_MAIN=your_main_password
ENDPOINT_KINEXON_MAIN=https://hbl-cloud.kinexon.com/api

# Base URL for API client
# Used as base_url when constructing the client
ENDPOINT_KINEXON_API=https://hbl-cloud.kinexon.com/api
```

## Quick Start
```python
from dotenv import load_dotenv
import os
from kinexon_handball_api.handball import HandballAPI
from kinexon_handball_api.fetchers import fetch_team_ids

load_dotenv()

api = HandballAPI(
    base_url=os.getenv("ENDPOINT_KINEXON_API", "https://hbl-cloud.kinexon.com/api"),
    api_key=os.getenv("API_KEY_KINEXON", ""),
    username_basic=os.getenv("USERNAME_KINEXON_SESSION", ""),
    password_basic=os.getenv("PASSWORD_KINEXON_SESSION", ""),
    username_main=os.getenv("USERNAME_KINEXON_MAIN", ""),
    password_main=os.getenv("PASSWORD_KINEXON_MAIN", ""),
    endpoint_session=os.getenv("ENDPOINT_KINEXON_SESSION", "https://hbl-cloud.kinexon.com/api/session"),
    endpoint_main=os.getenv("ENDPOINT_KINEXON_MAIN", "https://hbl-cloud.kinexon.com/api"),
)

avail = api.get_available_metrics_and_events()
print("Available metrics/events:", avail)

teams = fetch_team_ids()
print(f"Teams: {len(teams)}")

players = api.get_team_players(team_id=teams[0]["id"])
print("Players:", players)
```

## Project Structure (high level)
- `src/kinexon_handball_api/`
  - `api.py` — Core client (two-step auth + API key header)
  - `handball.py` — Handball helpers (metrics/events, sessions, players, positions)
  - `fetchers.py` — Local team ID registry loaded from `config/teams.yaml`
- `src/_vendor/kinexon_client/` — Generated OpenAPI client (vendored)
- `openapi/` — OpenAPI spec and generator config
- `scripts/` — Client regeneration scripts
- `tests/` — Unit tests

## Regenerate the OpenAPI Client (optional)
The client is generated with `openapi-python-client` and vendored into `src/_vendor/kinexon_client`.

```bash
# ensure dev tools
uv pip install -e ".[dev]"
# run the generator (bash)
./scripts/codegen.sh
```

The script downloads the spec, generates the client, moves it under `src/_vendor/kinexon_client`, and cleans up.

## Testing
```bash
pytest -q
```

## License
MIT — see `LICENSE`.

## Disclaimer
This project is an unofficial wrapper and is not affiliated with Kinexon. API access requires a valid contract and credentials from Kinexon.
