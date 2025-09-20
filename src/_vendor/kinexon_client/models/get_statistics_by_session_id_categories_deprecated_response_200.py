from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_statistics_by_session_id_categories_deprecated_response_200_category_names import (
        GetStatisticsBySessionIdCategoriesDeprecatedResponse200CategoryNames,
    )
    from ..models.get_statistics_by_session_id_categories_deprecated_response_200_percentage_maps import (
        GetStatisticsBySessionIdCategoriesDeprecatedResponse200PercentageMaps,
    )
    from ..models.get_statistics_by_session_id_categories_deprecated_response_200_players import (
        GetStatisticsBySessionIdCategoriesDeprecatedResponse200Players,
    )


T = TypeVar("T", bound="GetStatisticsBySessionIdCategoriesDeprecatedResponse200")


@_attrs_define
class GetStatisticsBySessionIdCategoriesDeprecatedResponse200:
    """
    Attributes:
        percentage_maps (Union[Unset, GetStatisticsBySessionIdCategoriesDeprecatedResponse200PercentageMaps]):
        category_names (Union[Unset, GetStatisticsBySessionIdCategoriesDeprecatedResponse200CategoryNames]):
        category_colors (Union[Unset, list[str]]):
        players (Union[Unset, GetStatisticsBySessionIdCategoriesDeprecatedResponse200Players]):
    """

    percentage_maps: Union[Unset, "GetStatisticsBySessionIdCategoriesDeprecatedResponse200PercentageMaps"] = UNSET
    category_names: Union[Unset, "GetStatisticsBySessionIdCategoriesDeprecatedResponse200CategoryNames"] = UNSET
    category_colors: Union[Unset, list[str]] = UNSET
    players: Union[Unset, "GetStatisticsBySessionIdCategoriesDeprecatedResponse200Players"] = UNSET
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
        from ..models.get_statistics_by_session_id_categories_deprecated_response_200_category_names import (
            GetStatisticsBySessionIdCategoriesDeprecatedResponse200CategoryNames,
        )
        from ..models.get_statistics_by_session_id_categories_deprecated_response_200_percentage_maps import (
            GetStatisticsBySessionIdCategoriesDeprecatedResponse200PercentageMaps,
        )
        from ..models.get_statistics_by_session_id_categories_deprecated_response_200_players import (
            GetStatisticsBySessionIdCategoriesDeprecatedResponse200Players,
        )

        d = dict(src_dict)
        _percentage_maps = d.pop("percentageMaps", UNSET)
        percentage_maps: Union[Unset, GetStatisticsBySessionIdCategoriesDeprecatedResponse200PercentageMaps]
        if isinstance(_percentage_maps, Unset):
            percentage_maps = UNSET
        else:
            percentage_maps = GetStatisticsBySessionIdCategoriesDeprecatedResponse200PercentageMaps.from_dict(
                _percentage_maps
            )

        _category_names = d.pop("categoryNames", UNSET)
        category_names: Union[Unset, GetStatisticsBySessionIdCategoriesDeprecatedResponse200CategoryNames]
        if isinstance(_category_names, Unset):
            category_names = UNSET
        else:
            category_names = GetStatisticsBySessionIdCategoriesDeprecatedResponse200CategoryNames.from_dict(
                _category_names
            )

        category_colors = cast(list[str], d.pop("categoryColors", UNSET))

        _players = d.pop("players", UNSET)
        players: Union[Unset, GetStatisticsBySessionIdCategoriesDeprecatedResponse200Players]
        if isinstance(_players, Unset):
            players = UNSET
        else:
            players = GetStatisticsBySessionIdCategoriesDeprecatedResponse200Players.from_dict(_players)

        get_statistics_by_session_id_categories_deprecated_response_200 = cls(
            percentage_maps=percentage_maps,
            category_names=category_names,
            category_colors=category_colors,
            players=players,
        )

        get_statistics_by_session_id_categories_deprecated_response_200.additional_properties = d
        return get_statistics_by_session_id_categories_deprecated_response_200

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
