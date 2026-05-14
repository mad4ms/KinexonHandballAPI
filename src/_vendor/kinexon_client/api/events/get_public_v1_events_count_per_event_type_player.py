from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_count import EventCount
from ...models.get_public_v1_events_count_per_event_type_player_time_entity_type import (
    GetPublicV1EventsCountPerEventTypePlayerTimeEntityType,
)
from ...types import Response


def _get_kwargs(
    players: str,
    time_entity_type: GetPublicV1EventsCountPerEventTypePlayerTimeEntityType,
    time_entity_identifier: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/public/v1/events/count-per-event-type/player/{players}/{time_entity_type}/{time_entity_identifier}".format(
            players=quote(str(players), safe=""),
            time_entity_type=quote(str(time_entity_type), safe=""),
            time_entity_identifier=quote(str(time_entity_identifier), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> EventCount | None:
    if response.status_code == 200:
        response_200 = EventCount.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[EventCount]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    players: str,
    time_entity_type: GetPublicV1EventsCountPerEventTypePlayerTimeEntityType,
    time_entity_identifier: str,
    *,
    client: AuthenticatedClient,
) -> Response[EventCount]:
    """Request a list of events and the respective event counts for a set of players.

    Args:
        players (str):
        time_entity_type (GetPublicV1EventsCountPerEventTypePlayerTimeEntityType):
        time_entity_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventCount]
    """

    kwargs = _get_kwargs(
        players=players,
        time_entity_type=time_entity_type,
        time_entity_identifier=time_entity_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    players: str,
    time_entity_type: GetPublicV1EventsCountPerEventTypePlayerTimeEntityType,
    time_entity_identifier: str,
    *,
    client: AuthenticatedClient,
) -> EventCount | None:
    """Request a list of events and the respective event counts for a set of players.

    Args:
        players (str):
        time_entity_type (GetPublicV1EventsCountPerEventTypePlayerTimeEntityType):
        time_entity_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventCount
    """

    return sync_detailed(
        players=players,
        time_entity_type=time_entity_type,
        time_entity_identifier=time_entity_identifier,
        client=client,
    ).parsed


async def asyncio_detailed(
    players: str,
    time_entity_type: GetPublicV1EventsCountPerEventTypePlayerTimeEntityType,
    time_entity_identifier: str,
    *,
    client: AuthenticatedClient,
) -> Response[EventCount]:
    """Request a list of events and the respective event counts for a set of players.

    Args:
        players (str):
        time_entity_type (GetPublicV1EventsCountPerEventTypePlayerTimeEntityType):
        time_entity_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventCount]
    """

    kwargs = _get_kwargs(
        players=players,
        time_entity_type=time_entity_type,
        time_entity_identifier=time_entity_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    players: str,
    time_entity_type: GetPublicV1EventsCountPerEventTypePlayerTimeEntityType,
    time_entity_identifier: str,
    *,
    client: AuthenticatedClient,
) -> EventCount | None:
    """Request a list of events and the respective event counts for a set of players.

    Args:
        players (str):
        time_entity_type (GetPublicV1EventsCountPerEventTypePlayerTimeEntityType):
        time_entity_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventCount
    """

    return (
        await asyncio_detailed(
            players=players,
            time_entity_type=time_entity_type,
            time_entity_identifier=time_entity_identifier,
            client=client,
        )
    ).parsed
