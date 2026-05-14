from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_speed_zone_entry_speed_zone_entry_category import EventSpeedZoneEntrySpeedZoneEntryCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventSpeedZoneEntry")


@_attrs_define
class EventSpeedZoneEntry:
    """
    Attributes:
        timestamp (int | Unset):
        timestamp_ms (int | Unset):
        timezone_id (int | Unset):
        game_clock (str | Unset):
        period (str | Unset):
        player_id (int | Unset):
        trajectory (str | Unset):
        speed_zone_entry_category (EventSpeedZoneEntrySpeedZoneEntryCategory | Unset):
    """

    timestamp: int | Unset = UNSET
    timestamp_ms: int | Unset = UNSET
    timezone_id: int | Unset = UNSET
    game_clock: str | Unset = UNSET
    period: str | Unset = UNSET
    player_id: int | Unset = UNSET
    trajectory: str | Unset = UNSET
    speed_zone_entry_category: EventSpeedZoneEntrySpeedZoneEntryCategory | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        trajectory = self.trajectory

        speed_zone_entry_category: str | Unset = UNSET
        if not isinstance(self.speed_zone_entry_category, Unset):
            speed_zone_entry_category = self.speed_zone_entry_category.value

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
        if player_id is not UNSET:
            field_dict["player_id"] = player_id
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if speed_zone_entry_category is not UNSET:
            field_dict["speed_zone_entry_category"] = speed_zone_entry_category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp", UNSET)

        timestamp_ms = d.pop("timestamp_ms", UNSET)

        timezone_id = d.pop("timezone_id", UNSET)

        game_clock = d.pop("game_clock", UNSET)

        period = d.pop("period", UNSET)

        player_id = d.pop("player_id", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _speed_zone_entry_category = d.pop("speed_zone_entry_category", UNSET)
        speed_zone_entry_category: EventSpeedZoneEntrySpeedZoneEntryCategory | Unset
        if isinstance(_speed_zone_entry_category, Unset):
            speed_zone_entry_category = UNSET
        else:
            speed_zone_entry_category = EventSpeedZoneEntrySpeedZoneEntryCategory(_speed_zone_entry_category)

        event_speed_zone_entry = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            trajectory=trajectory,
            speed_zone_entry_category=speed_zone_entry_category,
        )

        event_speed_zone_entry.additional_properties = d
        return event_speed_zone_entry

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
