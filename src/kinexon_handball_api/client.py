import logging
from typing import Any, Dict, List, Union, Optional
import requests
from requests.adapters import HTTPAdapter
from requests.auth import HTTPBasicAuth
from urllib3.util.retry import Retry
from tqdm import tqdm

from kinexon_handball_api.config import Settings
from kinexon_handball_api.exceptions import KinexonAPIError
from kinexon_handball_api.fetchers import fetch_team_ids

logger = logging.getLogger(__name__)


class KinexonClient:
    """
    Client for interacting with the Kinexon API.
    Provides methods for authentication, making API requests, and fetching data.
    """

    def __init__(self, settings: Settings):
        self.settings = settings
        self.session = self._init_session()
        self._authenticate()

    def _init_session(self) -> requests.Session:
        session = requests.Session()
        session.verify = getattr(self.settings, "verify_ssl", False)
        return session

    def _authenticate(self) -> None:
        """
        1) Persist Basic Auth on the session and GET the session endpoint.
        2) POST JSON (nested 'login') to the main endpoint.
        """

        # Session-level Basic Auth
        self.session.auth = HTTPBasicAuth(
            self.settings.username_session,
            self.settings.password_session,
        )
        resp = self.session.get(self.settings.endpoint_session, timeout=10)
        if not resp.ok:
            raise KinexonAPIError(
                f"Session login failed: {resp.status_code} {resp.text}",
                status_code=resp.status_code,
            )
        logger.info("Session-level authentication successful.")

        # Main login
        payload = {
            "login": {
                "username": self.settings.username_main,
                "password": self.settings.password_main,
            }
        }

        # funny nginx: it does not like trailing slashes
        # so we try both with and without trailing slash
        ep = self.settings.endpoint_main
        resp = self.session.post(ep, json=payload, timeout=10)
        if not resp or not resp.ok:
            raise KinexonAPIError(
                f"Main login failed at {ep}: "
                f"{resp.status_code if resp else 'N/A'} {resp.text if resp else ''}",
                status_code=resp.status_code if resp else None,
            )
        logger.info("Main authentication successful.")

    def _request(
        self,
        method: str,
        url: str,
        headers: Dict[str, Any] | None = None,
        params: Dict[str, Any] | None = None,
        json_payload: Dict[str, Any] | None = None,
        stream: bool = False,
    ) -> Union[Dict[str, Any], bytes]:
        """Make a request to the Kinexon API.
        Args:
            method (str): HTTP method (GET, POST, etc.)
            url (str): API endpoint URL
            headers (Dict[str, Any], optional): Request headers
            params (Dict[str, Any], optional): Query parameters
            json_payload (Dict[str, Any], optional): JSON payload for POST requests
            stream (bool): Whether to stream the response
        Returns:
            Union[Dict[str, Any], bytes]: JSON response or raw content
        Raises:
            KinexonAPIError: If the request fails
        """
        try:
            # inject api key in headers
            if headers is None:
                headers = {}
            headers["apiKey"] = self.settings.api_key

            resp = self.session.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json_payload,
                stream=stream,
            )
            resp.raise_for_status()

            try:
                return resp.json()
            except ValueError:
                content_type = resp.headers.get("Content-Type", "")
                if content_type.startswith(
                    "text/"
                ) and not content_type.endswith("csv"):
                    return resp.text
                return resp.content

        except requests.HTTPError as e:
            msg = f"API request failed [{method} {url}]: {e.response.status_code} {e.response.text}"
            logger.error(msg)
            raise KinexonAPIError(
                msg, status_code=e.response.status_code
            ) from e

    def get_team_ids(
        self, season: Optional[str] = None
    ) -> List[Dict[str, int]]:
        """
        Fetch the list of team IDs from the Kinexon API.
        Returns:
            List[Dict[str, int]]: List of team IDs and names.
        """
        return fetch_team_ids(season)

    def get_session_ids(self, team_id: int, start: str, end: str) -> Any:
        """
        Fetch event IDs for a specific team within a date range.
        Note: team_id seems to be ineffective, as all sessions are returned.
        Args:
            team_id (int): The ID of the team.
            start (str): Start date in ISO format (YYYY-MM-DD).
            end (str): End date in ISO format (YYYY-MM-DD).
        Returns:
            Any: JSON response containing event IDs.
        """
        url = (
            f"{self.settings.endpoint_api}/teams/{team_id}/sessions-and-phases"
        )
        headers = {"Accept": "application/json"}
        params = {"min": start, "max": end}
        return self._request("GET", url, headers=headers, params=params)

    def get_available_metrics_and_events(self) -> Any:
        """
        Fetch available metrics and events from the Kinexon API.
        Returns:
            Any: JSON response containing metrics and events.
        """
        url = f"{self.settings.endpoint_api}/statistics/list"
        headers = {"Accept": "application/json"}
        return self._request("GET", url, headers=headers)

    def get_position_data_by_session_id(
        self,
        session_id: str,
        update_rate: int = 20,
        compress: bool = False,
        imu_local: bool = False,
        center_origin: bool = False,
        group_by_ts: bool = False,
        players: Union[str, None] = None,
    ) -> bytes:
        """
        Get position data for a specific session.
        Args:
            session_id (str): The ID of the session to get data for.
            update_rate (int): Update rate in Hz (default: 20).
            compress (bool): Whether to compress the output (default: False).
            imu_local (bool): Use local IMU frame (default: False).
            center_origin (bool): Center origin of coordinates (default: False).
            group_by_ts (bool): Group by timestamp (default: False).
            players (Union[str, None]): Comma-separated player IDs to filter by.
        Returns:
            bytes: CSV content of the position data.
        """
        url = f"{self.settings.endpoint_api}/export/positions/session/{session_id}"
        params = {
            "updateRate": update_rate,
            "compressOutput": str(compress).lower(),
            "useLocalFrameIMU": str(imu_local).lower(),
            "centerOrigin": str(center_origin).lower(),
            "groupByTimestamp": str(group_by_ts).lower(),
        }
        if players:
            params["players"] = players

        headers = {"Accept": "text/csv"}

        logger.info(f"Fetching CSV data for session ID: {session_id} ...")

        response = self.session.request(
            "GET", url, headers=headers, params=params, stream=True
        )

        if response.status_code == 200:
            total_size = int(response.headers.get("content-length", 0))
            chunk_size = 1048576  # 1 MB
            csv_data = bytearray()

            # Use tqdm for progress tracking if available
            try:

                with tqdm(
                    total=total_size,
                    unit="B",
                    unit_scale=True,
                    desc="Downloading CSV",
                ) as progress_bar:
                    for chunk in response.iter_content(chunk_size=chunk_size):
                        csv_data.extend(chunk)
                        progress_bar.update(len(chunk))
            except ImportError:
                # Fallback without progress bar
                logger.info(
                    "tqdm not available, downloading without progress bar"
                )
                for chunk in response.iter_content(chunk_size=chunk_size):
                    csv_data.extend(chunk)

            return bytes(csv_data)
        else:
            msg = f"Failed to download CSV data: {response.status_code} {response.text}"
            logger.error(msg)
            raise KinexonAPIError(msg, status_code=response.status_code)
