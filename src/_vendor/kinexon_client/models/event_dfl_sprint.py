from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDflSprint")


@_attrs_define
class EventDflSprint:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        duration (Union[Unset, float]):
        distance (Union[Unset, float]):
        speed_max (Union[Unset, float]):
        x1 (Union[Unset, float]):
        y1 (Union[Unset, float]):
        x2 (Union[Unset, float]):
        y2 (Union[Unset, float]):
        x3 (Union[Unset, float]):
        y3 (Union[Unset, float]):
        x4 (Union[Unset, float]):
        y4 (Union[Unset, float]):
        x5 (Union[Unset, float]):
        y5 (Union[Unset, float]):
        trajectory (Union[Unset, str]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    duration: Union[Unset, float] = UNSET
    distance: Union[Unset, float] = UNSET
    speed_max: Union[Unset, float] = UNSET
    x1: Union[Unset, float] = UNSET
    y1: Union[Unset, float] = UNSET
    x2: Union[Unset, float] = UNSET
    y2: Union[Unset, float] = UNSET
    x3: Union[Unset, float] = UNSET
    y3: Union[Unset, float] = UNSET
    x4: Union[Unset, float] = UNSET
    y4: Union[Unset, float] = UNSET
    x5: Union[Unset, float] = UNSET
    y5: Union[Unset, float] = UNSET
    trajectory: Union[Unset, str] = UNSET
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
