from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_public_v1_statistics_by_session_id_categories_response_200_category_names import (
        GetPublicV1StatisticsBySessionIdCategoriesResponse200CategoryNames,
    )
    from ..models.get_public_v1_statistics_by_session_id_categories_response_200_percentage_maps import (
        GetPublicV1StatisticsBySessionIdCategoriesResponse200PercentageMaps,
    )
    from ..models.get_public_v1_statistics_by_session_id_categories_response_200_players import (
        GetPublicV1StatisticsBySessionIdCategoriesResponse200Players,
    )


T = TypeVar("T", bound="GetPublicV1StatisticsBySessionIdCategoriesResponse200")


@_attrs_define
class GetPublicV1StatisticsBySessionIdCategoriesResponse200:
    """
    Attributes:
        percentage_maps (Union[Unset, GetPublicV1StatisticsBySessionIdCategoriesResponse200PercentageMaps]):
        category_names (Union[Unset, GetPublicV1StatisticsBySessionIdCategoriesResponse200CategoryNames]):
        category_colors (Union[Unset, list[str]]):
        players (Union[Unset, GetPublicV1StatisticsBySessionIdCategoriesResponse200Players]):
    """

    percentage_maps: Union[Unset, "GetPublicV1StatisticsBySessionIdCategoriesResponse200PercentageMaps"] = UNSET
    category_names: Union[Unset, "GetPublicV1StatisticsBySessionIdCategoriesResponse200CategoryNames"] = UNSET
    category_colors: Union[Unset, list[str]] = UNSET
    players: Union[Unset, "GetPublicV1StatisticsBySessionIdCategoriesResponse200Players"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        percentage_maps: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.percentage_maps, Unset):
            percentage_maps = self.percentage_maps.to_dict()

        category_names: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.category_names, Unset):
            category_names = self.category_names.to_dict()

        category_colors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.category_colors, Unset):
            category_colors = self.category_colors

        players: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.players, Unset):
            players = self.players.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percentage_maps is not UNSET:
            field_dict["percentageMaps"] = percentage_maps
        if category_names is not UNSET:
            field_dict["categoryNames"] = category_names
        if category_colors is not UNSET:
            field_dict["categoryColors"] = category_colors
        if players is not UNSET:
            field_dict["players"] = players

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_public_v1_statistics_by_session_id_categories_response_200_category_names import (
            GetPublicV1StatisticsBySessionIdCategoriesResponse200CategoryNames,
        )
        from ..models.get_public_v1_statistics_by_session_id_categories_response_200_percentage_maps import (
            GetPublicV1StatisticsBySessionIdCategoriesResponse200PercentageMaps,
        )
        from ..models.get_public_v1_statistics_by_session_id_categories_response_200_players import (
            GetPublicV1StatisticsBySessionIdCategoriesResponse200Players,
        )

        d = dict(src_dict)
        _percentage_maps = d.pop("percentageMaps", UNSET)
        percentage_maps: Union[Unset, GetPublicV1StatisticsBySessionIdCategoriesResponse200PercentageMaps]
        if isinstance(_percentage_maps, Unset):
            percentage_maps = UNSET
        else:
            percentage_maps = GetPublicV1StatisticsBySessionIdCategoriesResponse200PercentageMaps.from_dict(
                _percentage_maps
            )

        _category_names = d.pop("categoryNames", UNSET)
        category_names: Union[Unset, GetPublicV1StatisticsBySessionIdCategoriesResponse200CategoryNames]
        if isinstance(_category_names, Unset):
            category_names = UNSET
        else:
            category_names = GetPublicV1StatisticsBySessionIdCategoriesResponse200CategoryNames.from_dict(
                _category_names
            )

        category_colors = cast(list[str], d.pop("categoryColors", UNSET))

        _players = d.pop("players", UNSET)
        players: Union[Unset, GetPublicV1StatisticsBySessionIdCategoriesResponse200Players]
        if isinstance(_players, Unset):
            players = UNSET
        else:
            players = GetPublicV1StatisticsBySessionIdCategoriesResponse200Players.from_dict(_players)

        get_public_v1_statistics_by_session_id_categories_response_200 = cls(
            percentage_maps=percentage_maps,
            category_names=category_names,
            category_colors=category_colors,
            players=players,
        )

        get_public_v1_statistics_by_session_id_categories_response_200.additional_properties = d
        return get_public_v1_statistics_by_session_id_categories_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
