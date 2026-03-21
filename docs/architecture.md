# Architecture

## Overview

This project uses a **Wrapper Pattern** around an auto-generated OpenAPI client.

```
User Code
    │
    ▼
HandballAPI / StatisticsCenterAPI        ← hand-written (src/kinexon_handball_api/)
    │
    ▼
kinexon_client (generated)               ← auto-generated (src/_vendor/kinexon_client/)
    │
    ▼
Kinexon REST API
```

There are two distinct public interfaces:

1. **`HandballAPI`** — typed wrapper for the main Kinexon Cloud REST endpoints (sessions, players, events, exports, statistics).
2. **`StatisticsCenterAPI`** — separate client for the Statistics Center, which uses a different auth scheme (JWT) and also exposes a WebSocket interface (via `python-socketio`).

## Source Layout

```
src/
├── kinexon_handball_api/          # hand-written wrapper (public package)
│   ├── __init__.py                # re-exports HandballAPI, StatisticsCenterAPI
│   ├── api.py                     # KinexonAPI base class (auth + httpx client)
│   ├── handball.py                # HandballAPI (inherits KinexonAPI)
│   ├── fetchers.py                # team ID loading from config/teams.yaml
│   ├── statistics_center.py       # StatisticsCenterAPI (JWT + WebSocket)
│   └── config/
│       └── teams.yaml             # team IDs keyed by season
└── _vendor/
    └── kinexon_client/            # generated OpenAPI client (do not edit)
        ├── api/                   # one module per API endpoint group
        │   ├── events/
        │   ├── exports/
        │   ├── players/
        │   ├── sessions_and_phases/
        │   ├── statistics/
        │   ├── categories_and_thresholds/
        │   └── available_metrics_and_events/
        ├── models/                # Pydantic v2 models for all request/response types
        ├── client.py              # Client / AuthenticatedClient base classes
        └── errors.py              # generated error types
```

The `pyproject.toml` build configuration points `setuptools` at both `src/` and `src/_vendor/` so both `kinexon_handball_api` and `kinexon_client` are installable from a single package.

## Class Hierarchy

```
KinexonAPI          (src/kinexon_handball_api/api.py)
    └── HandballAPI (src/kinexon_handball_api/handball.py)

StatisticsCenterAPI (src/kinexon_handball_api/statistics_center.py)  [independent]
```

### `KinexonAPI`

Base class responsible for:

- Storing credentials and configuration.
- Creating the `kinexon_client.Client` instance with the `api-key` header pre-injected.
- Executing the two-step authentication on `connect()` (called automatically on init).
- Providing `make_custom_request()` for low-level streaming or non-standard requests.
- Context manager support (`__enter__` / `__exit__` → `close()`).

### `HandballAPI`

Inherits `KinexonAPI`. Adds:

- `get_team_ids(season)` — loads team list from `config/teams.yaml` via `fetchers.py`.
- `get_sessions_for_team(team_id, start, end)` — sessions in a date range.
- `get_team_players(team_id)` — roster for a team.
- `get_events_for_session(event_type, players, session_id)` — event data for a session.
- `get_available_metrics_and_events()` — list of all metrics/events the API supports.
- `get_positions_csv(session_id, ...)` — position export as CSV string via generated client.
- `download_positions_csv_via_custom(session_id, ...)` — streaming download with `tqdm` progress bar and optional byte limit.

### `StatisticsCenterAPI`

Standalone client (does not inherit `KinexonAPI`). Uses:

- `httpx.Client` for REST calls.
- JWT authentication via `/auth/login`.
- `python-socketio` for WebSocket subscriptions (lazy-imported so the dependency is optional at import time).

## Generated Client

The generated client in `src/_vendor/kinexon_client/` is produced by [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client) from the Kinexon OpenAPI specification (`openapi/sports_app.json`).

Each endpoint is a module with two callable functions:

- `sync(...)` — returns parsed response body or `None`.
- `sync_detailed(...)` — returns a `Response[T]` object with `.status_code`, `.content`, `.headers`, and `.parsed`.

The wrapper layer always uses `sync_detailed` so it can inspect the status code before returning data.

## Configuration: Team IDs

Team IDs are not available via the API. They must be obtained manually from the Kinexon Cloud web UI (user profile → Teams tab) and stored in `src/kinexon_handball_api/config/teams.yaml`:

```yaml
current_season: "2025-26"
seasons:
  "2025-26":
    - id: 12345
      name: "Team Name"
```

`fetchers.py` reads this file (with `lru_cache`) and validates the structure.

## Design Decisions

- **Vendored generated client**: Shipping `kinexon_client` inside `src/_vendor/` avoids versioning conflicts and makes the package self-contained. The tradeoff is that the `_vendor` directory must be kept in sync with the API spec via `scripts/codegen.sh`.
- **`sync_detailed` over `sync`**: Using the detailed variant in the wrapper gives access to HTTP status codes, enabling meaningful error messages instead of silent `None` returns.
- **Two auth systems**: The main REST API uses a two-step session/cookie + JSON login. The Statistics Center uses a separate JWT flow. These are intentionally kept as separate classes.
- **Streaming via `make_custom_request`**: The generated client buffers full responses. For large position exports, `download_positions_csv_via_custom` bypasses the generated client and streams via `httpx` with chunk-based iteration.
