from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDflSprint")


@_attrs_define
class EventDflSprint:
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
        x1 (float | Unset):
        y1 (float | Unset):
        x2 (float | Unset):
        y2 (float | Unset):
        x3 (float | Unset):
        y3 (float | Unset):
        x4 (float | Unset):
        y4 (float | Unset):
        x5 (float | Unset):
        y5 (float | Unset):
        trajectory (str | Unset):
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
    x1: float | Unset = UNSET
    y1: float | Unset = UNSET
    x2: float | Unset = UNSET
    y2: float | Unset = UNSET
    x3: float | Unset = UNSET
    y3: float | Unset = UNSET
    x4: float | Unset = UNSET
    y4: float | Unset = UNSET
    x5: float | Unset = UNSET
    y5: float | Unset = UNSET
    trajectory: str | Unset = UNSET
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

        x1 = self.x1

        y1 = self.y1

        x2 = self.x2

        y2 = self.y2

        x3 = self.x3

        y3 = self.y3

        x4 = self.x4

        y4 = self.y4

        x5 = self.x5

        y5 = self.y5

        trajectory = self.trajectory

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
        if x1 is not UNSET:
            field_dict["x1"] = x1
        if y1 is not UNSET:
            field_dict["y1"] = y1
        if x2 is not UNSET:
            field_dict["x2"] = x2
        if y2 is not UNSET:
            field_dict["y2"] = y2
        if x3 is not UNSET:
            field_dict["x3"] = x3
        if y3 is not UNSET:
            field_dict["y3"] = y3
        if x4 is not UNSET:
            field_dict["x4"] = x4
        if y4 is not UNSET:
            field_dict["y4"] = y4
        if x5 is not UNSET:
            field_dict["x5"] = x5
        if y5 is not UNSET:
            field_dict["y5"] = y5
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory

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

        x1 = d.pop("x1", UNSET)

        y1 = d.pop("y1", UNSET)

        x2 = d.pop("x2", UNSET)

        y2 = d.pop("y2", UNSET)

        x3 = d.pop("x3", UNSET)

        y3 = d.pop("y3", UNSET)

        x4 = d.pop("x4", UNSET)

        y4 = d.pop("y4", UNSET)

        x5 = d.pop("x5", UNSET)

        y5 = d.pop("y5", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        event_dfl_sprint = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            duration=duration,
            distance=distance,
            speed_max=speed_max,
            x1=x1,
            y1=y1,
            x2=x2,
            y2=y2,
            x3=x3,
            y3=y3,
            x4=x4,
            y4=y4,
            x5=x5,
            y5=y5,
            trajectory=trajectory,
        )

        event_dfl_sprint.additional_properties = d
        return event_dfl_sprint

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
