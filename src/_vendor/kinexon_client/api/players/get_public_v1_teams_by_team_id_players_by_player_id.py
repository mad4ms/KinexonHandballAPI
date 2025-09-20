from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.player_model import PlayerModel
from ...types import Response


def _get_kwargs(
    team_id: int,
    player_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/public/v1/teams/{team_id}/players/{player_id}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PlayerModel]:
    if response.status_code == 200:
        response_200 = PlayerModel.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PlayerModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: int,
    player_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[PlayerModel]:
    """Get a player of a team

     Retuns a Player by {id} for given {teamId}

    Args:
        team_id (int):
        player_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PlayerModel]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        player_id=player_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id: int,
    player_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[PlayerModel]:
    """Get a player of a team

     Retuns a Player by {id} for given {teamId}

    Args:
        team_id (int):
        player_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PlayerModel
    """

    return sync_detailed(
        team_id=team_id,
        player_id=player_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    team_id: int,
    player_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[PlayerModel]:
    """Get a player of a team

     Retuns a Player by {id} for given {teamId}

    Args:
        team_id (int):
        player_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PlayerModel]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        player_id=player_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: int,
    player_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[PlayerModel]:
    """Get a player of a team

     Retuns a Player by {id} for given {teamId}

    Args:
        team_id (int):
        player_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PlayerModel
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            player_id=player_id,
            client=client,
        )
    ).parsed
