from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    time_entity_identifier: str,
    *,
    update_rate: Union[Unset, int] = UNSET,
    compress_output: Union[Unset, bool] = UNSET,
    use_local_frame_imu: Union[Unset, bool] = UNSET,
    players: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["updateRate"] = update_rate

    params["compressOutput"] = compress_output

    params["useLocalFrameIMU"] = use_local_frame_imu

    params["players"] = players

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/export/positions/session/{time_entity_identifier}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[str]:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    time_entity_identifier: str,
    *,
    client: AuthenticatedClient,
    update_rate: Union[Unset, int] = UNSET,
    compress_output: Union[Unset, bool] = UNSET,
    use_local_frame_imu: Union[Unset, bool] = UNSET,
    players: Union[Unset, str] = UNSET,
) -> Response[str]:
    """Get a export for positions of a given session

     Retuns a CSV for the given Session and Parameters

    Args:
        time_entity_identifier (str):
        update_rate (Union[Unset, int]):
        compress_output (Union[Unset, bool]):
        use_local_frame_imu (Union[Unset, bool]):
        players (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        time_entity_identifier=time_entity_identifier,
        update_rate=update_rate,
        compress_output=compress_output,
        use_local_frame_imu=use_local_frame_imu,
        players=players,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    time_entity_identifier: str,
    *,
    client: AuthenticatedClient,
    update_rate: Union[Unset, int] = UNSET,
    compress_output: Union[Unset, bool] = UNSET,
    use_local_frame_imu: Union[Unset, bool] = UNSET,
    players: Union[Unset, str] = UNSET,
) -> Optional[str]:
    """Get a export for positions of a given session

     Retuns a CSV for the given Session and Parameters

    Args:
        time_entity_identifier (str):
        update_rate (Union[Unset, int]):
        compress_output (Union[Unset, bool]):
        use_local_frame_imu (Union[Unset, bool]):
        players (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        time_entity_identifier=time_entity_identifier,
        client=client,
        update_rate=update_rate,
        compress_output=compress_output,
        use_local_frame_imu=use_local_frame_imu,
        players=players,
    ).parsed


async def asyncio_detailed(
    time_entity_identifier: str,
    *,
    client: AuthenticatedClient,
    update_rate: Union[Unset, int] = UNSET,
    compress_output: Union[Unset, bool] = UNSET,
    use_local_frame_imu: Union[Unset, bool] = UNSET,
    players: Union[Unset, str] = UNSET,
) -> Response[str]:
    """Get a export for positions of a given session

     Retuns a CSV for the given Session and Parameters

    Args:
        time_entity_identifier (str):
        update_rate (Union[Unset, int]):
        compress_output (Union[Unset, bool]):
        use_local_frame_imu (Union[Unset, bool]):
        players (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        time_entity_identifier=time_entity_identifier,
        update_rate=update_rate,
        compress_output=compress_output,
        use_local_frame_imu=use_local_frame_imu,
        players=players,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    time_entity_identifier: str,
    *,
    client: AuthenticatedClient,
    update_rate: Union[Unset, int] = UNSET,
    compress_output: Union[Unset, bool] = UNSET,
    use_local_frame_imu: Union[Unset, bool] = UNSET,
    players: Union[Unset, str] = UNSET,
) -> Optional[str]:
    """Get a export for positions of a given session

     Retuns a CSV for the given Session and Parameters

    Args:
        time_entity_identifier (str):
        update_rate (Union[Unset, int]):
        compress_output (Union[Unset, bool]):
        use_local_frame_imu (Union[Unset, bool]):
        players (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            time_entity_identifier=time_entity_identifier,
            client=client,
            update_rate=update_rate,
            compress_output=compress_output,
            use_local_frame_imu=use_local_frame_imu,
            players=players,
        )
    ).parsed
