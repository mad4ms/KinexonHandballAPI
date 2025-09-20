from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_public_v1_events_event_type_player_players_time_entity_type_time_entity_identifier_response_200_item import (
    GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierResponse200Item,
)
from ...models.get_public_v1_events_event_type_player_players_time_entity_type_time_entity_identifier_time_entity_type import (
    GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierTimeEntityType,
)
from ...types import Response


def _get_kwargs(
    event_type: str,
    players: str,
    time_entity_type: GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierTimeEntityType,
    time_entity_identifier: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/public/v1/events/{event_type}/player/{players}/{time_entity_type}/{time_entity_identifier}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierResponse200Item"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierResponse200Item.from_dict(
                    response_200_item_data
                )
            )

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierResponse200Item"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_type: str,
    players: str,
    time_entity_type: GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierTimeEntityType,
    time_entity_identifier: str,
    *,
    client: AuthenticatedClient,
) -> Response[list["GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierResponse200Item"]]:
    """Request a list of events and the respective event counts for a set of players.

    Args:
        event_type (str):
        players (str):
        time_entity_type
            (GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierTimeEntityType):
        time_entity_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierResponse200Item']]
    """

    kwargs = _get_kwargs(
        event_type=event_type,
        players=players,
        time_entity_type=time_entity_type,
        time_entity_identifier=time_entity_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_type: str,
    players: str,
    time_entity_type: GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierTimeEntityType,
    time_entity_identifier: str,
    *,
    client: AuthenticatedClient,
) -> Optional[list["GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierResponse200Item"]]:
    """Request a list of events and the respective event counts for a set of players.

    Args:
        event_type (str):
        players (str):
        time_entity_type
            (GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierTimeEntityType):
        time_entity_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierResponse200Item']
    """

    return sync_detailed(
        event_type=event_type,
        players=players,
        time_entity_type=time_entity_type,
        time_entity_identifier=time_entity_identifier,
        client=client,
    ).parsed


async def asyncio_detailed(
    event_type: str,
    players: str,
    time_entity_type: GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierTimeEntityType,
    time_entity_identifier: str,
    *,
    client: AuthenticatedClient,
) -> Response[list["GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierResponse200Item"]]:
    """Request a list of events and the respective event counts for a set of players.

    Args:
        event_type (str):
        players (str):
        time_entity_type
            (GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierTimeEntityType):
        time_entity_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierResponse200Item']]
    """

    kwargs = _get_kwargs(
        event_type=event_type,
        players=players,
        time_entity_type=time_entity_type,
        time_entity_identifier=time_entity_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_type: str,
    players: str,
    time_entity_type: GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierTimeEntityType,
    time_entity_identifier: str,
    *,
    client: AuthenticatedClient,
) -> Optional[list["GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierResponse200Item"]]:
    """Request a list of events and the respective event counts for a set of players.

    Args:
        event_type (str):
        players (str):
        time_entity_type
            (GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierTimeEntityType):
        time_entity_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['GetPublicV1EventsEventTypePlayerPlayersTimeEntityTypeTimeEntityIdentifierResponse200Item']
    """

    return (
        await asyncio_detailed(
            event_type=event_type,
            players=players,
            time_entity_type=time_entity_type,
            time_entity_identifier=time_entity_identifier,
            client=client,
        )
    ).parsed
