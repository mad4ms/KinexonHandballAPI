# Kinexon Handball API


[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


A Python wrapper for the Kinexon Handball API.

This library simplifies interaction with the Kinexon API by handling complex two-step authentication automatically and providing a fully typed interface for all API endpoints.

## Features

- **Automated Authentication**: Handles the multi-step login process (Session + Main) and API key injection automatically.
- **Fully Typed**: Built on top of a generated OpenAPI client, ensuring type safety for requests and response models.
- **High-Level Helpers**: Convenient methods for common workflows (e.g., fetching metrics, team rosters, and position data).
- **Hybrid Architecture**:
  - Use high-level helpers in `kinexon_handball_api` for ease of use.
  - Access the underlying `kinexon_client` for raw access to every single API endpoint generated from the official spec.

## Installation

This project requires **Python 3.13+**.

### Using uv (Recommended)
If you use [uv](https://github.com/astral-sh/uv) for fast package management:

```bash
git clone https://github.com/mad4ms/KinexonHandballAPI.git
cd KinexonHandballAPI
uv sync
```

If you prefer an editable install instead of syncing a lockfile:

```bash
uv pip install -e "."
```

## Configuration

The library uses **python-dotenv** to manage configuration. You can provide credentials via a `.env` file in your project root or via environment variables.

Create a `.env` file:

```env
# API Authorization
API_KEY_KINEXON=your_api_key

# Step 1: Session Authentication
USERNAME_KINEXON_SESSION=your_session_username
PASSWORD_KINEXON_SESSION=your_session_password
ENDPOINT_KINEXON_SESSION=https://hbl-cloud.kinexon.com/

# Step 2: Main Authentication
USERNAME_KINEXON_MAIN=your_main_username
PASSWORD_KINEXON_MAIN=your_main_password
ENDPOINT_KINEXON_MAIN=https://hbl-cloud.kinexon.com/checklogin

# API Base Configuration (no trailing /public/v1)
ENDPOINT_KINEXON_API=https://hbl-cloud.kinexon.com
```

Note: The two-step authentication requires separate credentials for each step.

## Usage

### Basic Example

The main entry point is the `HandballAPI` class.

```python
import os
from dotenv import load_dotenv
from kinexon_handball_api.handball import HandballAPI
from kinexon_handball_api.fetchers import fetch_team_ids

# 1. Load configuration
load_dotenv()

# 2. Initialize the API
api = HandballAPI(
  base_url=os.getenv("ENDPOINT_KINEXON_API", ""),
  api_key=os.getenv("API_KEY_KINEXON", ""),
  username_basic=os.getenv("USERNAME_KINEXON_SESSION", ""),
  password_basic=os.getenv("PASSWORD_KINEXON_SESSION", ""),
  username_main=os.getenv("USERNAME_KINEXON_MAIN", ""),
  password_main=os.getenv("PASSWORD_KINEXON_MAIN", ""),
  endpoint_session=os.getenv("ENDPOINT_KINEXON_SESSION", ""),
  endpoint_main=os.getenv("ENDPOINT_KINEXON_MAIN", ""),
)

# 3. Use high-level helpers
# Fetch available metrics
metrics = api.get_available_metrics_and_events()
print(f"Found {len(metrics)} available metrics.")

# Get players for a specific team
teams = fetch_team_ids()
if teams:
    first_team = teams[0]
    players = api.get_team_players(team_id=first_team["id"])
    print(f"Team {first_team['name']} has {len(players)} players.")
```

### Advanced: Accessing Raw Client

For endpoints not covered by high-level helpers, accessing the generated client directly is supported and encouraged. The generated client resides in `kinexon_client`.

```python
from kinexon_client.api.players import get_public_v1_teams_by_team_id_players
from kinexon_client.models import PlayerModel

# You can access the authenticated low-level client via `api.client`
response = get_public_v1_teams_by_team_id_players.sync_detailed(
    client=api.client,
    team_id=12345
)

if response.status_code == 200:
    # Full type support for the response model
    data: list[PlayerModel] = response.parsed
    print(data[0].firstname)
```

### Advanced: Adding new teams
You can add new teams by modifying `config/teams.yaml`. Somehow there is no API endpoint to fetch all teams, so this is a manual step for now.

### Statistics Center (REST + Websocket)

The package also provides a dedicated wrapper for the Statistics Center API:

```python
from kinexon_handball_api import StatisticsCenterAPI

sc = StatisticsCenterAPI(
  username="<USERNAME>",
  password="<PASSWORD>",
  interfaces_api_url="https://hbl.kinexon.com/statistics-center/interfaces-api",
  outputs_push_url="https://hbl.kinexon.com/statistics-center/outputs-push",
)

# JWT login
jwt = sc.login()

# REST endpoints — all return list[dict]
games = sc.get_games(season="2025_2026")
stats = sc.get_stats("<MATCH_ID>")
events = sc.get_events("<MATCH_ID>")

# Push endpoints
all_endpoints = sc.list_endpoints()

# WebSocket
def on_message(data):
  print("message", data)

def on_error(error):
  print("error", error)

socket_client = sc.connect_websocket(
  on_message=on_message,
  on_error=on_error,
)

sc.subscribe(socket_client, subscription_type="matches", identifier="2019_2020")
sc.subscribe(socket_client, subscription_type="stats", identifier="<MATCH_ID>")
sc.subscribe(
  socket_client,
  subscription_type="events",
  identifier="<MATCH_ID>",
  filter={"event": "shot"},
)
sc.subscribe(socket_client, subscription_type="live_events", identifier="<MATCH_ID>")
```

Supported websocket subscription types are `matches`, `stats`, `events`, and `live_events`.

## Architecture

This project uses a **Wrapper Pattern** around a generated OpenAPI client.

- **`src/kinexon_handball_api/`**: The public-facing code. Contains the `HandballAPI` and `StatisticsCenterAPI` classes, authentication logic, and user-friendly helpers.
- **`src/_vendor/kinexon_client/`**: Generated client for the main Kinexon Cloud REST API (from `openapi/sports_app.json`).
- **`src/_vendor/statistics_center_client/`**: Generated client for the Statistics Center API (from `openapi/statistics_center.json`). Provides typed models (`Games`, `LoginSuccess`) used by `StatisticsCenterAPI`.
  - *Note*: Vendoring the generated clients avoids external dependencies and versioning conflicts.
  - **Do not edit files in `_vendor` manually.** They are overwritten during code generation.

## Repository Layout

- **`src/kinexon_handball_api/`**: Hand-written wrapper and helper APIs.
- **`src/_vendor/kinexon_client/`**: Generated OpenAPI client for main REST API (do not edit).
- **`src/_vendor/statistics_center_client/`**: Generated OpenAPI client for Statistics Center (do not edit).
- **`openapi/`**: OpenAPI specs (`sports_app.json`, `statistics_center.json`) and generator configs.
- **`scripts/`**: Code generation helpers (`codegen.sh`, `rename_operation_ids.py`).
- **`test/`**: Test suite executed with `pytest`.

## AI Assistance

If you are using an AI coding agent (Claude Code, GitHub Copilot, Cursor, etc.) in this repo, see the project-specific guidance in [AGENTS.md](AGENTS.md).

## Development

### Setup

```bash
# Install dependencies including dev tools
uv pip install -e ".[dev]"
```

### Running Tests

```bash
pytest

Note: The integration tests use live API calls and will be skipped if required
environment variables are not set.
```

### Code Generation

If the Kinexon OpenAPI specification changes, you can regenerate the client:

**Windows (PowerShell)**:
```powershell
./scripts/codegen.ps1
```

**Linux / Mac**:
```bash
./scripts/codegen.sh
```

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contributing

Contributions are welcome! Please open issues or pull requests on GitHub.
