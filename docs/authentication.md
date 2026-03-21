# Authentication

## Main API: Two-Step Login

The Kinexon Cloud API uses a non-standard two-step authentication flow. `KinexonAPI.authenticate()` handles this automatically on `connect()`.

### Step 1 — Session-level Basic Auth

An HTTP GET is made to `ENDPOINT_KINEXON_SESSION` with HTTP Basic Auth credentials (`USERNAME_KINEXON_SESSION` / `PASSWORD_KINEXON_SESSION`). This establishes a session cookie on the underlying `httpx.Client`.

```
GET https://hbl-cloud.kinexon.com/
Authorization: Basic <base64(username:password)>
```

Accepted status codes: `200`, `204`, or a redirect. Anything else raises `APIRequestError`.

### Step 2 — JSON Main Login

A POST is made to `ENDPOINT_KINEXON_MAIN` with a JSON body containing the main credentials (`USERNAME_KINEXON_MAIN` / `PASSWORD_KINEXON_MAIN`).

```
POST https://hbl-cloud.kinexon.com/checklogin
Content-Type: application/json

{
  "login": {
    "username": "<main_username>",
    "password": "<main_password>"
  }
}
```

A `200` response completes authentication. The session cookie from Step 1 is retained by the shared `httpx.Client`.

### API Key Injection

All subsequent requests include the `api-key` header, which is injected by the `kinexon_client.Client` constructor:

```python
Client(
    base_url=self.base_url,
    headers={"api-key": self.api_key},
    ...
)
```

The `API_KEY_KINEXON` value is passed directly. The generated client adds this header to every request automatically.

### Required Environment Variables

| Variable | Description |
|---|---|
| `API_KEY_KINEXON` | Static API key for the `api-key` header |
| `USERNAME_KINEXON_SESSION` | Username for Step 1 Basic Auth |
| `PASSWORD_KINEXON_SESSION` | Password for Step 1 Basic Auth |
| `ENDPOINT_KINEXON_SESSION` | URL for Step 1 GET request |
| `USERNAME_KINEXON_MAIN` | Username for Step 2 JSON POST |
| `PASSWORD_KINEXON_MAIN` | Password for Step 2 JSON POST |
| `ENDPOINT_KINEXON_MAIN` | URL for Step 2 POST request |
| `ENDPOINT_KINEXON_API` | Base URL for all API calls (no trailing `/public/v1`) |

Load these from a `.env` file using `python-dotenv`:

```python
from dotenv import load_dotenv
load_dotenv()
```

### Re-authentication

`KinexonAPI` does not automatically re-authenticate on session expiry. If a session expires mid-use, call `api.authenticate()` explicitly to re-run both steps, or create a new `HandballAPI` instance.

---

## Statistics Center API: JWT Login

`StatisticsCenterAPI` uses a separate JWT-based flow against a different service.

### Login

```python
sc = StatisticsCenterAPI(username="<user>", password="<pass>", ...)
jwt = sc.login()
```

This POSTs to `{interfaces_api_url}/auth/login`:

```
POST https://hbl.kinexon.com/statistics-center/interfaces-api/auth/login
Content-Type: application/json

{"name": "<username>", "password": "<password>"}
```

The response JSON is expected to contain a `jwt` key. The token is cached on the instance (`sc._jwt`). Subsequent calls to `login()` return the cached token unless `force_refresh=True` is passed.

### Authenticated Requests

All REST calls to the Statistics Center include the JWT as a Bearer token:

```
Authorization: Bearer <jwt>
Content-Type: application/json
```

### WebSocket Authentication

The WebSocket connection (via `python-socketio`) passes the JWT in the connection headers:

```python
sio_client.connect(
    ws_url,
    headers={"Authorization": f"Bearer {token}"},
    transports=["polling", "websocket"],
)
```
