# Architecture

## Overview

This project uses a **Wrapper Pattern** around an auto-generated OpenAPI client.

```
User Code
    │
    ├──► HandballAPI                      ← hand-written (src/kinexon_handball_api/)
    │        │
    │        ▼
    │    kinexon_client (generated)       ← auto-generated (src/_vendor/kinexon_client/)
    │        │
    │        ▼
    │    Kinexon Cloud REST API
    │
    └──► StatisticsCenterAPI             ← hand-written (src/kinexon_handball_api/)
             │
             ▼
         statistics_center_client        ← auto-generated (src/_vendor/statistics_center_client/)
         (models: Games, LoginSuccess)
             │
             ▼
         Statistics Center REST + WS API
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
    ├── kinexon_client/            # generated from openapi/sports_app.json (do not edit)
    │   ├── api/                   # one module per API endpoint group
    │   │   ├── events/
    │   │   ├── exports/
    │   │   ├── players/
    │   │   ├── sessions_and_phases/
    │   │   ├── statistics/
    │   │   ├── categories_and_thresholds/
    │   │   └── available_metrics_and_events/
    │   ├── models/                # attrs models for all request/response types
    │   ├── client.py              # Client / AuthenticatedClient base classes
    │   └── errors.py
    └── statistics_center_client/  # generated from openapi/statistics_center.json (do not edit)
        ├── api/
        │   ├── games/             # GET /games
        │   ├── login/             # POST /auth/login
        │   └── stats/             # GET /stats/{matchId}, GET /events/{matchId}
        ├── models/                # Login, LoginSuccess, Games, Statistics
        ├── client.py
        └── errors.py
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
- JWT authentication via `/auth/login`. The login response is parsed into a `LoginSuccess` model from `statistics_center_client.models`.
- `get_games()`, `get_games_via_websocket()`, `get_stats()`, and `get_events()` all return `list[dict[str, Any]]` — the Statistics Center spec only documents 3 fields for games (`match_id`, `home_team`, `away_team`) while the real API returns many more; a generated model would bury the extra fields in `additional_properties` without `.get()` support, so plain dicts are used.
- `python-socketio` for WebSocket subscriptions (lazy-imported so the dependency is optional at import time).

## Generated Clients

There are two generated clients, both produced by [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client) via `scripts/codegen.sh`:

| Client | Spec | Package |
|---|---|---|
| `kinexon_client` | `openapi/sports_app.json` | `src/_vendor/kinexon_client/` |
| `statistics_center_client` | `openapi/statistics_center.json` | `src/_vendor/statistics_center_client/` |

The `sports_app.json` spec uses hash-based `operationId` values. `scripts/rename_operation_ids.py` replaces them with readable path-derived names before generation. The `statistics_center.json` spec has self-referential `allOf` schemas which are flattened by a pre-processing step in `codegen.sh`.

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
