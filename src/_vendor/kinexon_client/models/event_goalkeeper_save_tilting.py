from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

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
        timestamp (int | Unset):
        timestamp_ms (int | Unset):
        timezone_id (int | Unset):
        game_clock (str | Unset):
        period (str | Unset):
        player_id (int | Unset):
        time_to_ground_ms (float | Unset):
        time_to_feet_ms (float | Unset):
        x (float | Unset):
        y (float | Unset):
        trajectory (str | Unset):
        goalkeeper_save_tilting_category (EventGoalkeeperSaveTiltingGoalkeeperSaveTiltingCategory | Unset):
    """

    timestamp: int | Unset = UNSET
    timestamp_ms: int | Unset = UNSET
    timezone_id: int | Unset = UNSET
    game_clock: str | Unset = UNSET
    period: str | Unset = UNSET
    player_id: int | Unset = UNSET
    time_to_ground_ms: float | Unset = UNSET
    time_to_feet_ms: float | Unset = UNSET
    x: float | Unset = UNSET
    y: float | Unset = UNSET
    trajectory: str | Unset = UNSET
    goalkeeper_save_tilting_category: EventGoalkeeperSaveTiltingGoalkeeperSaveTiltingCategory | Unset = UNSET
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

        goalkeeper_save_tilting_category: str | Unset = UNSET
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
        goalkeeper_save_tilting_category: EventGoalkeeperSaveTiltingGoalkeeperSaveTiltingCategory | Unset
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
