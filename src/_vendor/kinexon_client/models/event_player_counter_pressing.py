from collections.abc import Mapping
from typing import Any, TypeVar, Union

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
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        group_id (Union[Unset, int]):
        pressing_index (Union[Unset, float]):
        opponent_player_id (Union[Unset, float]):
        distance_min (Union[Unset, float]):
        distance_max (Union[Unset, float]):
        duration (Union[Unset, float]):
        trajectory (Union[Unset, str]):
        player_counter_pressing_category (Union[Unset, EventPlayerCounterPressingPlayerCounterPressingCategory]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    group_id: Union[Unset, int] = UNSET
    pressing_index: Union[Unset, float] = UNSET
    opponent_player_id: Union[Unset, float] = UNSET
    distance_min: Union[Unset, float] = UNSET
    distance_max: Union[Unset, float] = UNSET
    duration: Union[Unset, float] = UNSET
    trajectory: Union[Unset, str] = UNSET
    player_counter_pressing_category: Union[Unset, EventPlayerCounterPressingPlayerCounterPressingCategory] = UNSET
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

        player_counter_pressing_category: Union[Unset, str] = UNSET
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
        player_counter_pressing_category: Union[Unset, EventPlayerCounterPressingPlayerCounterPressingCategory]
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
