from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventPlayByTeam")


@_attrs_define
class EventPlayByTeam:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        event_name (Union[Unset, str]):
        duration (Union[Unset, float]):
        group_id (Union[Unset, int]):
        down (Union[Unset, float]):
        play_game_clock (Union[Unset, float]):
        yard_line (Union[Unset, float]):
        play_id (Union[Unset, float]):
        yards_to_go (Union[Unset, float]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    event_name: Union[Unset, str] = UNSET
    duration: Union[Unset, float] = UNSET
    group_id: Union[Unset, int] = UNSET
    down: Union[Unset, float] = UNSET
    play_game_clock: Union[Unset, float] = UNSET
    yard_line: Union[Unset, float] = UNSET
    play_id: Union[Unset, float] = UNSET
    yards_to_go: Union[Unset, float] = UNSET
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
