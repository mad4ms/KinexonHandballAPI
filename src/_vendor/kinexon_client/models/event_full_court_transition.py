from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_full_court_transition_fct_category import (
    EventFullCourtTransitionFctCategory,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventFullCourtTransition")


@_attrs_define
class EventFullCourtTransition:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        intensity (Union[Unset, float]):
        transitioned_court_length (Union[Unset, float]):
        trajectory_length (Union[Unset, float]):
        acceleration_max (Union[Unset, float]):
        speed_max (Union[Unset, float]):
        metabolic_work (Union[Unset, float]):
        accel_load_accum (Union[Unset, float]):
        direction (Union[Unset, float]):
        trajectory (Union[Unset, str]):
        fct_category (Union[Unset, EventFullCourtTransitionFctCategory]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    intensity: Union[Unset, float] = UNSET
    transitioned_court_length: Union[Unset, float] = UNSET
    trajectory_length: Union[Unset, float] = UNSET
    acceleration_max: Union[Unset, float] = UNSET
    speed_max: Union[Unset, float] = UNSET
    metabolic_work: Union[Unset, float] = UNSET
    accel_load_accum: Union[Unset, float] = UNSET
    direction: Union[Unset, float] = UNSET
    trajectory: Union[Unset, str] = UNSET
    fct_category: Union[Unset, EventFullCourtTransitionFctCategory] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        intensity = self.intensity

        transitioned_court_length = self.transitioned_court_length

        trajectory_length = self.trajectory_length

        acceleration_max = self.acceleration_max

        speed_max = self.speed_max

        metabolic_work = self.metabolic_work

        accel_load_accum = self.accel_load_accum

        direction = self.direction

        trajectory = self.trajectory

        fct_category: Union[Unset, str] = UNSET
        if not isinstance(self.fct_category, Unset):
            fct_category = self.fct_category.value

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
        if intensity is not UNSET:
            field_dict["intensity"] = intensity
        if transitioned_court_length is not UNSET:
            field_dict["transitioned_court_length"] = transitioned_court_length
        if trajectory_length is not UNSET:
            field_dict["trajectory_length"] = trajectory_length
        if acceleration_max is not UNSET:
            field_dict["acceleration_max"] = acceleration_max
        if speed_max is not UNSET:
            field_dict["speed_max"] = speed_max
        if metabolic_work is not UNSET:
            field_dict["metabolic_work"] = metabolic_work
        if accel_load_accum is not UNSET:
            field_dict["accel_load_accum"] = accel_load_accum
        if direction is not UNSET:
            field_dict["direction"] = direction
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if fct_category is not UNSET:
            field_dict["fct_category"] = fct_category

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

        intensity = d.pop("intensity", UNSET)

        transitioned_court_length = d.pop("transitioned_court_length", UNSET)

        trajectory_length = d.pop("trajectory_length", UNSET)

        acceleration_max = d.pop("acceleration_max", UNSET)

        speed_max = d.pop("speed_max", UNSET)

        metabolic_work = d.pop("metabolic_work", UNSET)

        accel_load_accum = d.pop("accel_load_accum", UNSET)

        direction = d.pop("direction", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _fct_category = d.pop("fct_category", UNSET)
        fct_category: Union[Unset, EventFullCourtTransitionFctCategory]
        if isinstance(_fct_category, Unset):
            fct_category = UNSET
        else:
            fct_category = EventFullCourtTransitionFctCategory(_fct_category)

        event_full_court_transition = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            intensity=intensity,
            transitioned_court_length=transitioned_court_length,
            trajectory_length=trajectory_length,
            acceleration_max=acceleration_max,
            speed_max=speed_max,
            metabolic_work=metabolic_work,
            accel_load_accum=accel_load_accum,
            direction=direction,
            trajectory=trajectory,
            fct_category=fct_category,
        )

        event_full_court_transition.additional_properties = d
        return event_full_court_transition

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
