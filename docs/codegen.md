# Client Code Generation

## Overview

The generated client in `src/_vendor/kinexon_client/` is produced by [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client) from the Kinexon OpenAPI specification.

**Do not edit files in `src/_vendor/` manually.** They will be overwritten the next time codegen runs.

## When to Regenerate

Regenerate the client when:

- Kinexon updates their API specification (new endpoints, changed models, deprecated routes).
- You need access to an endpoint that does not yet exist in the generated modules under `src/_vendor/kinexon_client/api/`.

## Running Codegen

### Linux / Mac

```bash
./scripts/codegen.sh
```

### Windows (PowerShell)

```powershell
./scripts/codegen.ps1
```

Both scripts:

1. Download the latest OpenAPI spec from the Kinexon API and save it to `openapi/sports_app.json`.
2. Delete the existing `src/_vendor/kinexon_client/` directory.
3. Run `openapi-python-client generate` to produce a fresh client.
4. Move the generated output into `src/_vendor/kinexon_client/`.

## Output Structure

After generation, `src/_vendor/kinexon_client/` contains:

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
├── models/                       # Pydantic v2 models (request/response types)
├── client.py                     # Client base class
├── errors.py                     # UnexpectedStatus and related errors
└── __init__.py
```

Each endpoint module exposes `sync`, `sync_detailed`, `asyncio`, and `asyncio_detailed`. The wrapper always uses `sync_detailed`.

## After Regeneration

1. Review the diff in `src/_vendor/` for any breaking changes (removed endpoints, renamed parameters, changed model fields).
2. Update any wrapper methods in `src/kinexon_handball_api/handball.py` that reference renamed or removed generated functions.
3. Run the full check suite to catch type errors and broken imports:

```bash
uv run ruff check src test
uv run mypy src/kinexon_handball_api
uv run pytest
```

## Linting Exclusions

`pyproject.toml` excludes the generated client from both Ruff and mypy:

```toml
# ruff
extend-exclude = ["src/_vendor/kinexon_client"]

# mypy
[[tool.mypy.overrides]]
module = "kinexon_client.*"
follow_imports = "skip"
ignore_errors = true
```

Do not remove these exclusions. The generated code does not conform to the project's lint rules and is not expected to.
