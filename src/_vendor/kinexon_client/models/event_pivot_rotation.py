from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_pivot_rotation_direction import EventPivotRotationDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventPivotRotation")


@_attrs_define
class EventPivotRotation:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        magnitude (Union[Unset, float]):
        rotation_speed (Union[Unset, float]):
        trajectory (Union[Unset, str]):
        direction (Union[Unset, EventPivotRotationDirection]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    magnitude: Union[Unset, float] = UNSET
    rotation_speed: Union[Unset, float] = UNSET
    trajectory: Union[Unset, str] = UNSET
    direction: Union[Unset, EventPivotRotationDirection] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        magnitude = self.magnitude

        rotation_speed = self.rotation_speed

        trajectory = self.trajectory

        direction: Union[Unset, str] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

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
        if magnitude is not UNSET:
            field_dict["magnitude"] = magnitude
        if rotation_speed is not UNSET:
            field_dict["rotation_speed"] = rotation_speed
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if direction is not UNSET:
            field_dict["direction"] = direction

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

        magnitude = d.pop("magnitude", UNSET)

        rotation_speed = d.pop("rotation_speed", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, EventPivotRotationDirection]
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = EventPivotRotationDirection(_direction)

        event_pivot_rotation = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            magnitude=magnitude,
            rotation_speed=rotation_speed,
            trajectory=trajectory,
            direction=direction,
        )

        event_pivot_rotation.additional_properties = d
        return event_pivot_rotation

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
