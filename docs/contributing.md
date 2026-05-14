# Contributing

## Setup

```bash
git clone https://github.com/mad4ms/KinexonHandballAPI.git
cd KinexonHandballAPI

# Install with dev extras
uv pip install -e ".[dev]"

# Install pre-commit hooks
uv run pre-commit install
```

## Running Checks

```bash
# Lint
uv run ruff check src test

# Format check
uv run ruff format --check src test

# Type check (wrapper only; generated client is excluded)
uv run mypy src/kinexon_handball_api

# Tests (unit only, no API credentials needed)
uv run pytest

# Tests including integration (requires .env with live credentials)
uv run pytest -m "integration"
```

CI runs all three (`ruff`, `mypy`, `pytest`) against Python 3.12 and 3.13 on every push/PR to `main`. The build also verifies the package builds cleanly with `uv build`.

## Adding a New Endpoint Wrapper

1. Find the generated function in `src/_vendor/kinexon_client/api/<group>/`.
   - Group names map to API tag names (e.g., `events`, `players`, `exports`).
   - Function names are verbose: `get_public_v1_teams_by_team_id_players`.
2. Add a method to `HandballAPI` in [src/kinexon_handball_api/handball.py](../src/kinexon_handball_api/handball.py).
3. Use `sync_detailed` and `_handle_response` for consistent error handling:

```python
from kinexon_client.api.some_group import some_generated_function

def get_something(self, param: str) -> Any:
    self._require_value("param", param)
    resp = some_generated_function.sync_detailed(
        client=self.client,
        arg=param,
    )
    return self._handle_response(resp, "get_something", default={})
```

4. Add a unit test in `test/`.

## Adding Team IDs for a New Season

Team IDs are not available via the API. Obtain them from the Kinexon Cloud UI:

1. Log in to the Kinexon Cloud web app.
2. Go to user profile → Teams tab.
3. Note the numeric IDs next to each team name.
4. Add an entry to `src/kinexon_handball_api/config/teams.yaml`:

```yaml
current_season: "2026-27"
seasons:
  "2026-27":
    - id: 99999
      name: "New Team Name"
```

## Code Style

- **Formatter / linter**: Ruff (configured in `pyproject.toml`). Line length 88, target Python 3.12.
- **Type hints**: Required on all new hand-written code. `mypy` runs in strict mode on `src/kinexon_handball_api/`.
- **`src/_vendor/`**: Excluded from all linting and type checking. Never edit manually.

## Pull Requests

- Branch from `main`.
- Keep PRs focused. Separate feature/fix PRs from refactors.
- Ensure all CI checks pass before requesting review.
- Update [docs/api-reference.md](api-reference.md) if you add or change public methods.

## Releases

Releases are automated via the `.github/workflows/release.yml` workflow. Bump the version in `pyproject.toml` and tag the commit; the workflow handles the rest.
