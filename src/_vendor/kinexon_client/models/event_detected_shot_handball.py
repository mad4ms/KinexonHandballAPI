from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDetectedShotHandball")


@_attrs_define
class EventDetectedShotHandball:
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
        trajectory (str | Unset):
        shot_position_x (float | Unset):
        shot_position_y (float | Unset):
        hit_position_y (float | Unset):
        hit_position_z (float | Unset):
        success (float | Unset):
        shot_category (str | Unset):
        goalkeeper_id (float | Unset):
        shot_type (float | Unset):
        assisting_player_id (float | Unset):
        validated (float | Unset):
    """

    timestamp: int | Unset = UNSET
    timestamp_ms: int | Unset = UNSET
    timezone_id: int | Unset = UNSET
    game_clock: str | Unset = UNSET
    period: str | Unset = UNSET
    player_id: int | Unset = UNSET
    distance: float | Unset = UNSET
    speed_ball: float | Unset = UNSET
    trajectory: str | Unset = UNSET
    shot_position_x: float | Unset = UNSET
    shot_position_y: float | Unset = UNSET
    hit_position_y: float | Unset = UNSET
    hit_position_z: float | Unset = UNSET
    success: float | Unset = UNSET
    shot_category: str | Unset = UNSET
    goalkeeper_id: float | Unset = UNSET
    shot_type: float | Unset = UNSET
    assisting_player_id: float | Unset = UNSET
    validated: float | Unset = UNSET
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

        trajectory = self.trajectory

        shot_position_x = self.shot_position_x

        shot_position_y = self.shot_position_y

        hit_position_y = self.hit_position_y

        hit_position_z = self.hit_position_z

        success = self.success

        shot_category = self.shot_category

        goalkeeper_id = self.goalkeeper_id

        shot_type = self.shot_type

        assisting_player_id = self.assisting_player_id

        validated = self.validated

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
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if shot_position_x is not UNSET:
            field_dict["shot_position_x"] = shot_position_x
        if shot_position_y is not UNSET:
            field_dict["shot_position_y"] = shot_position_y
        if hit_position_y is not UNSET:
            field_dict["hit_position_y"] = hit_position_y
        if hit_position_z is not UNSET:
            field_dict["hit_position_z"] = hit_position_z
        if success is not UNSET:
            field_dict["success"] = success
        if shot_category is not UNSET:
            field_dict["shot_category"] = shot_category
        if goalkeeper_id is not UNSET:
            field_dict["goalkeeper_id"] = goalkeeper_id
        if shot_type is not UNSET:
            field_dict["shot_type"] = shot_type
        if assisting_player_id is not UNSET:
            field_dict["assisting_player_id"] = assisting_player_id
        if validated is not UNSET:
            field_dict["validated"] = validated

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

        trajectory = d.pop("trajectory", UNSET)

        shot_position_x = d.pop("shot_position_x", UNSET)

        shot_position_y = d.pop("shot_position_y", UNSET)

        hit_position_y = d.pop("hit_position_y", UNSET)

        hit_position_z = d.pop("hit_position_z", UNSET)

        success = d.pop("success", UNSET)

        shot_category = d.pop("shot_category", UNSET)

        goalkeeper_id = d.pop("goalkeeper_id", UNSET)

        shot_type = d.pop("shot_type", UNSET)

        assisting_player_id = d.pop("assisting_player_id", UNSET)

        validated = d.pop("validated", UNSET)

        event_detected_shot_handball = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            distance=distance,
            speed_ball=speed_ball,
            trajectory=trajectory,
            shot_position_x=shot_position_x,
            shot_position_y=shot_position_y,
            hit_position_y=hit_position_y,
            hit_position_z=hit_position_z,
            success=success,
            shot_category=shot_category,
            goalkeeper_id=goalkeeper_id,
            shot_type=shot_type,
            assisting_player_id=assisting_player_id,
            validated=validated,
        )

        event_detected_shot_handball.additional_properties = d
        return event_detected_shot_handball

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
