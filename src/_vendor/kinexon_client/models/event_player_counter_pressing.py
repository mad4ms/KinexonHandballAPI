from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_player_counter_pressing_player_counter_pressing_category import (
    EventPlayerCounterPressingPlayerCounterPressingCategory,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventPlayerCounterPressing")


@_attrs_define
class EventPlayerCounterPressing:
    """
    Attributes:
        timestamp (int | Unset):
        timestamp_ms (int | Unset):
        timezone_id (int | Unset):
        game_clock (str | Unset):
        period (str | Unset):
        player_id (int | Unset):
        group_id (int | Unset):
        pressing_index (float | Unset):
        opponent_player_id (float | Unset):
        distance_min (float | Unset):
        distance_max (float | Unset):
        duration (float | Unset):
        trajectory (str | Unset):
        player_counter_pressing_category (EventPlayerCounterPressingPlayerCounterPressingCategory | Unset):
    """

    timestamp: int | Unset = UNSET
    timestamp_ms: int | Unset = UNSET
    timezone_id: int | Unset = UNSET
    game_clock: str | Unset = UNSET
    period: str | Unset = UNSET
    player_id: int | Unset = UNSET
    group_id: int | Unset = UNSET
    pressing_index: float | Unset = UNSET
    opponent_player_id: float | Unset = UNSET
    distance_min: float | Unset = UNSET
    distance_max: float | Unset = UNSET
    duration: float | Unset = UNSET
    trajectory: str | Unset = UNSET
    player_counter_pressing_category: EventPlayerCounterPressingPlayerCounterPressingCategory | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        group_id = self.group_id

        pressing_index = self.pressing_index

        opponent_player_id = self.opponent_player_id

        distance_min = self.distance_min

        distance_max = self.distance_max

        duration = self.duration

        trajectory = self.trajectory

        player_counter_pressing_category: str | Unset = UNSET
        if not isinstance(self.player_counter_pressing_category, Unset):
            player_counter_pressing_category = self.player_counter_pressing_category.value

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
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if pressing_index is not UNSET:
            field_dict["pressing_index"] = pressing_index
        if opponent_player_id is not UNSET:
            field_dict["opponent_player_id"] = opponent_player_id
        if distance_min is not UNSET:
            field_dict["distance_min"] = distance_min
        if distance_max is not UNSET:
            field_dict["distance_max"] = distance_max
        if duration is not UNSET:
            field_dict["duration"] = duration
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if player_counter_pressing_category is not UNSET:
            field_dict["player_counter_pressing_category"] = player_counter_pressing_category

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

        group_id = d.pop("group_id", UNSET)

        pressing_index = d.pop("pressing_index", UNSET)

        opponent_player_id = d.pop("opponent_player_id", UNSET)

        distance_min = d.pop("distance_min", UNSET)

        distance_max = d.pop("distance_max", UNSET)

        duration = d.pop("duration", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _player_counter_pressing_category = d.pop("player_counter_pressing_category", UNSET)
        player_counter_pressing_category: EventPlayerCounterPressingPlayerCounterPressingCategory | Unset
        if isinstance(_player_counter_pressing_category, Unset):
            player_counter_pressing_category = UNSET
        else:
            player_counter_pressing_category = EventPlayerCounterPressingPlayerCounterPressingCategory(
                _player_counter_pressing_category
            )

        event_player_counter_pressing = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            group_id=group_id,
            pressing_index=pressing_index,
            opponent_player_id=opponent_player_id,
            distance_min=distance_min,
            distance_max=distance_max,
            duration=duration,
            trajectory=trajectory,
            player_counter_pressing_category=player_counter_pressing_category,
        )

        event_player_counter_pressing.additional_properties = d
        return event_player_counter_pressing

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
