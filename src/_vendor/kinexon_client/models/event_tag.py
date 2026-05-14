from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventTag")


@_attrs_define
class EventTag:
    """
    Attributes:
        timestamp (int | Unset):
        timestamp_ms (int | Unset):
        timezone_id (int | Unset):
        game_clock (str | Unset):
        period (str | Unset):
        id (int | Unset):
        tag_type (int | Unset):
        tag_name (str | Unset):
        duration (float | Unset):
        player_id (int | Unset):
        group_id (int | Unset):
    """

    timestamp: int | Unset = UNSET
    timestamp_ms: int | Unset = UNSET
    timezone_id: int | Unset = UNSET
    game_clock: str | Unset = UNSET
    period: str | Unset = UNSET
    id: int | Unset = UNSET
    tag_type: int | Unset = UNSET
    tag_name: str | Unset = UNSET
    duration: float | Unset = UNSET
    player_id: int | Unset = UNSET
    group_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        id = self.id

        tag_type = self.tag_type

        tag_name = self.tag_name

        duration = self.duration

        player_id = self.player_id

        group_id = self.group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if timestamp_ms is not UNSET:
            field_dict["timestamp_ms"] = timestamp_ms
        if timezone_id is not UNSET:
            field_dict["timezone_id"] = timezone_id
        if game_clock is not UNSET:
            field_dict["game_clock"] = game_clock
        if period is not UNSET:
            field_dict["period"] = period
        if id is not UNSET:
            field_dict["id"] = id
        if tag_type is not UNSET:
            field_dict["tag_type"] = tag_type
        if tag_name is not UNSET:
            field_dict["tag_name"] = tag_name
        if duration is not UNSET:
            field_dict["duration"] = duration
        if player_id is not UNSET:
            field_dict["player_id"] = player_id
        if group_id is not UNSET:
            field_dict["group_id"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp", UNSET)

        timestamp_ms = d.pop("timestamp_ms", UNSET)

        timezone_id = d.pop("timezone_id", UNSET)

        game_clock = d.pop("game_clock", UNSET)

        period = d.pop("period", UNSET)

        id = d.pop("id", UNSET)

        tag_type = d.pop("tag_type", UNSET)

        tag_name = d.pop("tag_name", UNSET)

        duration = d.pop("duration", UNSET)

        player_id = d.pop("player_id", UNSET)

        group_id = d.pop("group_id", UNSET)

        event_tag = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            id=id,
            tag_type=tag_type,
            tag_name=tag_name,
            duration=duration,
            player_id=player_id,
            group_id=group_id,
        )

        event_tag.additional_properties = d
        return event_tag

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
