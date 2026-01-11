# Kinexon Handball API


[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

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

### Standard Installation
Clone the repository and install using pip:

```bash
git clone https://github.com/mad4ms/KinexonHandballAPI.git
cd KinexonHandballAPI
pip install .
```

### Using uv (Recommended)
If you use [uv](https://github.com/astral-sh/uv) for fast package management:

```bash
git clone https://github.com/mad4ms/KinexonHandballAPI.git
cd KinexonHandballAPI
uv pip install .
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

# API Base Configuration
ENDPOINT_KINEXON_API=https://hbl-cloud.kinexon.com/public/v1/
```

yeah i know it's confusing, but the two-step authentication requires separate credentials for each step. Don't shoot the messenger!

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
    base_url=os.getenv("ENDPOINT_KINEXON_API"),
    api_key=os.getenv("API_KEY_KINEXON"),
    username_basic=os.getenv("USERNAME_KINEXON_SESSION"),
    password_basic=os.getenv("PASSWORD_KINEXON_SESSION"),
    username_main=os.getenv("USERNAME_KINEXON_MAIN"),
    password_main=os.getenv("PASSWORD_KINEXON_MAIN"),
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
from kinexon_client.api.players import get_team_players
from kinexon_client.models import PlayerModel

# You can access the authenticated low-level client via `api.client`
response = get_team_players.sync_detailed(
    client=api.client,
    team_id=12345
)

if response.status_code == 200:
    # Full type support for the response model
    data: list[PlayerModel] = response.parsed
    print(data[0].firstname)
```

### Advanced: Adding new teams
You can add new teams by modifying the `config/teams.json`. Somehow there is no API endpoint to fetch all teams, so this is a manual step for now.

## Architecture

This project uses a **Wrapper Pattern** around a generated OpenAPI client.

- **`src/kinexon_handball_api/`**: The public-facing code. Contains the `HandballAPI` class, authentication logic, and user-friendly helpers.
- **`src/_vendor/kinexon_client/`**: The low-level client code generated from the Kinexon OpenAPI specification.
  - *Note*: This directory allows us to ship the generated code without external dependencies or versioning conflicts.
  - **Do not edit files in `_vendor` manually.** They are overwritten during code generation.

## Development

### Setup

```bash
# Install dependencies including dev tools
uv pip install -e ".[dev]"
```

### Running Tests

```bash
# Run unit tests
uv run pytest -m "not integration"
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
