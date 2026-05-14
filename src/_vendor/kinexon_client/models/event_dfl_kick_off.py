from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_dfl_kick_off_dfl_kick_off_category import EventDflKickOffDflKickOffCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDflKickOff")


@_attrs_define
class EventDflKickOff:
    """
    Attributes:
        timestamp (int | Unset):
        timestamp_ms (int | Unset):
        timezone_id (int | Unset):
        game_clock (str | Unset):
        period (str | Unset):
        player_id (int | Unset):
        receiving_player (float | Unset):
        height (float | Unset):
        distance (float | Unset):
        dfl_from_open_play (float | Unset):
        dfl_penalty_box (float | Unset):
        trajectory (str | Unset):
        dfl_kick_off_category (EventDflKickOffDflKickOffCategory | Unset):
    """

    timestamp: int | Unset = UNSET
    timestamp_ms: int | Unset = UNSET
    timezone_id: int | Unset = UNSET
    game_clock: str | Unset = UNSET
    period: str | Unset = UNSET
    player_id: int | Unset = UNSET
    receiving_player: float | Unset = UNSET
    height: float | Unset = UNSET
    distance: float | Unset = UNSET
    dfl_from_open_play: float | Unset = UNSET
    dfl_penalty_box: float | Unset = UNSET
    trajectory: str | Unset = UNSET
    dfl_kick_off_category: EventDflKickOffDflKickOffCategory | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        receiving_player = self.receiving_player

        height = self.height

        distance = self.distance

        dfl_from_open_play = self.dfl_from_open_play

        dfl_penalty_box = self.dfl_penalty_box

        trajectory = self.trajectory

        dfl_kick_off_category: str | Unset = UNSET
        if not isinstance(self.dfl_kick_off_category, Unset):
            dfl_kick_off_category = self.dfl_kick_off_category.value

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
        if receiving_player is not UNSET:
            field_dict["receiving_player"] = receiving_player
        if height is not UNSET:
            field_dict["height"] = height
        if distance is not UNSET:
            field_dict["distance"] = distance
        if dfl_from_open_play is not UNSET:
            field_dict["dfl_from_open_play"] = dfl_from_open_play
        if dfl_penalty_box is not UNSET:
            field_dict["dfl_penalty_box"] = dfl_penalty_box
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if dfl_kick_off_category is not UNSET:
            field_dict["dfl_kick_off_category"] = dfl_kick_off_category

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

        receiving_player = d.pop("receiving_player", UNSET)

        height = d.pop("height", UNSET)

        distance = d.pop("distance", UNSET)

        dfl_from_open_play = d.pop("dfl_from_open_play", UNSET)

        dfl_penalty_box = d.pop("dfl_penalty_box", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _dfl_kick_off_category = d.pop("dfl_kick_off_category", UNSET)
        dfl_kick_off_category: EventDflKickOffDflKickOffCategory | Unset
        if isinstance(_dfl_kick_off_category, Unset):
            dfl_kick_off_category = UNSET
        else:
            dfl_kick_off_category = EventDflKickOffDflKickOffCategory(_dfl_kick_off_category)

        event_dfl_kick_off = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            receiving_player=receiving_player,
            height=height,
            distance=distance,
            dfl_from_open_play=dfl_from_open_play,
            dfl_penalty_box=dfl_penalty_box,
            trajectory=trajectory,
            dfl_kick_off_category=dfl_kick_off_category,
        )

        event_dfl_kick_off.additional_properties = d
        return event_dfl_kick_off

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
