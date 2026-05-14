from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_detected_pass_type import EventDetectedPassType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDetectedPass")


@_attrs_define
class EventDetectedPass:
    """
    Attributes:
        timestamp (int | Unset):
        timestamp_ms (int | Unset):
        timezone_id (int | Unset):
        game_clock (str | Unset):
        period (str | Unset):
        player_id (int | Unset):
        distance (float | Unset):
        speed_ball (float | Unset):
        packing (float | Unset):
        receiving_player_id (float | Unset):
        verticality (float | Unset):
        horizontality (float | Unset):
        trajectory (str | Unset):
        type_ (EventDetectedPassType | Unset):
    """

    timestamp: int | Unset = UNSET
    timestamp_ms: int | Unset = UNSET
    timezone_id: int | Unset = UNSET
    game_clock: str | Unset = UNSET
    period: str | Unset = UNSET
    player_id: int | Unset = UNSET
    distance: float | Unset = UNSET
    speed_ball: float | Unset = UNSET
    packing: float | Unset = UNSET
    receiving_player_id: float | Unset = UNSET
    verticality: float | Unset = UNSET
    horizontality: float | Unset = UNSET
    trajectory: str | Unset = UNSET
    type_: EventDetectedPassType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        distance = self.distance

        speed_ball = self.speed_ball

        packing = self.packing

        receiving_player_id = self.receiving_player_id

        verticality = self.verticality

        horizontality = self.horizontality

        trajectory = self.trajectory

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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
        if speed_ball is not UNSET:
            field_dict["speed_ball"] = speed_ball
        if packing is not UNSET:
            field_dict["packing"] = packing
        if receiving_player_id is not UNSET:
            field_dict["receiving_player_id"] = receiving_player_id
        if verticality is not UNSET:
            field_dict["verticality"] = verticality
        if horizontality is not UNSET:
            field_dict["horizontality"] = horizontality
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if type_ is not UNSET:
            field_dict["type"] = type_

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

        speed_ball = d.pop("speed_ball", UNSET)

        packing = d.pop("packing", UNSET)

        receiving_player_id = d.pop("receiving_player_id", UNSET)

        verticality = d.pop("verticality", UNSET)

        horizontality = d.pop("horizontality", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: EventDetectedPassType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EventDetectedPassType(_type_)

        event_detected_pass = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            distance=distance,
            speed_ball=speed_ball,
            packing=packing,
            receiving_player_id=receiving_player_id,
            verticality=verticality,
            horizontality=horizontality,
            trajectory=trajectory,
            type_=type_,
        )

        event_detected_pass.additional_properties = d
        return event_detected_pass

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
