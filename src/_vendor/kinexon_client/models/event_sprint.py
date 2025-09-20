from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_sprint_sprint_category import EventSprintSprintCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventSprint")


@_attrs_define
class EventSprint:
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
        speed_avg (Union[Unset, float]):
        sprint_category (Union[Unset, EventSprintSprintCategory]):
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
    speed_avg: Union[Unset, float] = UNSET
    sprint_category: Union[Unset, EventSprintSprintCategory] = UNSET
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

        speed_avg = self.speed_avg

        sprint_category: Union[Unset, str] = UNSET
        if not isinstance(self.sprint_category, Unset):
            sprint_category = self.sprint_category.value

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
        if speed_avg is not UNSET:
            field_dict["speed_avg"] = speed_avg
        if sprint_category is not UNSET:
            field_dict["sprint_category"] = sprint_category
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

        speed_avg = d.pop("speed_avg", UNSET)

        _sprint_category = d.pop("sprint_category", UNSET)
        sprint_category: Union[Unset, EventSprintSprintCategory]
        if isinstance(_sprint_category, Unset):
            sprint_category = UNSET
        else:
            sprint_category = EventSprintSprintCategory(_sprint_category)

        trajectory = d.pop("trajectory", UNSET)

        event_sprint = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            duration=duration,
            distance=distance,
            speed_max=speed_max,
            speed_avg=speed_avg,
            sprint_category=sprint_category,
            trajectory=trajectory,
        )

        event_sprint.additional_properties = d
        return event_sprint

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
