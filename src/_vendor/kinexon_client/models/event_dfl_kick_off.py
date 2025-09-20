from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_dfl_kick_off_dfl_kick_off_category import (
    EventDflKickOffDflKickOffCategory,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDflKickOff")


@_attrs_define
class EventDflKickOff:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        receiving_player (Union[Unset, float]):
        height (Union[Unset, float]):
        distance (Union[Unset, float]):
        dfl_from_open_play (Union[Unset, float]):
        dfl_penalty_box (Union[Unset, float]):
        trajectory (Union[Unset, str]):
        dfl_kick_off_category (Union[Unset, EventDflKickOffDflKickOffCategory]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    receiving_player: Union[Unset, float] = UNSET
    height: Union[Unset, float] = UNSET
    distance: Union[Unset, float] = UNSET
    dfl_from_open_play: Union[Unset, float] = UNSET
    dfl_penalty_box: Union[Unset, float] = UNSET
    trajectory: Union[Unset, str] = UNSET
    dfl_kick_off_category: Union[Unset, EventDflKickOffDflKickOffCategory] = UNSET
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

        dfl_kick_off_category: Union[Unset, str] = UNSET
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
        dfl_kick_off_category: Union[Unset, EventDflKickOffDflKickOffCategory]
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
