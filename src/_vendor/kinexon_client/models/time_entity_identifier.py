from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.time_entity_identifier_quick_identifier import (
    TimeEntityIdentifierQuickIdentifier,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeEntityIdentifier")


@_attrs_define
class TimeEntityIdentifier:
    """
    Attributes:
        generic_id (Union[Unset, str]): Generic Session Id
        id (Union[Unset, int]): Session of Phase Id
        quick_identifier (Union[Unset, TimeEntityIdentifierQuickIdentifier]): returns the 'latest' (last ended
            session/phase) or the 'current' (still running) phase/session
    """

    generic_id: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    quick_identifier: Union[Unset, TimeEntityIdentifierQuickIdentifier] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        generic_id = self.generic_id

        id = self.id

        quick_identifier: Union[Unset, str] = UNSET
        if not isinstance(self.quick_identifier, Unset):
            quick_identifier = self.quick_identifier.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if generic_id is not UNSET:
            field_dict["generic-id"] = generic_id
        if id is not UNSET:
            field_dict["id"] = id
        if quick_identifier is not UNSET:
            field_dict["quick-identifier"] = quick_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        generic_id = d.pop("generic-id", UNSET)

        id = d.pop("id", UNSET)

        _quick_identifier = d.pop("quick-identifier", UNSET)
        quick_identifier: Union[Unset, TimeEntityIdentifierQuickIdentifier]
        if isinstance(_quick_identifier, Unset):
            quick_identifier = UNSET
        else:
            quick_identifier = TimeEntityIdentifierQuickIdentifier(_quick_identifier)

        time_entity_identifier = cls(
            generic_id=generic_id,
            id=id,
            quick_identifier=quick_identifier,
        )

        time_entity_identifier.additional_properties = d
        return time_entity_identifier

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
