from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventShift")


@_attrs_define
class EventShift:
    """
    Attributes:
        timestamp (int | Unset):
        timestamp_ms (int | Unset):
        timezone_id (int | Unset):
        game_clock (str | Unset):
        period (str | Unset):
        player_id (int | Unset):
        end_time (float | Unset):
        duration (float | Unset):
        distance_total (float | Unset):
        distance_speed_category1 (float | Unset):
        distance_speed_category2 (float | Unset):
        distance_speed_category3 (float | Unset):
        distance_speed_category4 (float | Unset):
        distance_speed_category5 (float | Unset):
        distance_speed_category6 (float | Unset):
        distance_speed_category7 (float | Unset):
        metabolic_power_avg (float | Unset):
        speed_max (float | Unset):
        mechanical_load (float | Unset):
        mechanical_intensity (float | Unset):
    """

    timestamp: int | Unset = UNSET
    timestamp_ms: int | Unset = UNSET
    timezone_id: int | Unset = UNSET
    game_clock: str | Unset = UNSET
    period: str | Unset = UNSET
    player_id: int | Unset = UNSET
    end_time: float | Unset = UNSET
    duration: float | Unset = UNSET
    distance_total: float | Unset = UNSET
    distance_speed_category1: float | Unset = UNSET
    distance_speed_category2: float | Unset = UNSET
    distance_speed_category3: float | Unset = UNSET
    distance_speed_category4: float | Unset = UNSET
    distance_speed_category5: float | Unset = UNSET
    distance_speed_category6: float | Unset = UNSET
    distance_speed_category7: float | Unset = UNSET
    metabolic_power_avg: float | Unset = UNSET
    speed_max: float | Unset = UNSET
    mechanical_load: float | Unset = UNSET
    mechanical_intensity: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        end_time = self.end_time

        duration = self.duration

        distance_total = self.distance_total

        distance_speed_category1 = self.distance_speed_category1

        distance_speed_category2 = self.distance_speed_category2

        distance_speed_category3 = self.distance_speed_category3

        distance_speed_category4 = self.distance_speed_category4

        distance_speed_category5 = self.distance_speed_category5

        distance_speed_category6 = self.distance_speed_category6

        distance_speed_category7 = self.distance_speed_category7

        metabolic_power_avg = self.metabolic_power_avg

        speed_max = self.speed_max

        mechanical_load = self.mechanical_load

        mechanical_intensity = self.mechanical_intensity

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
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if duration is not UNSET:
            field_dict["duration"] = duration
        if distance_total is not UNSET:
            field_dict["distance_total"] = distance_total
        if distance_speed_category1 is not UNSET:
            field_dict["distance_speed_category1"] = distance_speed_category1
        if distance_speed_category2 is not UNSET:
            field_dict["distance_speed_category2"] = distance_speed_category2
        if distance_speed_category3 is not UNSET:
            field_dict["distance_speed_category3"] = distance_speed_category3
        if distance_speed_category4 is not UNSET:
            field_dict["distance_speed_category4"] = distance_speed_category4
        if distance_speed_category5 is not UNSET:
            field_dict["distance_speed_category5"] = distance_speed_category5
        if distance_speed_category6 is not UNSET:
            field_dict["distance_speed_category6"] = distance_speed_category6
        if distance_speed_category7 is not UNSET:
            field_dict["distance_speed_category7"] = distance_speed_category7
        if metabolic_power_avg is not UNSET:
            field_dict["metabolic_power_avg"] = metabolic_power_avg
        if speed_max is not UNSET:
            field_dict["speed_max"] = speed_max
        if mechanical_load is not UNSET:
            field_dict["mechanical_load"] = mechanical_load
        if mechanical_intensity is not UNSET:
            field_dict["mechanical_intensity"] = mechanical_intensity

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

        end_time = d.pop("end_time", UNSET)

        duration = d.pop("duration", UNSET)

        distance_total = d.pop("distance_total", UNSET)

        distance_speed_category1 = d.pop("distance_speed_category1", UNSET)

        distance_speed_category2 = d.pop("distance_speed_category2", UNSET)

        distance_speed_category3 = d.pop("distance_speed_category3", UNSET)

        distance_speed_category4 = d.pop("distance_speed_category4", UNSET)

        distance_speed_category5 = d.pop("distance_speed_category5", UNSET)

        distance_speed_category6 = d.pop("distance_speed_category6", UNSET)

        distance_speed_category7 = d.pop("distance_speed_category7", UNSET)

        metabolic_power_avg = d.pop("metabolic_power_avg", UNSET)

        speed_max = d.pop("speed_max", UNSET)

        mechanical_load = d.pop("mechanical_load", UNSET)

        mechanical_intensity = d.pop("mechanical_intensity", UNSET)

        event_shift = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            end_time=end_time,
            duration=duration,
            distance_total=distance_total,
            distance_speed_category1=distance_speed_category1,
            distance_speed_category2=distance_speed_category2,
            distance_speed_category3=distance_speed_category3,
            distance_speed_category4=distance_speed_category4,
            distance_speed_category5=distance_speed_category5,
            distance_speed_category6=distance_speed_category6,
            distance_speed_category7=distance_speed_category7,
            metabolic_power_avg=metabolic_power_avg,
            speed_max=speed_max,
            mechanical_load=mechanical_load,
            mechanical_intensity=mechanical_intensity,
        )

        event_shift.additional_properties = d
        return event_shift

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
