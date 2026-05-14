# API Reference

## `HandballAPI`

`HandballAPI` is the main entry point. It inherits from `KinexonAPI` (which handles authentication and the underlying `httpx` client).

### Construction

```python
from kinexon_handball_api.handball import HandballAPI

api = HandballAPI(
    base_url="https://hbl-cloud.kinexon.com",
    api_key="<API_KEY_KINEXON>",
    username_basic="<USERNAME_KINEXON_SESSION>",
    password_basic="<PASSWORD_KINEXON_SESSION>",
    username_main="<USERNAME_KINEXON_MAIN>",
    password_main="<PASSWORD_KINEXON_MAIN>",
    endpoint_session="https://hbl-cloud.kinexon.com/",
    endpoint_main="https://hbl-cloud.kinexon.com/checklogin",
    timeout=10.0,           # optional, default 10.0
    verify_ssl=True,        # optional, default True
    connect_on_init=True,   # optional, default True (authenticates immediately)
)
```

Use as a context manager to ensure the HTTP client is closed:

```python
with HandballAPI(...) as api:
    players = api.get_team_players(team_id=12345)
```

---

### `get_team_ids(season=None)`

Returns team IDs from `config/teams.yaml`.

```python
teams = api.get_team_ids()          # uses current_season from config
teams = api.get_team_ids("2024-25") # specific season
# [{"id": 12345, "name": "Team Name"}, ...]
```

Also available as a standalone function:

```python
from kinexon_handball_api.fetchers import fetch_team_ids, get_available_seasons, get_current_season

teams = fetch_team_ids("2025-26")
seasons = get_available_seasons()   # ["2024-25", "2025-26"]
current = get_current_season()      # "2025-26"
```

---

### `get_sessions_for_team(team_id, start, end)`

Returns sessions and phases for a team within a date range.

```python
from datetime import datetime

sessions = api.get_sessions_for_team(
    team_id=12345,
    start=datetime(2025, 9, 1),
    end=datetime(2025, 12, 31),
)

# Accepts ISO strings too:
sessions = api.get_sessions_for_team(12345, "2025-09-01", "2025-12-31")
```

---

### `get_team_players(team_id)`

Returns the current roster for a team.

```python
players = api.get_team_players(team_id=12345)
```

---

### `get_events_for_session(event_type, players, session_id)`

Returns event data for a session.

```python
events = api.get_events_for_session(
    event_type="detected_shot_handball",  # default
    players="in-entity",                  # default
    session_id="<session_uuid>",
)
```

Common `event_type` values: `detected_shot_handball`, `acceleration`, `jump`, `change_of_direction`.

---

### `get_available_metrics_and_events()`

Returns all metric and event types the API supports.

```python
metrics = api.get_available_metrics_and_events()
```

---

### `get_positions_csv(session_id, update_rate, group_by_ts, players)`

Returns position data as a CSV string (buffered in memory).

```python
csv_str = api.get_positions_csv(
    session_id="<session_uuid>",
    update_rate=20,       # Hz, default 20
    group_by_ts=True,     # default True
    players=None,         # filter by player IDs (comma-separated string), default all
)
```

---

### `download_positions_csv_via_custom(session_id, ...)`

Downloads position data via streaming. Suitable for large sessions. Returns `bytes`.

```python
data = api.download_positions_csv_via_custom(
    session_id="<session_uuid>",
    update_rate=20,
    compress_output=False,
    use_local_frame_imu=False,
    center_origin=False,
    group_by_timestamp=False,
    players=None,
    max_bytes=None,       # stop after N bytes (useful for sampling)
    chunk_size=1048576,   # 1 MB chunks, default
    show_progress=True,   # tqdm progress bar, default True
    timeout=None,         # override instance timeout
)
```

---

### `make_custom_request(method, url, ...)` (inherited from `KinexonAPI`)

Low-level access to the authenticated `httpx.Client`. Use this for any endpoint not covered by the helpers above.

```python
resp = api.make_custom_request(
    "GET",
    "/public/v1/some/endpoint",
    params={"key": "value"},
    headers={"Accept": "application/json"},
    stream=False,
)
# resp is an httpx.Response — already raise_for_status()'d for non-streaming calls
data = resp.json()
```

If `stream=True`, the caller is responsible for closing the response:

```python
resp = api.make_custom_request("GET", "/...", stream=True)
try:
    for chunk in resp.iter_bytes():
        ...
finally:
    resp.close()
```

---

## `StatisticsCenterAPI`

Separate client for the Kinexon Statistics Center service.

### Construction

```python
from kinexon_handball_api import StatisticsCenterAPI

sc = StatisticsCenterAPI(
    username="<username>",
    password="<password>",
    interfaces_api_url="https://hbl.kinexon.com/statistics-center/interfaces-api",
    outputs_push_url="https://hbl.kinexon.com/statistics-center/outputs-push",
    timeout=10.0,
    verify_ssl=True,
)
```

### `login(force_refresh=False)`

Authenticates and returns the JWT. Cached on the instance after first call. The response is parsed via the generated `LoginSuccess` model.

```python
jwt = sc.login()
```

### `get_games(season="")`

Returns all matches for the given season. Returns `list[Games]` (from `statistics_center_client.models`).

```python
from statistics_center_client.models import Games

games: list[Games] = sc.get_games(season="2025_2026")
for g in games:
    print(g.match_id, g.home_team, g.away_team)
    # extra fields from the API are in g.additional_properties
```

### `get_stats(match_id)`

Returns player statistics for a match from `/stats/{match_id}`. Returns `list[dict[str, Any]]` (the Statistics Center spec has no field-level schema for stats responses).

```python
stats = sc.get_stats("123456")
```

### `get_events(match_id, event_type="")`

Returns events for a match from `/events/{match_id}`. Returns `list[dict[str, Any]]`.

```python
events = sc.get_events("123456", event_type="shot")
```

### `get_games_via_websocket(season, timeout_s=10.0)`

Discovers matches for a season via the WebSocket matches stream. Returns `list[Games]`.

```python
games: list[Games] = sc.get_games_via_websocket("2025_2026")
```

### `list_endpoints(jwt=None)`

Returns all configured push endpoints.

```python
endpoints = sc.list_endpoints()
```

### `connect_websocket(...)`

Creates and connects a `python-socketio` client.

```python
def on_message(data):
    print("Received:", data)

def on_error(err):
    print("Error:", err)

sio = sc.connect_websocket(
    on_message=on_message,
    on_error=on_error,
    on_connect=lambda: print("Connected"),
    transports=["polling", "websocket"],  # default
)
```

### `subscribe(websocket_client, subscription_type, identifier, ...)`

Sends a subscription message over an active WebSocket connection.

```python
sc.subscribe(sio, subscription_type="matches", identifier="2025_26")
sc.subscribe(sio, subscription_type="stats", identifier="<match_id>")
sc.subscribe(sio, subscription_type="events", identifier="<match_id>", filter={"event": "shot"})
sc.subscribe(sio, subscription_type="live_events", identifier="<match_id>")
```

Supported `subscription_type` values: `matches`, `stats`, `events`, `live_events`.

---

## Using the Raw Generated Client

For endpoints not wrapped by `HandballAPI`, the generated client is directly accessible:

```python
from kinexon_client.api.statistics import get_public_v1_statistics_by_type_by_player_id_by_time_entity_range_type

resp = get_public_v1_statistics_by_type_by_player_id_by_time_entity_range_type.sync_detailed(
    client=api.client,
    statistic_type="speed_max",
    player_id="<player_id>",
    time_entity_range_type="session",
    # ... other params
)

if resp.status_code == 200:
    data = resp.parsed
```

All generated modules are under `src/_vendor/kinexon_client/api/`. See that directory for the full list of available endpoints.
