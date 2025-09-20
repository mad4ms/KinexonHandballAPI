from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_goal_kick_goal_kick_category import EventGoalKickGoalKickCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventGoalKick")


@_attrs_define
class EventGoalKick:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        speed (Union[Unset, float]):
        distance (Union[Unset, float]):
        receiving_player_id (Union[Unset, float]):
        successful (Union[Unset, float]):
        duration (Union[Unset, float]):
        trajectory (Union[Unset, str]):
        goal_kick_category (Union[Unset, EventGoalKickGoalKickCategory]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    speed: Union[Unset, float] = UNSET
    distance: Union[Unset, float] = UNSET
    receiving_player_id: Union[Unset, float] = UNSET
    successful: Union[Unset, float] = UNSET
    duration: Union[Unset, float] = UNSET
    trajectory: Union[Unset, str] = UNSET
    goal_kick_category: Union[Unset, EventGoalKickGoalKickCategory] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        speed = self.speed

        distance = self.distance

        receiving_player_id = self.receiving_player_id

        successful = self.successful

        duration = self.duration

        trajectory = self.trajectory

        goal_kick_category: Union[Unset, str] = UNSET
        if not isinstance(self.goal_kick_category, Unset):
            goal_kick_category = self.goal_kick_category.value

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
        if speed is not UNSET:
            field_dict["speed"] = speed
        if distance is not UNSET:
            field_dict["distance"] = distance
        if receiving_player_id is not UNSET:
            field_dict["receiving_player_id"] = receiving_player_id
        if successful is not UNSET:
            field_dict["successful"] = successful
        if duration is not UNSET:
            field_dict["duration"] = duration
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if goal_kick_category is not UNSET:
            field_dict["goal_kick_category"] = goal_kick_category

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

        speed = d.pop("speed", UNSET)

        distance = d.pop("distance", UNSET)

        receiving_player_id = d.pop("receiving_player_id", UNSET)

        successful = d.pop("successful", UNSET)

        duration = d.pop("duration", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _goal_kick_category = d.pop("goal_kick_category", UNSET)
        goal_kick_category: Union[Unset, EventGoalKickGoalKickCategory]
        if isinstance(_goal_kick_category, Unset):
            goal_kick_category = UNSET
        else:
            goal_kick_category = EventGoalKickGoalKickCategory(_goal_kick_category)

        event_goal_kick = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            speed=speed,
            distance=distance,
            receiving_player_id=receiving_player_id,
            successful=successful,
            duration=duration,
            trajectory=trajectory,
            goal_kick_category=goal_kick_category,
        )

        event_goal_kick.additional_properties = d
        return event_goal_kick

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
