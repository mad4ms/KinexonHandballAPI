from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_deceleration_deceleration_category import EventDecelerationDecelerationCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDeceleration")


@_attrs_define
class EventDeceleration:
    """
    Attributes:
        timestamp (int | Unset):
        timestamp_ms (int | Unset):
        timezone_id (int | Unset):
        game_clock (str | Unset):
        period (str | Unset):
        player_id (int | Unset):
        duration (float | Unset):
        distance (float | Unset):
        speed_max (float | Unset):
        acceleration_min (float | Unset):
        deceleration_avg (float | Unset):
        speed_change (float | Unset):
        trajectory (str | Unset):
        deceleration_category (EventDecelerationDecelerationCategory | Unset):
    """

    timestamp: int | Unset = UNSET
    timestamp_ms: int | Unset = UNSET
    timezone_id: int | Unset = UNSET
    game_clock: str | Unset = UNSET
    period: str | Unset = UNSET
    player_id: int | Unset = UNSET
    duration: float | Unset = UNSET
    distance: float | Unset = UNSET
    speed_max: float | Unset = UNSET
    acceleration_min: float | Unset = UNSET
    deceleration_avg: float | Unset = UNSET
    speed_change: float | Unset = UNSET
    trajectory: str | Unset = UNSET
    deceleration_category: EventDecelerationDecelerationCategory | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        duration = self.duration

        distance = self.distance

        speed_max = self.speed_max

        acceleration_min = self.acceleration_min

        deceleration_avg = self.deceleration_avg

        speed_change = self.speed_change

        trajectory = self.trajectory

        deceleration_category: str | Unset = UNSET
        if not isinstance(self.deceleration_category, Unset):
            deceleration_category = self.deceleration_category.value

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
        if duration is not UNSET:
            field_dict["duration"] = duration
        if distance is not UNSET:
            field_dict["distance"] = distance
        if speed_max is not UNSET:
            field_dict["speed_max"] = speed_max
        if acceleration_min is not UNSET:
            field_dict["acceleration_min"] = acceleration_min
        if deceleration_avg is not UNSET:
            field_dict["deceleration_avg"] = deceleration_avg
        if speed_change is not UNSET:
            field_dict["speed_change"] = speed_change
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if deceleration_category is not UNSET:
            field_dict["deceleration_category"] = deceleration_category

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

        duration = d.pop("duration", UNSET)

        distance = d.pop("distance", UNSET)

        speed_max = d.pop("speed_max", UNSET)

        acceleration_min = d.pop("acceleration_min", UNSET)

        deceleration_avg = d.pop("deceleration_avg", UNSET)

        speed_change = d.pop("speed_change", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _deceleration_category = d.pop("deceleration_category", UNSET)
        deceleration_category: EventDecelerationDecelerationCategory | Unset
        if isinstance(_deceleration_category, Unset):
            deceleration_category = UNSET
        else:
            deceleration_category = EventDecelerationDecelerationCategory(_deceleration_category)

        event_deceleration = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            duration=duration,
            distance=distance,
            speed_max=speed_max,
            acceleration_min=acceleration_min,
            deceleration_avg=deceleration_avg,
            speed_change=speed_change,
            trajectory=trajectory,
            deceleration_category=deceleration_category,
        )

        event_deceleration.additional_properties = d
        return event_deceleration

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
