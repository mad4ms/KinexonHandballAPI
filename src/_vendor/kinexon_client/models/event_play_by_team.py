from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventPlayByTeam")


@_attrs_define
class EventPlayByTeam:
    """
    Attributes:
        timestamp (int | Unset):
        timestamp_ms (int | Unset):
        timezone_id (int | Unset):
        game_clock (str | Unset):
        period (str | Unset):
        event_name (str | Unset):
        duration (float | Unset):
        group_id (int | Unset):
        down (float | Unset):
        play_game_clock (float | Unset):
        yard_line (float | Unset):
        play_id (float | Unset):
        yards_to_go (float | Unset):
    """

    timestamp: int | Unset = UNSET
    timestamp_ms: int | Unset = UNSET
    timezone_id: int | Unset = UNSET
    game_clock: str | Unset = UNSET
    period: str | Unset = UNSET
    event_name: str | Unset = UNSET
    duration: float | Unset = UNSET
    group_id: int | Unset = UNSET
    down: float | Unset = UNSET
    play_game_clock: float | Unset = UNSET
    yard_line: float | Unset = UNSET
    play_id: float | Unset = UNSET
    yards_to_go: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        event_name = self.event_name

        duration = self.duration

        group_id = self.group_id

        down = self.down

        play_game_clock = self.play_game_clock

        yard_line = self.yard_line

        play_id = self.play_id

        yards_to_go = self.yards_to_go

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
        if event_name is not UNSET:
            field_dict["event_name"] = event_name
        if duration is not UNSET:
            field_dict["duration"] = duration
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if down is not UNSET:
            field_dict["down"] = down
        if play_game_clock is not UNSET:
            field_dict["play_game_clock"] = play_game_clock
        if yard_line is not UNSET:
            field_dict["yard_line"] = yard_line
        if play_id is not UNSET:
            field_dict["play_id"] = play_id
        if yards_to_go is not UNSET:
            field_dict["yards_to_go"] = yards_to_go

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp", UNSET)

        timestamp_ms = d.pop("timestamp_ms", UNSET)

        timezone_id = d.pop("timezone_id", UNSET)

        game_clock = d.pop("game_clock", UNSET)

        period = d.pop("period", UNSET)

        event_name = d.pop("event_name", UNSET)

        duration = d.pop("duration", UNSET)

        group_id = d.pop("group_id", UNSET)

        down = d.pop("down", UNSET)

        play_game_clock = d.pop("play_game_clock", UNSET)

        yard_line = d.pop("yard_line", UNSET)

        play_id = d.pop("play_id", UNSET)

        yards_to_go = d.pop("yards_to_go", UNSET)

        event_play_by_team = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            event_name=event_name,
            duration=duration,
            group_id=group_id,
            down=down,
            play_game_clock=play_game_clock,
            yard_line=yard_line,
            play_id=play_id,
            yards_to_go=yards_to_go,
        )

        event_play_by_team.additional_properties = d
        return event_play_by_team

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
