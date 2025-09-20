from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventPlayByPlayer")


@_attrs_define
class EventPlayByPlayer:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        event_name (Union[Unset, str]):
        group_id (Union[Unset, int]):
        player_id (Union[Unset, int]):
        duration (Union[Unset, float]):
        play_id (Union[Unset, float]):
        distance_total (Union[Unset, float]):
        speed_max (Union[Unset, float]):
        accel_max (Union[Unset, float]):
        accel_min (Union[Unset, float]):
        metabolic_work (Union[Unset, float]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    event_name: Union[Unset, str] = UNSET
    group_id: Union[Unset, int] = UNSET
    player_id: Union[Unset, int] = UNSET
    duration: Union[Unset, float] = UNSET
    play_id: Union[Unset, float] = UNSET
    distance_total: Union[Unset, float] = UNSET
    speed_max: Union[Unset, float] = UNSET
    accel_max: Union[Unset, float] = UNSET
    accel_min: Union[Unset, float] = UNSET
    metabolic_work: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        event_name = self.event_name

        group_id = self.group_id

        player_id = self.player_id

        duration = self.duration

        play_id = self.play_id

        distance_total = self.distance_total

        speed_max = self.speed_max

        accel_max = self.accel_max

        accel_min = self.accel_min

        metabolic_work = self.metabolic_work

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
        if event_name is not UNSET:
            field_dict["event_name"] = event_name
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if player_id is not UNSET:
            field_dict["player_id"] = player_id
        if duration is not UNSET:
            field_dict["duration"] = duration
        if play_id is not UNSET:
            field_dict["play_id"] = play_id
        if distance_total is not UNSET:
            field_dict["distance_total"] = distance_total
        if speed_max is not UNSET:
            field_dict["speed_max"] = speed_max
        if accel_max is not UNSET:
            field_dict["accel_max"] = accel_max
        if accel_min is not UNSET:
            field_dict["accel_min"] = accel_min
        if metabolic_work is not UNSET:
            field_dict["metabolic_work"] = metabolic_work

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp", UNSET)

        timestamp_ms = d.pop("timestamp_ms", UNSET)

        timezone_id = d.pop("timezone_id", UNSET)

        game_clock = d.pop("game_clock", UNSET)

        period = d.pop("period", UNSET)

        event_name = d.pop("event_name", UNSET)

        group_id = d.pop("group_id", UNSET)

        player_id = d.pop("player_id", UNSET)

        duration = d.pop("duration", UNSET)

        play_id = d.pop("play_id", UNSET)

        distance_total = d.pop("distance_total", UNSET)

        speed_max = d.pop("speed_max", UNSET)

        accel_max = d.pop("accel_max", UNSET)

        accel_min = d.pop("accel_min", UNSET)

        metabolic_work = d.pop("metabolic_work", UNSET)

        event_play_by_player = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            event_name=event_name,
            group_id=group_id,
            player_id=player_id,
            duration=duration,
            play_id=play_id,
            distance_total=distance_total,
            speed_max=speed_max,
            accel_max=accel_max,
            accel_min=accel_min,
            metabolic_work=metabolic_work,
        )

        event_play_by_player.additional_properties = d
        return event_play_by_player

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
