from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_dfl_free_kick_dfl_free_kick_category import (
    EventDflFreeKickDflFreeKickCategory,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDflFreeKick")


@_attrs_define
class EventDflFreeKick:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        dfl_execution_mode (Union[Unset, float]):
        height (Union[Unset, float]):
        distance (Union[Unset, float]):
        dfl_free_kick_play (Union[Unset, float]):
        trajectory (Union[Unset, str]):
        dfl_free_kick_category (Union[Unset, EventDflFreeKickDflFreeKickCategory]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    dfl_execution_mode: Union[Unset, float] = UNSET
    height: Union[Unset, float] = UNSET
    distance: Union[Unset, float] = UNSET
    dfl_free_kick_play: Union[Unset, float] = UNSET
    trajectory: Union[Unset, str] = UNSET
    dfl_free_kick_category: Union[Unset, EventDflFreeKickDflFreeKickCategory] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        dfl_execution_mode = self.dfl_execution_mode

        height = self.height

        distance = self.distance

        dfl_free_kick_play = self.dfl_free_kick_play

        trajectory = self.trajectory

        dfl_free_kick_category: Union[Unset, str] = UNSET
        if not isinstance(self.dfl_free_kick_category, Unset):
            dfl_free_kick_category = self.dfl_free_kick_category.value

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
        if dfl_execution_mode is not UNSET:
            field_dict["dfl_execution_mode"] = dfl_execution_mode
        if height is not UNSET:
            field_dict["height"] = height
        if distance is not UNSET:
            field_dict["distance"] = distance
        if dfl_free_kick_play is not UNSET:
            field_dict["dfl_free_kick_play"] = dfl_free_kick_play
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if dfl_free_kick_category is not UNSET:
            field_dict["dfl_free_kick_category"] = dfl_free_kick_category

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

        dfl_execution_mode = d.pop("dfl_execution_mode", UNSET)

        height = d.pop("height", UNSET)

        distance = d.pop("distance", UNSET)

        dfl_free_kick_play = d.pop("dfl_free_kick_play", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _dfl_free_kick_category = d.pop("dfl_free_kick_category", UNSET)
        dfl_free_kick_category: Union[Unset, EventDflFreeKickDflFreeKickCategory]
        if isinstance(_dfl_free_kick_category, Unset):
            dfl_free_kick_category = UNSET
        else:
            dfl_free_kick_category = EventDflFreeKickDflFreeKickCategory(_dfl_free_kick_category)

        event_dfl_free_kick = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            dfl_execution_mode=dfl_execution_mode,
            height=height,
            distance=distance,
            dfl_free_kick_play=dfl_free_kick_play,
            trajectory=trajectory,
            dfl_free_kick_category=dfl_free_kick_category,
        )

        event_dfl_free_kick.additional_properties = d
        return event_dfl_free_kick

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
