# Client Code Generation

## Overview

Two generated clients live under `src/_vendor/`, both produced by [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client):

| Client | Spec | Output |
|---|---|---|
| `kinexon_client` | `openapi/sports_app.json` | `src/_vendor/kinexon_client/` |
| `statistics_center_client` | `openapi/statistics_center.json` | `src/_vendor/statistics_center_client/` |

**Do not edit files in `src/_vendor/` manually.** They will be overwritten the next time codegen runs.

## When to Regenerate

Regenerate when:

- Kinexon updates their API specification (new endpoints, changed models, deprecated routes).
- You need access to an endpoint not yet in the generated modules.
- The `openapi/sports_app_new.json` or `openapi/statistics_center.json` file has been updated with a fresh spec.

## Running Codegen

### Linux / Mac

```bash
./scripts/codegen.sh
```

### Windows (PowerShell)

```powershell
./scripts/codegen.ps1
```

> **Note:** Both scripts attempt to download the specs via `curl`. The API-doc endpoints require authentication, so if the download fails (401), replace `openapi/sports_app.json` and/or `openapi/statistics_center.json` manually, then re-run the script — it will skip the download and use the local files.

## What the Script Does

### sports_app client

1. Downloads `openapi/sports_app.json` from the live API.
2. Runs `scripts/rename_operation_ids.py` — replaces hash-based `operationId` values (e.g. `d54d2f11c25c...`) with readable path-derived names (e.g. `GetPublicV1StatisticsList`). This is required because `openapi-python-client` uses the `operationId` directly as the module filename.
3. Runs `openapi-python-client generate` with `openapi/config.yaml`.
4. Moves output to `src/_vendor/kinexon_client/`.

### statistics_center client

1. Downloads `openapi/statistics_center.json` from the live API.
2. Strips non-HTTP paths (the spec includes a `ws://` documentation entry that is not a real REST endpoint).
3. Flattens self-referential `allOf` schemas (a known bug in the upstream spec where each schema references itself in `allOf`).
4. Runs `openapi-python-client generate` with `openapi/statistics_center_config.yaml`.
5. Moves output to `src/_vendor/statistics_center_client/`.

## Output Structure

### kinexon_client

```
kinexon_client/
├── api/                          # one sub-package per API tag
│   ├── events/
│   ├── exports/
│   ├── players/
│   ├── sessions_and_phases/
│   ├── statistics/
│   ├── categories_and_thresholds/
│   └── available_metrics_and_events/
├── models/                       # attrs models (request/response types)
├── client.py                     # Client / AuthenticatedClient base classes
├── errors.py
└── __init__.py
```

### statistics_center_client

```
statistics_center_client/
├── api/
│   ├── games/                    # GET /games
│   ├── login/                    # POST /auth/login
│   └── stats/                    # GET /stats/{matchId}, GET /events/{matchId}
├── models/                       # Login, LoginSuccess, Games, Statistics
├── client.py
├── errors.py
└── __init__.py
```

Each endpoint module exposes `sync`, `sync_detailed`, `asyncio`, and `asyncio_detailed`. The wrapper always uses `sync_detailed`.

## Adding a New operationId Mapping

If Kinexon adds new endpoints with hash-based `operationId`s and codegen produces unreadable module names, add an entry to `scripts/rename_operation_ids.py`:

```python
OPID_MAP = {
    # existing entries ...
    "abcdef1234567890": "GetPublicV1MyNewEndpoint",
}
```

## After Regeneration

1. Review the diff in `src/_vendor/` for breaking changes (removed endpoints, renamed parameters, changed model fields).
2. Update wrapper methods in `src/kinexon_handball_api/handball.py` or `statistics_center.py` that reference renamed/removed functions.
3. Run the full check suite:

```bash
uv run ruff check src test
uv run mypy src/kinexon_handball_api
uv run pytest
```

## Linting Exclusions

`pyproject.toml` excludes both generated clients from Ruff and mypy:

```toml
# ruff
extend-exclude = [
    "src/_vendor/kinexon_client",
    "src/_vendor/statistics_center_client",
]

# mypy
[[tool.mypy.overrides]]
module = ["kinexon_client.*", "statistics_center_client.*"]
follow_imports = "skip"
ignore_errors = true
```

Do not remove these exclusions. The generated code does not conform to the project's lint rules and is not expected to.
