"""Kinexon API client wrapper with two-step authentication."""

import logging
from types import TracebackType
from typing import Any

import httpx
from kinexon_client import Client


class APIRequestError(Exception):
    """Exception raised for request errors."""


class KinexonAPI:
    """
    API-key authenticated wrapper for Kinexon API.
    Provides low-level setup for generated kinexon_client.* functions.
    """

    def __init__(  # noqa: PLR0913
        self,
        base_url: str,
        username_basic: str,
        password_basic: str,
        username_main: str,
        password_main: str,
        endpoint_session: str,
        endpoint_main: str,
        api_key: str,
        timeout: float = 10.0,
        verify_ssl: bool = True,
        connect_on_init: bool = True,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout
        self.verify_ssl = verify_ssl

        self.username_basic = username_basic
        self.password_basic = password_basic
        self.username_main = username_main
        self.password_main = password_main
        self.endpoint_session = endpoint_session
        self.endpoint_main = endpoint_main

        self.client: Client | None = None
        if connect_on_init:
            self.connect()

        # Use AuthenticatedClient (generated client requires it)
        # Note: We bypass Authorization headers;
        # API key is injected via query by generated funcs.

    def connect(self) -> None:
        self.client = Client(
            base_url=self.base_url,
            # token="",  # not used
            # prefix="",
            # auth_header_name=None,
            headers={"api-key": self.api_key},
            timeout=httpx.Timeout(self.timeout),
            verify_ssl=self.verify_ssl,
            raise_on_unexpected_status=True,
        )

        self.authenticate()

    def _get_httpx_client(self) -> httpx.Client:
        if self.client is None:
            raise APIRequestError("Client not initialized. Call connect() first.")
        return self.client.get_httpx_client()

    def authenticate(self) -> bool:
        """
        Authenticate with Kinexon API using a two-step login:
        1) Persist Basic Auth on the session and GET the session endpoint.
        2) POST JSON (nested 'login') to the main endpoint.
        """
        logger = logging.getLogger(__name__)
        ok_status = 200

        # Use a temporary httpx.Client for authentication
        client = self._get_httpx_client()
        client.auth = httpx.BasicAuth(
            self.username_basic,
            self.password_basic,
        )
        # Step 1: Session-level Basic Auth
        resp = client.get(
            self.endpoint_session,
            # auth=(self.username_basic, self.password_basic),
        )
        if resp.status_code not in {200, 204} and not resp.is_redirect:
            raise APIRequestError(
                f"Session login failed: {resp.status_code} {resp.text}"
            )
        logger.info("Session-level authentication successful.")

        # Step 2: Main login
        payload = {
            "login": {
                "username": self.username_main,
                "password": self.password_main,
            }
        }
        resp = client.post(self.endpoint_main, json=payload)
        if resp.status_code != ok_status:
            raise APIRequestError(f"Main login failed: {resp.status_code} {resp.text}")
        logger.info("Main authentication successful.")

        return True

    def close(self) -> None:
        if self.client is None:
            return
        self.client.get_httpx_client().close()

    def __enter__(self) -> "KinexonAPI":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        self.close()

    def make_custom_request(  # noqa: PLR0913
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        data: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        stream: bool = False,
        timeout: float | None = None,
    ) -> httpx.Response:
        """
        Low-level custom request via the authenticated httpx.Client.
        If stream=True, returns an open Response with streaming enabled.
        Caller is responsible for closing the response (resp.close()).
        """
        client = self._get_httpx_client()

        # Prepend base URL if relative
        if not (url.startswith("http://") or url.startswith("https://")):
            url = f"{self.base_url.rstrip('/')}/{url.lstrip('/')}"

        req = client.build_request(
            method=method,
            url=url,
            params=params,
            headers=headers,
            data=data,
            json=json,
            timeout=timeout or self.timeout,
        )

        # stream=True -> no context manager here; caller must close resp
        resp = client.send(req, stream=stream)
        # For non-streaming, raise immediately so caller gets a ready-to-use object
        if not stream:
            resp.raise_for_status()
        return resp
