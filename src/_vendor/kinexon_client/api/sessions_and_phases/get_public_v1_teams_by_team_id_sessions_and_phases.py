import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.session import Session
from ...types import UNSET, Response


def _get_kwargs(
    team_id: int,
    *,
    min_: datetime.datetime,
    max_: datetime.datetime,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_min_ = min_.isoformat()
    params["min"] = json_min_

    json_max_ = max_.isoformat()
    params["max"] = json_max_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/public/v1/teams/{team_id}/sessions-and-phases",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["Session"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Session.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["Session"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: int,
    *,
    client: AuthenticatedClient,
    min_: datetime.datetime,
    max_: datetime.datetime,
) -> Response[list["Session"]]:
    """List of sessions and nested phases

     Retuns a list of all sessions for given {teamId} in range {min} - {max}.

    Args:
        team_id (int):
        min_ (datetime.datetime):
        max_ (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Session']]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        min_=min_,
        max_=max_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id: int,
    *,
    client: AuthenticatedClient,
    min_: datetime.datetime,
    max_: datetime.datetime,
) -> Optional[list["Session"]]:
    """List of sessions and nested phases

     Retuns a list of all sessions for given {teamId} in range {min} - {max}.

    Args:
        team_id (int):
        min_ (datetime.datetime):
        max_ (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Session']
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        min_=min_,
        max_=max_,
    ).parsed


async def asyncio_detailed(
    team_id: int,
    *,
    client: AuthenticatedClient,
    min_: datetime.datetime,
    max_: datetime.datetime,
) -> Response[list["Session"]]:
    """List of sessions and nested phases

     Retuns a list of all sessions for given {teamId} in range {min} - {max}.

    Args:
        team_id (int):
        min_ (datetime.datetime):
        max_ (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Session']]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        min_=min_,
        max_=max_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: int,
    *,
    client: AuthenticatedClient,
    min_: datetime.datetime,
    max_: datetime.datetime,
) -> Optional[list["Session"]]:
    """List of sessions and nested phases

     Retuns a list of all sessions for given {teamId} in range {min} - {max}.

    Args:
        team_id (int):
        min_ (datetime.datetime):
        max_ (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Session']
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            min_=min_,
            max_=max_,
        )
    ).parsed
