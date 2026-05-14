from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    time_entity_identifier: str,
    *,
    update_rate: int | Unset = UNSET,
    compress_output: bool | Unset = UNSET,
    players: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["updateRate"] = update_rate

    params["compressOutput"] = compress_output

    params["players"] = players

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/export/inertial/session/{time_entity_identifier}".format(
            time_entity_identifier=quote(str(time_entity_identifier), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[str]:
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
    update_rate: int | Unset = UNSET,
    compress_output: bool | Unset = UNSET,
    players: str | Unset = UNSET,
) -> Response[str]:
    """Get a export for inertial of a given session

     Retuns a CSV for the given Session and Parameters

    Args:
        time_entity_identifier (str):
        update_rate (int | Unset):
        compress_output (bool | Unset):
        players (str | Unset):

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
    update_rate: int | Unset = UNSET,
    compress_output: bool | Unset = UNSET,
    players: str | Unset = UNSET,
) -> str | None:
    """Get a export for inertial of a given session

     Retuns a CSV for the given Session and Parameters

    Args:
        time_entity_identifier (str):
        update_rate (int | Unset):
        compress_output (bool | Unset):
        players (str | Unset):

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
        players=players,
    ).parsed


async def asyncio_detailed(
    time_entity_identifier: str,
    *,
    client: AuthenticatedClient,
    update_rate: int | Unset = UNSET,
    compress_output: bool | Unset = UNSET,
    players: str | Unset = UNSET,
) -> Response[str]:
    """Get a export for inertial of a given session

     Retuns a CSV for the given Session and Parameters

    Args:
        time_entity_identifier (str):
        update_rate (int | Unset):
        compress_output (bool | Unset):
        players (str | Unset):

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
        players=players,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    time_entity_identifier: str,
    *,
    client: AuthenticatedClient,
    update_rate: int | Unset = UNSET,
    compress_output: bool | Unset = UNSET,
    players: str | Unset = UNSET,
) -> str | None:
    """Get a export for inertial of a given session

     Retuns a CSV for the given Session and Parameters

    Args:
        time_entity_identifier (str):
        update_rate (int | Unset):
        compress_output (bool | Unset):
        players (str | Unset):

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
            players=players,
        )
    ).parsed
