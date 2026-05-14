from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_turn_ice_hockey_turn_category import EventTurnIceHockeyTurnCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventTurnIceHockey")


@_attrs_define
class EventTurnIceHockey:
    """
    Attributes:
        timestamp (int | Unset):
        timestamp_ms (int | Unset):
        timezone_id (int | Unset):
        game_clock (str | Unset):
        period (str | Unset):
        player_id (int | Unset):
        group_id (int | Unset):
        duration (float | Unset):
        turn_radius (float | Unset):
        turn_angle (float | Unset):
        direction_of_rotation (float | Unset):
        turn_speed_start (float | Unset):
        turn_speed_end (float | Unset):
        trajectory (str | Unset):
        turn_category (EventTurnIceHockeyTurnCategory | Unset):
    """

    timestamp: int | Unset = UNSET
    timestamp_ms: int | Unset = UNSET
    timezone_id: int | Unset = UNSET
    game_clock: str | Unset = UNSET
    period: str | Unset = UNSET
    player_id: int | Unset = UNSET
    group_id: int | Unset = UNSET
    duration: float | Unset = UNSET
    turn_radius: float | Unset = UNSET
    turn_angle: float | Unset = UNSET
    direction_of_rotation: float | Unset = UNSET
    turn_speed_start: float | Unset = UNSET
    turn_speed_end: float | Unset = UNSET
    trajectory: str | Unset = UNSET
    turn_category: EventTurnIceHockeyTurnCategory | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        group_id = self.group_id

        duration = self.duration

        turn_radius = self.turn_radius

        turn_angle = self.turn_angle

        direction_of_rotation = self.direction_of_rotation

        turn_speed_start = self.turn_speed_start

        turn_speed_end = self.turn_speed_end

        trajectory = self.trajectory

        turn_category: str | Unset = UNSET
        if not isinstance(self.turn_category, Unset):
            turn_category = self.turn_category.value

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
        if duration is not UNSET:
            field_dict["duration"] = duration
        if turn_radius is not UNSET:
            field_dict["turn_radius"] = turn_radius
        if turn_angle is not UNSET:
            field_dict["turn_angle"] = turn_angle
        if direction_of_rotation is not UNSET:
            field_dict["direction_of_rotation"] = direction_of_rotation
        if turn_speed_start is not UNSET:
            field_dict["turn_speed_start"] = turn_speed_start
        if turn_speed_end is not UNSET:
            field_dict["turn_speed_end"] = turn_speed_end
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if turn_category is not UNSET:
            field_dict["turn_category"] = turn_category

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

        duration = d.pop("duration", UNSET)

        turn_radius = d.pop("turn_radius", UNSET)

        turn_angle = d.pop("turn_angle", UNSET)

        direction_of_rotation = d.pop("direction_of_rotation", UNSET)

        turn_speed_start = d.pop("turn_speed_start", UNSET)

        turn_speed_end = d.pop("turn_speed_end", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _turn_category = d.pop("turn_category", UNSET)
        turn_category: EventTurnIceHockeyTurnCategory | Unset
        if isinstance(_turn_category, Unset):
            turn_category = UNSET
        else:
            turn_category = EventTurnIceHockeyTurnCategory(_turn_category)

        event_turn_ice_hockey = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            group_id=group_id,
            duration=duration,
            turn_radius=turn_radius,
            turn_angle=turn_angle,
            direction_of_rotation=direction_of_rotation,
            turn_speed_start=turn_speed_start,
            turn_speed_end=turn_speed_end,
            trajectory=trajectory,
            turn_category=turn_category,
        )

        event_turn_ice_hockey.additional_properties = d
        return event_turn_ice_hockey

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
