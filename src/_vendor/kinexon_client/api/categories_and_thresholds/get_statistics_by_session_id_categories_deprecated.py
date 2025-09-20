from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_statistics_by_session_id_categories_deprecated_response_200 import (
    GetStatisticsBySessionIdCategoriesDeprecatedResponse200,
)
from ...types import Response


def _get_kwargs(
    session_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/statistics/{session_id}/categories",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetStatisticsBySessionIdCategoriesDeprecatedResponse200]:
    if response.status_code == 200:
        response_200 = GetStatisticsBySessionIdCategoriesDeprecatedResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetStatisticsBySessionIdCategoriesDeprecatedResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GetStatisticsBySessionIdCategoriesDeprecatedResponse200]:
    """Returns categories and thresholds for a session

     Returns categories and thresholds for a session

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStatisticsBySessionIdCategoriesDeprecatedResponse200]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[GetStatisticsBySessionIdCategoriesDeprecatedResponse200]:
    """Returns categories and thresholds for a session

     Returns categories and thresholds for a session

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStatisticsBySessionIdCategoriesDeprecatedResponse200
    """

    return sync_detailed(
        session_id=session_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GetStatisticsBySessionIdCategoriesDeprecatedResponse200]:
    """Returns categories and thresholds for a session

     Returns categories and thresholds for a session

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStatisticsBySessionIdCategoriesDeprecatedResponse200]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[GetStatisticsBySessionIdCategoriesDeprecatedResponse200]:
    """Returns categories and thresholds for a session

     Returns categories and thresholds for a session

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStatisticsBySessionIdCategoriesDeprecatedResponse200
    """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
        )
    ).parsed
