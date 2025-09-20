import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Phase")


@_attrs_define
class Phase:
    """
    Attributes:
        id (Union[Unset, int]):  Example: 2.
        session_id (Union[Unset, int]):  Example: 12.
        start_phase (Union[Unset, datetime.datetime]): Start of the phase in UTC Example: 2019-01-01 12:05:00.
        end_phase (Union[None, Unset, datetime.datetime]): End of the phase in UTC Example: 2019-01-01 12:05:00.
        description (Union[Unset, str]):  Example: Sprint Training.
        duration (Union[Unset, int]): Duration of the phase in seconds Example: 60.
        type_ (Union[Unset, str]):  Example: Sprint Training.
        group_assignment (Union[Unset, str]): The player to group assignment for this session in JSON format Example:
            {1: {'player_id': 1, 'function': 'M'}, 2: {'player_id': 2, 'function': 'C'}}.
        group_colors (Union[Unset, list[str]]): Color of the groups in this session in JSON format Example: ['#00ff00',
            '#3399ff'].
        group_names (Union[Unset, list[str]]): Name of the respective groups Example: ['Team A', 'Team B'].
    """

    id: Union[Unset, int] = UNSET
    session_id: Union[Unset, int] = UNSET
    start_phase: Union[Unset, datetime.datetime] = UNSET
    end_phase: Union[None, Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    duration: Union[Unset, int] = UNSET
    type_: Union[Unset, str] = UNSET
    group_assignment: Union[Unset, str] = UNSET
    group_colors: Union[Unset, list[str]] = UNSET
    group_names: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        session_id = self.session_id

        start_phase: Union[Unset, str] = UNSET
        if not isinstance(self.start_phase, Unset):
            start_phase = self.start_phase.isoformat()

        end_phase: Union[None, Unset, str]
        if isinstance(self.end_phase, Unset):
            end_phase = UNSET
        elif isinstance(self.end_phase, datetime.datetime):
            end_phase = self.end_phase.isoformat()
        else:
            end_phase = self.end_phase

        description = self.description

        duration = self.duration

        type_ = self.type_

        group_assignment = self.group_assignment

        group_colors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.group_colors, Unset):
            group_colors = self.group_colors

        group_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.group_names, Unset):
            group_names = self.group_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if start_phase is not UNSET:
            field_dict["start_phase"] = start_phase
        if end_phase is not UNSET:
            field_dict["end_phase"] = end_phase
        if description is not UNSET:
            field_dict["description"] = description
        if duration is not UNSET:
            field_dict["duration"] = duration
        if type_ is not UNSET:
            field_dict["type"] = type_
        if group_assignment is not UNSET:
            field_dict["group_assignment"] = group_assignment
        if group_colors is not UNSET:
            field_dict["group_colors"] = group_colors
        if group_names is not UNSET:
            field_dict["group_names"] = group_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        session_id = d.pop("session_id", UNSET)

        _start_phase = d.pop("start_phase", UNSET)
        start_phase: Union[Unset, datetime.datetime]
        if isinstance(_start_phase, Unset):
            start_phase = UNSET
        else:
            start_phase = isoparse(_start_phase)

        def _parse_end_phase(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_phase_type_0 = isoparse(data)

                return end_phase_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_phase = _parse_end_phase(d.pop("end_phase", UNSET))

        description = d.pop("description", UNSET)

        duration = d.pop("duration", UNSET)

        type_ = d.pop("type", UNSET)

        group_assignment = d.pop("group_assignment", UNSET)

        group_colors = cast(list[str], d.pop("group_colors", UNSET))

        group_names = cast(list[str], d.pop("group_names", UNSET))

        phase = cls(
            id=id,
            session_id=session_id,
            start_phase=start_phase,
            end_phase=end_phase,
            description=description,
            duration=duration,
            type_=type_,
            group_assignment=group_assignment,
            group_colors=group_colors,
            group_names=group_names,
        )

        phase.additional_properties = d
        return phase

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
