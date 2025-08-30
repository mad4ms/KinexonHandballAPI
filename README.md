# Kinexon Handball API

A Python wrapper for accessing and processing Kinexon Handball data. This library provides a clean, type-safe interface to interact with the Kinexon API for handball analytics and position data.

## Features

- 🔐 **Secure Authentication**: Dual-layer authentication system with session and main login
- 📊 **Data Export**: Export position data, metrics, and events in various formats
- 🏃 **Team Management**: Access team IDs and session information
- 🛡️ **Error Handling**: Comprehensive error handling with custom exceptions
- ⚡ **Performance**: Built-in retry logic and connection pooling
- 🧪 **Testing**: Full test suite with integration and unit tests
- 📦 **Type Safety**: Full type hints and Pydantic validation

## Installation

### Prerequisites

- Python 3.12 or higher
- `uv` as package manager
- Valid Kinexon API credentials


### Install

```bash
git clone https://github.com/mad4ms/KinexonHandballAPI.git
cd KinexonHandballAPI
uv pip install -e .
```

## Quick Start

### Basic Usage

```python
from kinexon_handball_api.client import KinexonClient
from kinexon_handball_api.config import Settings

# Initialize settings from environment variables
settings = Settings()

# Create client instance
client = KinexonClient(settings)

# Get available teams
# Fetches a hardcoded DEFAULT_TEAM_IDS specified in fetchers.py
teams = client.get_team_ids()
print(f"Available teams: {len(teams)}")

# Get session IDs for a team
sessions = client.get_session_ids(
    team_id=13,  # Füchse Berlin
    start="2025-01-01",
    end="2025-01-31"
)

# Get position data
position_data = client.get_position_data_by_session_id("session_123")
```

### Environment Configuration

Create a `.env` file with your Kinexon credentials:

```env
# Session Authentication
USERNAME_KINEXON_SESSION=your_session_username
PASSWORD_KINEXON_SESSION=your_session_password
ENDPOINT_KINEXON_SESSION=https://api.kinexon.com/session

# Main Authentication
USERNAME_KINEXON_MAIN=your_main_username
PASSWORD_KINEXON_MAIN=your_main_password
ENDPOINT_KINEXON_MAIN=https://api.kinexon.com/login

# API Configuration
ENDPOINT_KINEXON_API=https://api.kinexon.com/api
API_KEY_KINEXON=your_api_key
```

## Team Configuration

Team IDs are stored in `config/teams.yaml` and organized by season. To update team IDs for a new season:

1. Go to Kinexon Cloud web app
2. Click "Team" selection dropdown
3. Click user → profile
4. Switch to "Teams" tab
5. Copy IDs next to team names
6. Update `config/teams.yaml` with new season data

The current season is automatically used, or you can specify a season:
```python
# Get current season teams
teams = client.get_team_ids()

# Get specific season teams
teams_2024 = client.get_team_ids("2024-25")
```
```

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/mad4ms/KinexonHandballAPI.git
cd KinexonHandballAPI

# Install development dependencies
uv pip install -e ".[dev]"

# Install pre-commit hooks (optional but recommended)
uv pip install pre-commit
pre-commit install
```

### Running Tests

```bash
# Unit tests
pytest tests/test_client.py

# Integration tests (requires live API access)
pytest tests/test_integration_*.py -m integration

# All tests
pytest
```

## Examples

###  Workflow

```python
import os
from datetime import datetime, timedelta
from kinexon_handball_api.client import KinexonClient
from kinexon_handball_api.config import Settings

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize client
settings = Settings()
client = KinexonClient(settings)

# Get all teams (current season)
teams = client.get_team_ids()
print(f"Found {len(teams)} teams")

# Get teams for specific season
teams_2024 = client.get_team_ids("2024-25")
print(f"Found {len(teams_2024)} teams in 2024-25 season")

# Get sessions for a specific team
team_id = 13  # Füchse Berlin

# Fetch any games of the last 30 days
end_date = datetime.now()
start_date = end_date - timedelta(days=30)

# Fetch session ids of the last 30 days
sessions = client.get_session_ids(
    team_id=team_id,
    start=start_date.strftime("%Y-%m-%d"),
    end=end_date.strftime("%Y-%m-%d")
)

print(f"Found {len(sessions)} sessions for team {team_id}")

# Get position data for each session
for session in sessions:
    session_id = session["session_id"]
    description = session["description"]
    
    print(f"Getting position data for session: {description} ({session_id})")
    
    # Mind that the download can take ages, as a file is usually around 150 MB.
    # @Kinexon: 160MB in 7min = terrible
    # Probably using RDBMS for time-series data?
    # Time-series DB (or even PG timescaledb) + compression + proper indexes + streaming
    # Kinda using a screwdriver to hammer nails
    try:
        position_data = client.get_position_data_by_session_id(
            session_id=session_id,
        )
        
        # Save to file
        filename = f"positions_{session_id}.csv"
        with open(filename, "wb") as f:
            f.write(position_data)
        
        print(f"Saved {filename}")
        
    except Exception as e:
        print(f"Failed to get position data for session {session_id}: {e}")
```


## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines (enforced by flake8)
- Use Black for code formatting (88 character line length)
- Sort imports with isort (Black-compatible profile)
- Add type hints to all functions (enforced by mypy)
- Write tests for new functionality
- Update documentation for API changes
- Use conventional commit messages

### Pre-commit Hooks

The project includes pre-commit hooks that automatically run code quality checks:

```bash
# Install pre-commit hooks
uv pip install pre-commit
pre-commit install

# Run manually (optional)
pre-commit run --all-files
```

This ensures all code meets quality standards before commits.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support and questions:

- Create an issue on GitHub
- Review the test examples for usage patterns

## Changelog

### v0.1.0
- Initial release
- Basic API client functionality
- Authentication system
- Position data retrieval with progress tracking
- Team and session management
- Comprehensive test suite
- Improved error handling for large CSV downloads

## Acknowledgments

- Kinexon for providing the handball analytics API