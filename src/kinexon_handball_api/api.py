"""
Kinexon  API Client
API-key authenticated wrapper, integrating with generated kinexon_client functions.

Author: Michael Adams, 2025
"""

import logging

import httpx
from kinexon_client import Client
from requests.auth import HTTPBasicAuth

from typing import Any, Dict, Optional, List


class APIRequestError(Exception):
    """Exception raised for request errors."""


class KinexonAPI:
    """
    API-key authenticated wrapper for Kinexon API.
    Provides low-level setup for generated kinexon_client.* functions.
    """

    def __init__(
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

        # Use AuthenticatedClient (generated client requires it)
        # Note: We bypass Authorization headers;
        # API key is injected via query by generated funcs.

        self.client = Client(
            base_url=self.base_url,
            # token="",  # not used
            # prefix="",
            # auth_header_name=None,
            headers={"api-key": self.api_key},
            timeout=httpx.Timeout(timeout),
            verify_ssl=self.verify_ssl,
            raise_on_unexpected_status=True,
        )

        self.authenticate()

    def authenticate(
        self,
    ) -> bool:
        """
        Authenticate with Kinexon API using a two-step login:
        1) Persist Basic Auth on the session and GET the session endpoint.
        2) POST JSON (nested 'login') to the main endpoint.
        """
        logger = logging.getLogger(__name__)

        # Use a temporary httpx.Client for authentication
        self.client.get_httpx_client().auth = HTTPBasicAuth(
            self.username_basic,
            self.password_basic,
        )
        # Step 1: Session-level Basic Auth
        resp = self.client.get_httpx_client().get(
            self.endpoint_session,
            # auth=(self.username_basic, self.password_basic),
        )
        if not resp.is_redirect:
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
        resp = self.client.get_httpx_client().post(
            self.endpoint_main, json=payload
        )
        if resp.status_code != 200:
            raise APIRequestError(
                f"Main login failed: {resp.status_code} {resp.text}"
            )
        logger.info("Main authentication successful.")

        return True

    def close(self) -> None:
        self.client.get_httpx_client().close()

    def __enter__(self) -> "KinexonAPI":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def make_custom_request(
        self,
        method: str,
        url: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        stream: bool = False,
        timeout: Optional[float] = None,
    ) -> httpx.Response:
        """
        Low-level custom request via the authenticated httpx.Client.
        If stream=True, returns an open Response with streaming enabled.
        Caller is responsible for closing the response (resp.close()).
        """
        client = self.client.get_httpx_client()

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
