from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_dfl_goal_kick_dfl_goal_kick_category import (
    EventDflGoalKickDflGoalKickCategory,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDflGoalKick")


@_attrs_define
class EventDflGoalKick:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        height (Union[Unset, float]):
        distance (Union[Unset, float]):
        trajectory (Union[Unset, str]):
        dfl_goal_kick_category (Union[Unset, EventDflGoalKickDflGoalKickCategory]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    height: Union[Unset, float] = UNSET
    distance: Union[Unset, float] = UNSET
    trajectory: Union[Unset, str] = UNSET
    dfl_goal_kick_category: Union[Unset, EventDflGoalKickDflGoalKickCategory] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        height = self.height

        distance = self.distance

        trajectory = self.trajectory

        dfl_goal_kick_category: Union[Unset, str] = UNSET
        if not isinstance(self.dfl_goal_kick_category, Unset):
            dfl_goal_kick_category = self.dfl_goal_kick_category.value

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
        if height is not UNSET:
            field_dict["height"] = height
        if distance is not UNSET:
            field_dict["distance"] = distance
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if dfl_goal_kick_category is not UNSET:
            field_dict["dfl_goal_kick_category"] = dfl_goal_kick_category

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

        height = d.pop("height", UNSET)

        distance = d.pop("distance", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _dfl_goal_kick_category = d.pop("dfl_goal_kick_category", UNSET)
        dfl_goal_kick_category: Union[Unset, EventDflGoalKickDflGoalKickCategory]
        if isinstance(_dfl_goal_kick_category, Unset):
            dfl_goal_kick_category = UNSET
        else:
            dfl_goal_kick_category = EventDflGoalKickDflGoalKickCategory(_dfl_goal_kick_category)

        event_dfl_goal_kick = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            height=height,
            distance=distance,
            trajectory=trajectory,
            dfl_goal_kick_category=dfl_goal_kick_category,
        )

        event_dfl_goal_kick.additional_properties = d
        return event_dfl_goal_kick

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
