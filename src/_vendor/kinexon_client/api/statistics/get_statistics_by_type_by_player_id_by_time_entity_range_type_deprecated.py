import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_statistics_by_type_by_player_id_by_time_entity_range_type_deprecated_time_entity_range_type import (
    GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedTimeEntityRangeType,
)
from ...models.get_statistics_by_type_by_player_id_by_time_entity_range_type_deprecated_type import (
    GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedType,
)
from ...models.player_statistic import PlayerStatistic
from ...types import UNSET, Response, Unset


def _get_kwargs(
    type_: GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedType,
    player_id: int,
    time_entity_range_type: GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedTimeEntityRangeType,
    *,
    min_: datetime.datetime,
    max_: datetime.datetime,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_min_ = min_.isoformat()
    params["min"] = json_min_

    json_max_ = max_.isoformat()
    params["max"] = json_max_

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/statistics/{type_}/{player_id}/{time_entity_range_type}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["PlayerStatistic"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PlayerStatistic.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["PlayerStatistic"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedType,
    player_id: int,
    time_entity_range_type: GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedTimeEntityRangeType,
    *,
    client: AuthenticatedClient,
    min_: datetime.datetime,
    max_: datetime.datetime,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[list["PlayerStatistic"]]:
    """Request statistics for a range of statistics

    Args:
        type_ (GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedType):
        player_id (int):
        time_entity_range_type
            (GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedTimeEntityRangeType):
        min_ (datetime.datetime):
        max_ (datetime.datetime):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['PlayerStatistic']]
    """

    kwargs = _get_kwargs(
        type_=type_,
        player_id=player_id,
        time_entity_range_type=time_entity_range_type,
        min_=min_,
        max_=max_,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedType,
    player_id: int,
    time_entity_range_type: GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedTimeEntityRangeType,
    *,
    client: AuthenticatedClient,
    min_: datetime.datetime,
    max_: datetime.datetime,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[list["PlayerStatistic"]]:
    """Request statistics for a range of statistics

    Args:
        type_ (GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedType):
        player_id (int):
        time_entity_range_type
            (GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedTimeEntityRangeType):
        min_ (datetime.datetime):
        max_ (datetime.datetime):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['PlayerStatistic']
    """

    return sync_detailed(
        type_=type_,
        player_id=player_id,
        time_entity_range_type=time_entity_range_type,
        client=client,
        min_=min_,
        max_=max_,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    type_: GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedType,
    player_id: int,
    time_entity_range_type: GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedTimeEntityRangeType,
    *,
    client: AuthenticatedClient,
    min_: datetime.datetime,
    max_: datetime.datetime,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[list["PlayerStatistic"]]:
    """Request statistics for a range of statistics

    Args:
        type_ (GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedType):
        player_id (int):
        time_entity_range_type
            (GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedTimeEntityRangeType):
        min_ (datetime.datetime):
        max_ (datetime.datetime):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['PlayerStatistic']]
    """

    kwargs = _get_kwargs(
        type_=type_,
        player_id=player_id,
        time_entity_range_type=time_entity_range_type,
        min_=min_,
        max_=max_,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedType,
    player_id: int,
    time_entity_range_type: GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedTimeEntityRangeType,
    *,
    client: AuthenticatedClient,
    min_: datetime.datetime,
    max_: datetime.datetime,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[list["PlayerStatistic"]]:
    """Request statistics for a range of statistics

    Args:
        type_ (GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedType):
        player_id (int):
        time_entity_range_type
            (GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedTimeEntityRangeType):
        min_ (datetime.datetime):
        max_ (datetime.datetime):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['PlayerStatistic']
    """

    return (
        await asyncio_detailed(
            type_=type_,
            player_id=player_id,
            time_entity_range_type=time_entity_range_type,
            client=client,
            min_=min_,
            max_=max_,
            fields=fields,
        )
    ).parsed
