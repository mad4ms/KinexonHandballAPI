from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_dfl_shot_at_goal_dfl_shot_kind_category import (
    EventDflShotAtGoalDflShotKindCategory,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDflShotAtGoal")


@_attrs_define
class EventDflShotAtGoal:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        x (Union[Unset, float]):
        y (Union[Unset, float]):
        dfl_shot_kind_category (Union[Unset, EventDflShotAtGoalDflShotKindCategory]):
        trajectory (Union[Unset, str]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET
    dfl_shot_kind_category: Union[Unset, EventDflShotAtGoalDflShotKindCategory] = UNSET
    trajectory: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        x = self.x

        y = self.y

        dfl_shot_kind_category: Union[Unset, str] = UNSET
        if not isinstance(self.dfl_shot_kind_category, Unset):
            dfl_shot_kind_category = self.dfl_shot_kind_category.value

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
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if dfl_shot_kind_category is not UNSET:
            field_dict["dfl_shot_kind_category"] = dfl_shot_kind_category
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

        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        _dfl_shot_kind_category = d.pop("dfl_shot_kind_category", UNSET)
        dfl_shot_kind_category: Union[Unset, EventDflShotAtGoalDflShotKindCategory]
        if isinstance(_dfl_shot_kind_category, Unset):
            dfl_shot_kind_category = UNSET
        else:
            dfl_shot_kind_category = EventDflShotAtGoalDflShotKindCategory(_dfl_shot_kind_category)

        trajectory = d.pop("trajectory", UNSET)

        event_dfl_shot_at_goal = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            x=x,
            y=y,
            dfl_shot_kind_category=dfl_shot_kind_category,
            trajectory=trajectory,
        )

        event_dfl_shot_at_goal.additional_properties = d
        return event_dfl_shot_at_goal

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
