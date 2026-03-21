# Kinexon Handball API - AI Agent Instructions

## Project Overview

Python wrapper for the Kinexon Handball API. Provides a user-friendly abstraction over a raw, auto-generated OpenAPI client.

## Architectural Structure

- **Wrapper Core (`src/kinexon_handball_api/`)**: Hand-written logic, authentication, and high-level helpers. New features go here.
  - `api.py`: Two-step authentication and `httpx` client initialization.
  - `handball.py`: Main entry point (`HandballAPI`). Convenience methods for common API operations.
  - `fetchers.py`: Static data loading (e.g., team IDs from `config/teams.yaml`).
  - `statistics_center.py`: Separate wrapper for the Statistics Center REST + WebSocket API.
- **Generated Client (`src/_vendor/kinexon_client/`)**: Auto-generated OpenAPI client via `openapi-python-client`.
  - **CRITICAL: Do NOT edit files in `src/_vendor/` manually.** They are overwritten by `scripts/codegen.sh`.
  - If the API spec changes, regenerate using `scripts/codegen.sh` (Linux/Mac) or `scripts/codegen.ps1` (Windows).

See [docs/architecture.md](docs/architecture.md) for the full architectural breakdown.

## Development Workflows

### Adding New API Features

1. Check `src/_vendor/kinexon_client/api/` for an existing generated endpoint. Names are verbose (e.g., `get_public_v_1_events...`).
2. Add a method to `HandballAPI` in `src/kinexon_handball_api/handball.py`.
3. Use the `sync_detailed` method of the generated function to access status codes and parsed data.

```python
from kinexon_client.api.some_module import some_generated_function

def my_wrapper_method(self, param):
    resp = some_generated_function.sync_detailed(client=self.client, arg=param)
    if resp.status_code != 200:
        raise RuntimeError(f"Error: {resp.content}")
    return resp.parsed
```

See [docs/api-reference.md](docs/api-reference.md) for all available wrapper methods.

### Updating the Generated Client

If the upstream OpenAPI spec changes:

```bash
./scripts/codegen.sh         # Linux/Mac
./scripts/codegen.ps1        # Windows PowerShell
```

This downloads the latest spec to `openapi/sports_app.json` and regenerates `src/_vendor/kinexon_client/`.

See [docs/codegen.md](docs/codegen.md) for details.

### Dependencies

Use `uv` for package management.

```bash
uv pip install -e ".[dev]"   # editable install with dev extras
uv run pytest                # run tests
uv run ruff check src test   # lint
uv run mypy src/kinexon_handball_api  # type-check
```

## Conventions & Patterns

- **Authentication**: `KinexonAPI` handles the two-step auth automatically. Do not pass generic auth headers manually; the client injects the `api-key`.
- **Imports**: Import generated classes/functions from `kinexon_client.*`. The build system treats `src/_vendor` as a package source.
- **Type Hints**: Use standard Python typing (`list`, `dict`, `Optional`) and Pydantic models from `kinexon_client.models`.
- **Config**: Keep configuration (team IDs, seasons) in `config/teams.yaml` via `fetchers.py`. Do not hardcode in logic.
- **Linting**: Ruff (line length 88, target py312). The `src/_vendor/` directory is excluded from all linting.
- **Tests**: `pytest`. Integration tests require a live API and are skipped without credentials (`@pytest.mark.integration`).

## Key Files

| File | Purpose |
|---|---|
| `src/kinexon_handball_api/handball.py` | Main public API class (`HandballAPI`) |
| `src/kinexon_handball_api/api.py` | Auth base class (`KinexonAPI`) |
| `src/kinexon_handball_api/fetchers.py` | Team ID loading from YAML config |
| `src/kinexon_handball_api/statistics_center.py` | Statistics Center API client |
| `src/_vendor/kinexon_client/` | Generated OpenAPI client (do not edit) |
| `config/teams.yaml` | Team IDs and season configuration |
| `scripts/codegen.sh` | Client regeneration script |
| `pyproject.toml` | Project metadata, dependencies, tool config |

## Further Reading

- [docs/architecture.md](docs/architecture.md) - Full architectural overview and design decisions
- [docs/authentication.md](docs/authentication.md) - Two-step authentication deep dive
- [docs/api-reference.md](docs/api-reference.md) - All wrapper methods and usage examples
- [docs/codegen.md](docs/codegen.md) - How to regenerate the OpenAPI client
- [docs/contributing.md](docs/contributing.md) - Development setup and contribution guidelines
