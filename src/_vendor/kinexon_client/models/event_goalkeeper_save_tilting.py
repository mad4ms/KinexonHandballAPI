from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_goalkeeper_save_tilting_goalkeeper_save_tilting_category import (
    EventGoalkeeperSaveTiltingGoalkeeperSaveTiltingCategory,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventGoalkeeperSaveTilting")


@_attrs_define
class EventGoalkeeperSaveTilting:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        time_to_ground_ms (Union[Unset, float]):
        time_to_feet_ms (Union[Unset, float]):
        x (Union[Unset, float]):
        y (Union[Unset, float]):
        trajectory (Union[Unset, str]):
        goalkeeper_save_tilting_category (Union[Unset, EventGoalkeeperSaveTiltingGoalkeeperSaveTiltingCategory]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    time_to_ground_ms: Union[Unset, float] = UNSET
    time_to_feet_ms: Union[Unset, float] = UNSET
    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET
    trajectory: Union[Unset, str] = UNSET
    goalkeeper_save_tilting_category: Union[Unset, EventGoalkeeperSaveTiltingGoalkeeperSaveTiltingCategory] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        time_to_ground_ms = self.time_to_ground_ms

        time_to_feet_ms = self.time_to_feet_ms

        x = self.x

        y = self.y

        trajectory = self.trajectory

        goalkeeper_save_tilting_category: Union[Unset, str] = UNSET
        if not isinstance(self.goalkeeper_save_tilting_category, Unset):
            goalkeeper_save_tilting_category = self.goalkeeper_save_tilting_category.value

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
        if time_to_ground_ms is not UNSET:
            field_dict["time_to_ground_ms"] = time_to_ground_ms
        if time_to_feet_ms is not UNSET:
            field_dict["time_to_feet_ms"] = time_to_feet_ms
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if goalkeeper_save_tilting_category is not UNSET:
            field_dict["goalkeeper_save_tilting_category"] = goalkeeper_save_tilting_category

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

        time_to_ground_ms = d.pop("time_to_ground_ms", UNSET)

        time_to_feet_ms = d.pop("time_to_feet_ms", UNSET)

        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _goalkeeper_save_tilting_category = d.pop("goalkeeper_save_tilting_category", UNSET)
        goalkeeper_save_tilting_category: Union[Unset, EventGoalkeeperSaveTiltingGoalkeeperSaveTiltingCategory]
        if isinstance(_goalkeeper_save_tilting_category, Unset):
            goalkeeper_save_tilting_category = UNSET
        else:
            goalkeeper_save_tilting_category = EventGoalkeeperSaveTiltingGoalkeeperSaveTiltingCategory(
                _goalkeeper_save_tilting_category
            )

        event_goalkeeper_save_tilting = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            time_to_ground_ms=time_to_ground_ms,
            time_to_feet_ms=time_to_feet_ms,
            x=x,
            y=y,
            trajectory=trajectory,
            goalkeeper_save_tilting_category=goalkeeper_save_tilting_category,
        )

        event_goalkeeper_save_tilting.additional_properties = d
        return event_goalkeeper_save_tilting

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
