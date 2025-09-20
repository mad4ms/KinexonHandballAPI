from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_exertion_exertion_category import EventExertionExertionCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventExertion")


@_attrs_define
class EventExertion:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        duration (Union[Unset, float]):
        accel_load_avg (Union[Unset, float]):
        accel_load_max (Union[Unset, float]):
        distance (Union[Unset, float]):
        speed_max (Union[Unset, float]):
        trajectory (Union[Unset, str]):
        exertion_category (Union[Unset, EventExertionExertionCategory]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    duration: Union[Unset, float] = UNSET
    accel_load_avg: Union[Unset, float] = UNSET
    accel_load_max: Union[Unset, float] = UNSET
    distance: Union[Unset, float] = UNSET
    speed_max: Union[Unset, float] = UNSET
    trajectory: Union[Unset, str] = UNSET
    exertion_category: Union[Unset, EventExertionExertionCategory] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        duration = self.duration

        accel_load_avg = self.accel_load_avg

        accel_load_max = self.accel_load_max

        distance = self.distance

        speed_max = self.speed_max

        trajectory = self.trajectory

        exertion_category: Union[Unset, str] = UNSET
        if not isinstance(self.exertion_category, Unset):
            exertion_category = self.exertion_category.value

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
        if accel_load_avg is not UNSET:
            field_dict["accel_load_avg"] = accel_load_avg
        if accel_load_max is not UNSET:
            field_dict["accel_load_max"] = accel_load_max
        if distance is not UNSET:
            field_dict["distance"] = distance
        if speed_max is not UNSET:
            field_dict["speed_max"] = speed_max
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if exertion_category is not UNSET:
            field_dict["exertion_category"] = exertion_category

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

        accel_load_avg = d.pop("accel_load_avg", UNSET)

        accel_load_max = d.pop("accel_load_max", UNSET)

        distance = d.pop("distance", UNSET)

        speed_max = d.pop("speed_max", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _exertion_category = d.pop("exertion_category", UNSET)
        exertion_category: Union[Unset, EventExertionExertionCategory]
        if isinstance(_exertion_category, Unset):
            exertion_category = UNSET
        else:
            exertion_category = EventExertionExertionCategory(_exertion_category)

        event_exertion = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            duration=duration,
            accel_load_avg=accel_load_avg,
            accel_load_max=accel_load_max,
            distance=distance,
            speed_max=speed_max,
            trajectory=trajectory,
            exertion_category=exertion_category,
        )

        event_exertion.additional_properties = d
        return event_exertion

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
