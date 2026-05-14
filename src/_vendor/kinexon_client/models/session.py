from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.phase import Phase


T = TypeVar("T", bound="Session")


@_attrs_define
class Session:
    """
    Attributes:
        session_id (int | Unset): Session Example: 12.
        start_session (datetime.datetime | Unset): Start of the session in UTC Example: 2019-01-01 12:00:00.
        end_session (datetime.datetime | None | Unset): End of the session in UTC Example: 2019-01-01 13:00:00.
        duration (int | Unset): Length of session in seconds Example: 1200.
        type_ (str | Unset):  Example: GAME.
        description (str | Unset):  Example: Kinexon Sports vs. Kinexon Industries.
        timezone_id (int | Unset): ID of the timezone the session was recorded in Example: 3.
        group_assignment (str | Unset): The player to group assignment for this session in JSON format Example: {1:
            {'player_id': 1, 'function': 'M'}, 2: {'player_id': 2, 'function': 'C'}}.
        group_colors (list[str] | Unset): Color of the groups in this session in JSON format Example: ['#00ff00',
            '#3399ff'].
        group_names (list[str] | Unset): Name of the respective groups Example: ['Team A', 'Team B'].
        phases (list[Phase] | Unset):
    """

    session_id: int | Unset = UNSET
    start_session: datetime.datetime | Unset = UNSET
    end_session: datetime.datetime | None | Unset = UNSET
    duration: int | Unset = UNSET
    type_: str | Unset = UNSET
    description: str | Unset = UNSET
    timezone_id: int | Unset = UNSET
    group_assignment: str | Unset = UNSET
    group_colors: list[str] | Unset = UNSET
    group_names: list[str] | Unset = UNSET
    phases: list[Phase] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        start_session: str | Unset = UNSET
        if not isinstance(self.start_session, Unset):
            start_session = self.start_session.isoformat()

        end_session: None | str | Unset
        if isinstance(self.end_session, Unset):
            end_session = UNSET
        elif isinstance(self.end_session, datetime.datetime):
            end_session = self.end_session.isoformat()
        else:
            end_session = self.end_session

        duration = self.duration

        type_ = self.type_

        description = self.description

        timezone_id = self.timezone_id

        group_assignment = self.group_assignment

        group_colors: list[str] | Unset = UNSET
        if not isinstance(self.group_colors, Unset):
            group_colors = self.group_colors

        group_names: list[str] | Unset = UNSET
        if not isinstance(self.group_names, Unset):
            group_names = self.group_names

        phases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.phases, Unset):
            phases = []
            for phases_item_data in self.phases:
                phases_item = phases_item_data.to_dict()
                phases.append(phases_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if start_session is not UNSET:
            field_dict["start_session"] = start_session
        if end_session is not UNSET:
            field_dict["end_session"] = end_session
        if duration is not UNSET:
            field_dict["duration"] = duration
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description
        if timezone_id is not UNSET:
            field_dict["timezone_id"] = timezone_id
        if group_assignment is not UNSET:
            field_dict["group_assignment"] = group_assignment
        if group_colors is not UNSET:
            field_dict["group_colors"] = group_colors
        if group_names is not UNSET:
            field_dict["group_names"] = group_names
        if phases is not UNSET:
            field_dict["phases"] = phases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.phase import Phase

        d = dict(src_dict)
        session_id = d.pop("session_id", UNSET)

        _start_session = d.pop("start_session", UNSET)
        start_session: datetime.datetime | Unset
        if isinstance(_start_session, Unset):
            start_session = UNSET
        else:
            start_session = isoparse(_start_session)

        def _parse_end_session(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_session_type_0 = isoparse(data)

                return end_session_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_session = _parse_end_session(d.pop("end_session", UNSET))

        duration = d.pop("duration", UNSET)

        type_ = d.pop("type", UNSET)

        description = d.pop("description", UNSET)

        timezone_id = d.pop("timezone_id", UNSET)

        group_assignment = d.pop("group_assignment", UNSET)

        group_colors = cast(list[str], d.pop("group_colors", UNSET))

        group_names = cast(list[str], d.pop("group_names", UNSET))

        _phases = d.pop("phases", UNSET)
        phases: list[Phase] | Unset = UNSET
        if _phases is not UNSET:
            phases = []
            for phases_item_data in _phases:
                phases_item = Phase.from_dict(phases_item_data)

                phases.append(phases_item)

        session = cls(
            session_id=session_id,
            start_session=start_session,
            end_session=end_session,
            duration=duration,
            type_=type_,
            description=description,
            timezone_id=timezone_id,
            group_assignment=group_assignment,
            group_colors=group_colors,
            group_names=group_names,
            phases=phases,
        )

        session.additional_properties = d
        return session

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
