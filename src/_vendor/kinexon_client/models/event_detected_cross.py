from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_detected_cross_detected_cross_category import EventDetectedCrossDetectedCrossCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDetectedCross")


@_attrs_define
class EventDetectedCross:
    """
    Attributes:
        timestamp (int | Unset):
        timestamp_ms (int | Unset):
        timezone_id (int | Unset):
        game_clock (str | Unset):
        period (str | Unset):
        player_id (int | Unset):
        distance (float | Unset):
        speed_avg (float | Unset):
        speed_max (float | Unset):
        receiving_player_id (float | Unset):
        trajectory (str | Unset):
        detected_cross_category (EventDetectedCrossDetectedCrossCategory | Unset):
    """

    timestamp: int | Unset = UNSET
    timestamp_ms: int | Unset = UNSET
    timezone_id: int | Unset = UNSET
    game_clock: str | Unset = UNSET
    period: str | Unset = UNSET
    player_id: int | Unset = UNSET
    distance: float | Unset = UNSET
    speed_avg: float | Unset = UNSET
    speed_max: float | Unset = UNSET
    receiving_player_id: float | Unset = UNSET
    trajectory: str | Unset = UNSET
    detected_cross_category: EventDetectedCrossDetectedCrossCategory | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        distance = self.distance

        speed_avg = self.speed_avg

        speed_max = self.speed_max

        receiving_player_id = self.receiving_player_id

        trajectory = self.trajectory

        detected_cross_category: str | Unset = UNSET
        if not isinstance(self.detected_cross_category, Unset):
            detected_cross_category = self.detected_cross_category.value

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
        if distance is not UNSET:
            field_dict["distance"] = distance
        if speed_avg is not UNSET:
            field_dict["speed_avg"] = speed_avg
        if speed_max is not UNSET:
            field_dict["speed_max"] = speed_max
        if receiving_player_id is not UNSET:
            field_dict["receiving_player_id"] = receiving_player_id
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if detected_cross_category is not UNSET:
            field_dict["detected_cross_category"] = detected_cross_category

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

        distance = d.pop("distance", UNSET)

        speed_avg = d.pop("speed_avg", UNSET)

        speed_max = d.pop("speed_max", UNSET)

        receiving_player_id = d.pop("receiving_player_id", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _detected_cross_category = d.pop("detected_cross_category", UNSET)
        detected_cross_category: EventDetectedCrossDetectedCrossCategory | Unset
        if isinstance(_detected_cross_category, Unset):
            detected_cross_category = UNSET
        else:
            detected_cross_category = EventDetectedCrossDetectedCrossCategory(_detected_cross_category)

        event_detected_cross = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            distance=distance,
            speed_avg=speed_avg,
            speed_max=speed_max,
            receiving_player_id=receiving_player_id,
            trajectory=trajectory,
            detected_cross_category=detected_cross_category,
        )

        event_detected_cross.additional_properties = d
        return event_detected_cross

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
