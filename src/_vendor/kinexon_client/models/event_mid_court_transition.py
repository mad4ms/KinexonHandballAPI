from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_mid_court_transition_mct_category import EventMidCourtTransitionMctCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventMidCourtTransition")


@_attrs_define
class EventMidCourtTransition:
    """
    Attributes:
        timestamp (int | Unset):
        timestamp_ms (int | Unset):
        timezone_id (int | Unset):
        game_clock (str | Unset):
        period (str | Unset):
        player_id (int | Unset):
        intensity (float | Unset):
        transitioned_court_length (float | Unset):
        trajectory_length (float | Unset):
        acceleration_max (float | Unset):
        speed_max (float | Unset):
        metabolic_work (float | Unset):
        accel_load_accum (float | Unset):
        direction (float | Unset):
        sequence_length (float | Unset):
        period_time (float | Unset):
        trajectory (str | Unset):
        mct_category (EventMidCourtTransitionMctCategory | Unset):
    """

    timestamp: int | Unset = UNSET
    timestamp_ms: int | Unset = UNSET
    timezone_id: int | Unset = UNSET
    game_clock: str | Unset = UNSET
    period: str | Unset = UNSET
    player_id: int | Unset = UNSET
    intensity: float | Unset = UNSET
    transitioned_court_length: float | Unset = UNSET
    trajectory_length: float | Unset = UNSET
    acceleration_max: float | Unset = UNSET
    speed_max: float | Unset = UNSET
    metabolic_work: float | Unset = UNSET
    accel_load_accum: float | Unset = UNSET
    direction: float | Unset = UNSET
    sequence_length: float | Unset = UNSET
    period_time: float | Unset = UNSET
    trajectory: str | Unset = UNSET
    mct_category: EventMidCourtTransitionMctCategory | Unset = UNSET
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

        sequence_length = self.sequence_length

        period_time = self.period_time

        trajectory = self.trajectory

        mct_category: str | Unset = UNSET
        if not isinstance(self.mct_category, Unset):
            mct_category = self.mct_category.value

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
        if sequence_length is not UNSET:
            field_dict["sequence_length"] = sequence_length
        if period_time is not UNSET:
            field_dict["period_time"] = period_time
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if mct_category is not UNSET:
            field_dict["mct_category"] = mct_category

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

        sequence_length = d.pop("sequence_length", UNSET)

        period_time = d.pop("period_time", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _mct_category = d.pop("mct_category", UNSET)
        mct_category: EventMidCourtTransitionMctCategory | Unset
        if isinstance(_mct_category, Unset):
            mct_category = UNSET
        else:
            mct_category = EventMidCourtTransitionMctCategory(_mct_category)

        event_mid_court_transition = cls(
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
            sequence_length=sequence_length,
            period_time=period_time,
            trajectory=trajectory,
            mct_category=mct_category,
        )

        event_mid_court_transition.additional_properties = d
        return event_mid_court_transition

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
