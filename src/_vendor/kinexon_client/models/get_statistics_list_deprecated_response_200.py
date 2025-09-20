from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetStatisticsListDeprecatedResponse200")


@_attrs_define
class GetStatisticsListDeprecatedResponse200:
    """
    Attributes:
        metrics (Union[Unset, list[str]]):
        events (Union[Unset, list[str]]):
    """

    metrics: Union[Unset, list[str]] = UNSET
    events: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metrics: Union[Unset, list[str]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics

        events: Union[Unset, list[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        metrics = cast(list[str], d.pop("metrics", UNSET))

        events = cast(list[str], d.pop("events", UNSET))

        get_statistics_list_deprecated_response_200 = cls(
            metrics=metrics,
            events=events,
        )

        get_statistics_list_deprecated_response_200.additional_properties = d
        return get_statistics_list_deprecated_response_200

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
