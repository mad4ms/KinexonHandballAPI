from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_detected_shot_ice_hockey_shot_made import (
    EventDetectedShotIceHockeyShotMade,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDetectedShotIceHockey")


@_attrs_define
class EventDetectedShotIceHockey:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        distance (Union[Unset, float]):
        speed_puck (Union[Unset, float]):
        trajectory (Union[Unset, str]):
        shot_made (Union[Unset, EventDetectedShotIceHockeyShotMade]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    distance: Union[Unset, float] = UNSET
    speed_puck: Union[Unset, float] = UNSET
    trajectory: Union[Unset, str] = UNSET
    shot_made: Union[Unset, EventDetectedShotIceHockeyShotMade] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        distance = self.distance

        speed_puck = self.speed_puck

        trajectory = self.trajectory

        shot_made: Union[Unset, int] = UNSET
        if not isinstance(self.shot_made, Unset):
            shot_made = self.shot_made.value

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
        if distance is not UNSET:
            field_dict["distance"] = distance
        if speed_puck is not UNSET:
            field_dict["speed_puck"] = speed_puck
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if shot_made is not UNSET:
            field_dict["shot_made"] = shot_made

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

        distance = d.pop("distance", UNSET)

        speed_puck = d.pop("speed_puck", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _shot_made = d.pop("shot_made", UNSET)
        shot_made: Union[Unset, EventDetectedShotIceHockeyShotMade]
        if isinstance(_shot_made, Unset):
            shot_made = UNSET
        else:
            shot_made = EventDetectedShotIceHockeyShotMade(_shot_made)

        event_detected_shot_ice_hockey = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            distance=distance,
            speed_puck=speed_puck,
            trajectory=trajectory,
            shot_made=shot_made,
        )

        event_detected_shot_ice_hockey.additional_properties = d
        return event_detected_shot_ice_hockey

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
