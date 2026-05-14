from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerStatistic")


@_attrs_define
class PlayerStatistic:
    """
    Attributes:
        speed_avg (float | Unset): m/s Example: 2.4.
        accel_avg (float | Unset): m/s² Example: 2.3.
        accel_load_avg (float | Unset):  Example: 4.5.
        accel_load_accum_avg_per_minute (float | Unset): float Example: 2.1.
        load_acceleration_load_category1_avg_per_minute (float | Unset):  Example: 20.
        load_acceleration_load_category2_avg_per_minute (float | Unset):  Example: 20.
        load_acceleration_load_category3_avg_per_minute (float | Unset):  Example: 20.
        load_acceleration_load_category4_avg_per_minute (float | Unset):  Example: 20.
        load_acceleration_load_category5_avg_per_minute (float | Unset):  Example: 20.
        load_acceleration_load_category6_avg_per_minute (float | Unset):  Example: 20.
        load_acceleration_load_category7_avg_per_minute (float | Unset):  Example: 20.
        step_balance_avg (float | Unset): % Example: 40.
        metabolic_power_avg (float | Unset):  Example: 280.
        metabolic_power_per_mass_avg (float | Unset): W/kg Example: 3.9.
        distance_total_avg_per_minute (float | Unset): m Example: 20.
        distance_speed_category1_avg_per_minute (float | Unset): m Example: 120.
        distance_speed_category2_avg_per_minute (float | Unset): m Example: 120.
        distance_speed_category3_avg_per_minute (float | Unset): m Example: 120.
        distance_speed_category4_avg_per_minute (float | Unset): m Example: 120.
        distance_speed_category5_avg_per_minute (float | Unset): m Example: 120.
        distance_speed_category6_avg_per_minute (float | Unset): m Example: 120.
        distance_speed_category7_avg_per_minute (float | Unset): m Example: 120.
        distance_total_relative_avg_per_minute (float | Unset): m Example: 20.
        distance_speed_relative_category1_avg_per_minute (float | Unset): m Example: 120.
        distance_speed_relative_category2_avg_per_minute (float | Unset): m Example: 120.
        distance_speed_relative_category3_avg_per_minute (float | Unset): m Example: 120.
        distance_speed_relative_category4_avg_per_minute (float | Unset): m Example: 120.
        distance_speed_relative_category5_avg_per_minute (float | Unset): m Example: 120.
        distance_speed_relative_category6_avg_per_minute (float | Unset): m Example: 120.
        distance_speed_relative_category7_avg_per_minute (float | Unset): m Example: 120.
        distance_high_metabolic_load_avg_per_minute (float | Unset): m Example: 4.2.
        distance_high_metabolic_power_avg_per_minute (float | Unset): m Example: 4.2.
        distance_from_steps_avg_per_minute (float | Unset): m Example: 20.
        metabolic_work_avg_per_minute (float | Unset): kcal Example: 9.9.
        jump_load_avg_per_minute (float | Unset): J Example: 2.1.
        jump_load_per_mass_avg_per_minute (float | Unset): J/kg Example: 2.1.
        physio_intensity (float | Unset): physio_load/total_time
        mechanical_intensity (float | Unset): mechanical_load/total_time
        mechanical_accel_total_avg_per_minute (float | Unset):  Example: 2.1.
        mechanical_accel_category1_avg_per_minute (float | Unset):  Example: 1.2.
        mechanical_accel_category2_avg_per_minute (float | Unset):  Example: 1.2.
        mechanical_accel_category3_avg_per_minute (float | Unset):  Example: 1.2.
        mechanical_accel_category4_avg_per_minute (float | Unset):  Example: 1.2.
        mechanical_decel_total_avg_per_minute (float | Unset):  Example: 1.2.
        mechanical_decel_category1_avg_per_minute (float | Unset):  Example: 1.2.
        mechanical_decel_category2_avg_per_minute (float | Unset):  Example: 1.2.
        mechanical_decel_category3_avg_per_minute (float | Unset):  Example: 1.2.
        mechanical_decel_category4_avg_per_minute (float | Unset):  Example: 1.2.
        mechanical_intensity_offence (float | Unset):  Example: 20.
        mechanical_intensity_defence (float | Unset):  Example: 20.
        playoff_load (float | Unset):  Example: 120.
        human_core_temperature_avg (float | Unset): °C Example: 37.6.
        ball_contact_count_avg_per_minute (float | Unset): float Example: 2.1.
        distance_total_skating_avg_per_minute (float | Unset): m Example: 20.
        distance_skating_speed_category1_avg_per_minute (float | Unset):  Example: 1.2.
        distance_skating_speed_category2_avg_per_minute (float | Unset):  Example: 1.2.
        distance_skating_speed_category3_avg_per_minute (float | Unset):  Example: 1.2.
        distance_skating_speed_category4_avg_per_minute (float | Unset):  Example: 1.2.
        distance_skating_speed_category5_avg_per_minute (float | Unset):  Example: 1.2.
        distance_skating_speed_category6_avg_per_minute (float | Unset):  Example: 1.2.
        distance_skating_speed_category7_avg_per_minute (float | Unset):  Example: 1.2.
        distance_total_gliding_avg_per_minute (float | Unset): m Example: 20.
        distance_gliding_speed_category1_avg_per_minute (float | Unset):  Example: 1.2.
        distance_gliding_speed_category2_avg_per_minute (float | Unset):  Example: 1.2.
        distance_gliding_speed_category3_avg_per_minute (float | Unset):  Example: 1.2.
        distance_gliding_speed_category4_avg_per_minute (float | Unset):  Example: 1.2.
        distance_gliding_speed_category5_avg_per_minute (float | Unset):  Example: 1.2.
        distance_gliding_speed_category6_avg_per_minute (float | Unset):  Example: 1.2.
        distance_gliding_speed_category7_avg_per_minute (float | Unset):  Example: 1.2.
        imu_missing_recording_ratio (float | Unset):  Example: 1.5.
    """

    speed_avg: float | Unset = UNSET
    accel_avg: float | Unset = UNSET
    accel_load_avg: float | Unset = UNSET
    accel_load_accum_avg_per_minute: float | Unset = UNSET
    load_acceleration_load_category1_avg_per_minute: float | Unset = UNSET
    load_acceleration_load_category2_avg_per_minute: float | Unset = UNSET
    load_acceleration_load_category3_avg_per_minute: float | Unset = UNSET
    load_acceleration_load_category4_avg_per_minute: float | Unset = UNSET
    load_acceleration_load_category5_avg_per_minute: float | Unset = UNSET
    load_acceleration_load_category6_avg_per_minute: float | Unset = UNSET
    load_acceleration_load_category7_avg_per_minute: float | Unset = UNSET
    step_balance_avg: float | Unset = UNSET
    metabolic_power_avg: float | Unset = UNSET
    metabolic_power_per_mass_avg: float | Unset = UNSET
    distance_total_avg_per_minute: float | Unset = UNSET
    distance_speed_category1_avg_per_minute: float | Unset = UNSET
    distance_speed_category2_avg_per_minute: float | Unset = UNSET
    distance_speed_category3_avg_per_minute: float | Unset = UNSET
    distance_speed_category4_avg_per_minute: float | Unset = UNSET
    distance_speed_category5_avg_per_minute: float | Unset = UNSET
    distance_speed_category6_avg_per_minute: float | Unset = UNSET
    distance_speed_category7_avg_per_minute: float | Unset = UNSET
    distance_total_relative_avg_per_minute: float | Unset = UNSET
    distance_speed_relative_category1_avg_per_minute: float | Unset = UNSET
    distance_speed_relative_category2_avg_per_minute: float | Unset = UNSET
    distance_speed_relative_category3_avg_per_minute: float | Unset = UNSET
    distance_speed_relative_category4_avg_per_minute: float | Unset = UNSET
    distance_speed_relative_category5_avg_per_minute: float | Unset = UNSET
    distance_speed_relative_category6_avg_per_minute: float | Unset = UNSET
    distance_speed_relative_category7_avg_per_minute: float | Unset = UNSET
    distance_high_metabolic_load_avg_per_minute: float | Unset = UNSET
    distance_high_metabolic_power_avg_per_minute: float | Unset = UNSET
    distance_from_steps_avg_per_minute: float | Unset = UNSET
    metabolic_work_avg_per_minute: float | Unset = UNSET
    jump_load_avg_per_minute: float | Unset = UNSET
    jump_load_per_mass_avg_per_minute: float | Unset = UNSET
    physio_intensity: float | Unset = UNSET
    mechanical_intensity: float | Unset = UNSET
    mechanical_accel_total_avg_per_minute: float | Unset = UNSET
    mechanical_accel_category1_avg_per_minute: float | Unset = UNSET
    mechanical_accel_category2_avg_per_minute: float | Unset = UNSET
    mechanical_accel_category3_avg_per_minute: float | Unset = UNSET
    mechanical_accel_category4_avg_per_minute: float | Unset = UNSET
    mechanical_decel_total_avg_per_minute: float | Unset = UNSET
    mechanical_decel_category1_avg_per_minute: float | Unset = UNSET
    mechanical_decel_category2_avg_per_minute: float | Unset = UNSET
    mechanical_decel_category3_avg_per_minute: float | Unset = UNSET
    mechanical_decel_category4_avg_per_minute: float | Unset = UNSET
    mechanical_intensity_offence: float | Unset = UNSET
    mechanical_intensity_defence: float | Unset = UNSET
    playoff_load: float | Unset = UNSET
    human_core_temperature_avg: float | Unset = UNSET
    ball_contact_count_avg_per_minute: float | Unset = UNSET
    distance_total_skating_avg_per_minute: float | Unset = UNSET
    distance_skating_speed_category1_avg_per_minute: float | Unset = UNSET
    distance_skating_speed_category2_avg_per_minute: float | Unset = UNSET
    distance_skating_speed_category3_avg_per_minute: float | Unset = UNSET
    distance_skating_speed_category4_avg_per_minute: float | Unset = UNSET
    distance_skating_speed_category5_avg_per_minute: float | Unset = UNSET
    distance_skating_speed_category6_avg_per_minute: float | Unset = UNSET
    distance_skating_speed_category7_avg_per_minute: float | Unset = UNSET
    distance_total_gliding_avg_per_minute: float | Unset = UNSET
    distance_gliding_speed_category1_avg_per_minute: float | Unset = UNSET
    distance_gliding_speed_category2_avg_per_minute: float | Unset = UNSET
    distance_gliding_speed_category3_avg_per_minute: float | Unset = UNSET
    distance_gliding_speed_category4_avg_per_minute: float | Unset = UNSET
    distance_gliding_speed_category5_avg_per_minute: float | Unset = UNSET
    distance_gliding_speed_category6_avg_per_minute: float | Unset = UNSET
    distance_gliding_speed_category7_avg_per_minute: float | Unset = UNSET
    imu_missing_recording_ratio: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        speed_avg = self.speed_avg

        accel_avg = self.accel_avg

        accel_load_avg = self.accel_load_avg

        accel_load_accum_avg_per_minute = self.accel_load_accum_avg_per_minute

        load_acceleration_load_category1_avg_per_minute = self.load_acceleration_load_category1_avg_per_minute

        load_acceleration_load_category2_avg_per_minute = self.load_acceleration_load_category2_avg_per_minute

        load_acceleration_load_category3_avg_per_minute = self.load_acceleration_load_category3_avg_per_minute

        load_acceleration_load_category4_avg_per_minute = self.load_acceleration_load_category4_avg_per_minute

        load_acceleration_load_category5_avg_per_minute = self.load_acceleration_load_category5_avg_per_minute

        load_acceleration_load_category6_avg_per_minute = self.load_acceleration_load_category6_avg_per_minute

        load_acceleration_load_category7_avg_per_minute = self.load_acceleration_load_category7_avg_per_minute

        step_balance_avg = self.step_balance_avg

        metabolic_power_avg = self.metabolic_power_avg

        metabolic_power_per_mass_avg = self.metabolic_power_per_mass_avg

        distance_total_avg_per_minute = self.distance_total_avg_per_minute

        distance_speed_category1_avg_per_minute = self.distance_speed_category1_avg_per_minute

        distance_speed_category2_avg_per_minute = self.distance_speed_category2_avg_per_minute

        distance_speed_category3_avg_per_minute = self.distance_speed_category3_avg_per_minute

        distance_speed_category4_avg_per_minute = self.distance_speed_category4_avg_per_minute

        distance_speed_category5_avg_per_minute = self.distance_speed_category5_avg_per_minute

        distance_speed_category6_avg_per_minute = self.distance_speed_category6_avg_per_minute

        distance_speed_category7_avg_per_minute = self.distance_speed_category7_avg_per_minute

        distance_total_relative_avg_per_minute = self.distance_total_relative_avg_per_minute

        distance_speed_relative_category1_avg_per_minute = self.distance_speed_relative_category1_avg_per_minute

        distance_speed_relative_category2_avg_per_minute = self.distance_speed_relative_category2_avg_per_minute

        distance_speed_relative_category3_avg_per_minute = self.distance_speed_relative_category3_avg_per_minute

        distance_speed_relative_category4_avg_per_minute = self.distance_speed_relative_category4_avg_per_minute

        distance_speed_relative_category5_avg_per_minute = self.distance_speed_relative_category5_avg_per_minute

        distance_speed_relative_category6_avg_per_minute = self.distance_speed_relative_category6_avg_per_minute

        distance_speed_relative_category7_avg_per_minute = self.distance_speed_relative_category7_avg_per_minute

        distance_high_metabolic_load_avg_per_minute = self.distance_high_metabolic_load_avg_per_minute

        distance_high_metabolic_power_avg_per_minute = self.distance_high_metabolic_power_avg_per_minute

        distance_from_steps_avg_per_minute = self.distance_from_steps_avg_per_minute

        metabolic_work_avg_per_minute = self.metabolic_work_avg_per_minute

        jump_load_avg_per_minute = self.jump_load_avg_per_minute

        jump_load_per_mass_avg_per_minute = self.jump_load_per_mass_avg_per_minute

        physio_intensity = self.physio_intensity

        mechanical_intensity = self.mechanical_intensity

        mechanical_accel_total_avg_per_minute = self.mechanical_accel_total_avg_per_minute

        mechanical_accel_category1_avg_per_minute = self.mechanical_accel_category1_avg_per_minute

        mechanical_accel_category2_avg_per_minute = self.mechanical_accel_category2_avg_per_minute

        mechanical_accel_category3_avg_per_minute = self.mechanical_accel_category3_avg_per_minute

        mechanical_accel_category4_avg_per_minute = self.mechanical_accel_category4_avg_per_minute

        mechanical_decel_total_avg_per_minute = self.mechanical_decel_total_avg_per_minute

        mechanical_decel_category1_avg_per_minute = self.mechanical_decel_category1_avg_per_minute

        mechanical_decel_category2_avg_per_minute = self.mechanical_decel_category2_avg_per_minute

        mechanical_decel_category3_avg_per_minute = self.mechanical_decel_category3_avg_per_minute

        mechanical_decel_category4_avg_per_minute = self.mechanical_decel_category4_avg_per_minute

        mechanical_intensity_offence = self.mechanical_intensity_offence

        mechanical_intensity_defence = self.mechanical_intensity_defence

        playoff_load = self.playoff_load

        human_core_temperature_avg = self.human_core_temperature_avg

        ball_contact_count_avg_per_minute = self.ball_contact_count_avg_per_minute

        distance_total_skating_avg_per_minute = self.distance_total_skating_avg_per_minute

        distance_skating_speed_category1_avg_per_minute = self.distance_skating_speed_category1_avg_per_minute

        distance_skating_speed_category2_avg_per_minute = self.distance_skating_speed_category2_avg_per_minute

        distance_skating_speed_category3_avg_per_minute = self.distance_skating_speed_category3_avg_per_minute

        distance_skating_speed_category4_avg_per_minute = self.distance_skating_speed_category4_avg_per_minute

        distance_skating_speed_category5_avg_per_minute = self.distance_skating_speed_category5_avg_per_minute

        distance_skating_speed_category6_avg_per_minute = self.distance_skating_speed_category6_avg_per_minute

        distance_skating_speed_category7_avg_per_minute = self.distance_skating_speed_category7_avg_per_minute

        distance_total_gliding_avg_per_minute = self.distance_total_gliding_avg_per_minute

        distance_gliding_speed_category1_avg_per_minute = self.distance_gliding_speed_category1_avg_per_minute

        distance_gliding_speed_category2_avg_per_minute = self.distance_gliding_speed_category2_avg_per_minute

        distance_gliding_speed_category3_avg_per_minute = self.distance_gliding_speed_category3_avg_per_minute

        distance_gliding_speed_category4_avg_per_minute = self.distance_gliding_speed_category4_avg_per_minute

        distance_gliding_speed_category5_avg_per_minute = self.distance_gliding_speed_category5_avg_per_minute

        distance_gliding_speed_category6_avg_per_minute = self.distance_gliding_speed_category6_avg_per_minute

        distance_gliding_speed_category7_avg_per_minute = self.distance_gliding_speed_category7_avg_per_minute

        imu_missing_recording_ratio = self.imu_missing_recording_ratio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if speed_avg is not UNSET:
            field_dict["speed_avg"] = speed_avg
        if accel_avg is not UNSET:
            field_dict["accel_avg"] = accel_avg
        if accel_load_avg is not UNSET:
            field_dict["accel_load_avg"] = accel_load_avg
        if accel_load_accum_avg_per_minute is not UNSET:
            field_dict["accel_load_accum_avg_per_minute"] = accel_load_accum_avg_per_minute
        if load_acceleration_load_category1_avg_per_minute is not UNSET:
            field_dict["load_acceleration_load_category1_avg_per_minute"] = (
                load_acceleration_load_category1_avg_per_minute
            )
        if load_acceleration_load_category2_avg_per_minute is not UNSET:
            field_dict["load_acceleration_load_category2_avg_per_minute"] = (
                load_acceleration_load_category2_avg_per_minute
            )
        if load_acceleration_load_category3_avg_per_minute is not UNSET:
            field_dict["load_acceleration_load_category3_avg_per_minute"] = (
                load_acceleration_load_category3_avg_per_minute
            )
        if load_acceleration_load_category4_avg_per_minute is not UNSET:
            field_dict["load_acceleration_load_category4_avg_per_minute"] = (
                load_acceleration_load_category4_avg_per_minute
            )
        if load_acceleration_load_category5_avg_per_minute is not UNSET:
            field_dict["load_acceleration_load_category5_avg_per_minute"] = (
                load_acceleration_load_category5_avg_per_minute
            )
        if load_acceleration_load_category6_avg_per_minute is not UNSET:
            field_dict["load_acceleration_load_category6_avg_per_minute"] = (
                load_acceleration_load_category6_avg_per_minute
            )
        if load_acceleration_load_category7_avg_per_minute is not UNSET:
            field_dict["load_acceleration_load_category7_avg_per_minute"] = (
                load_acceleration_load_category7_avg_per_minute
            )
        if step_balance_avg is not UNSET:
            field_dict["step_balance_avg"] = step_balance_avg
        if metabolic_power_avg is not UNSET:
            field_dict["metabolic_power_avg"] = metabolic_power_avg
        if metabolic_power_per_mass_avg is not UNSET:
            field_dict["metabolic_power_per_mass_avg"] = metabolic_power_per_mass_avg
        if distance_total_avg_per_minute is not UNSET:
            field_dict["distance_total_avg_per_minute"] = distance_total_avg_per_minute
        if distance_speed_category1_avg_per_minute is not UNSET:
            field_dict["distance_speed_category1_avg_per_minute"] = distance_speed_category1_avg_per_minute
        if distance_speed_category2_avg_per_minute is not UNSET:
            field_dict["distance_speed_category2_avg_per_minute"] = distance_speed_category2_avg_per_minute
        if distance_speed_category3_avg_per_minute is not UNSET:
            field_dict["distance_speed_category3_avg_per_minute"] = distance_speed_category3_avg_per_minute
        if distance_speed_category4_avg_per_minute is not UNSET:
            field_dict["distance_speed_category4_avg_per_minute"] = distance_speed_category4_avg_per_minute
        if distance_speed_category5_avg_per_minute is not UNSET:
            field_dict["distance_speed_category5_avg_per_minute"] = distance_speed_category5_avg_per_minute
        if distance_speed_category6_avg_per_minute is not UNSET:
            field_dict["distance_speed_category6_avg_per_minute"] = distance_speed_category6_avg_per_minute
        if distance_speed_category7_avg_per_minute is not UNSET:
            field_dict["distance_speed_category7_avg_per_minute"] = distance_speed_category7_avg_per_minute
        if distance_total_relative_avg_per_minute is not UNSET:
            field_dict["distance_total_relative_avg_per_minute"] = distance_total_relative_avg_per_minute
        if distance_speed_relative_category1_avg_per_minute is not UNSET:
            field_dict["distance_speed_relative_category1_avg_per_minute"] = (
                distance_speed_relative_category1_avg_per_minute
            )
        if distance_speed_relative_category2_avg_per_minute is not UNSET:
            field_dict["distance_speed_relative_category2_avg_per_minute"] = (
                distance_speed_relative_category2_avg_per_minute
            )
        if distance_speed_relative_category3_avg_per_minute is not UNSET:
            field_dict["distance_speed_relative_category3_avg_per_minute"] = (
                distance_speed_relative_category3_avg_per_minute
            )
        if distance_speed_relative_category4_avg_per_minute is not UNSET:
            field_dict["distance_speed_relative_category4_avg_per_minute"] = (
                distance_speed_relative_category4_avg_per_minute
            )
        if distance_speed_relative_category5_avg_per_minute is not UNSET:
            field_dict["distance_speed_relative_category5_avg_per_minute"] = (
                distance_speed_relative_category5_avg_per_minute
            )
        if distance_speed_relative_category6_avg_per_minute is not UNSET:
            field_dict["distance_speed_relative_category6_avg_per_minute"] = (
                distance_speed_relative_category6_avg_per_minute
            )
        if distance_speed_relative_category7_avg_per_minute is not UNSET:
            field_dict["distance_speed_relative_category7_avg_per_minute"] = (
                distance_speed_relative_category7_avg_per_minute
            )
        if distance_high_metabolic_load_avg_per_minute is not UNSET:
            field_dict["distance_high_metabolic_load_avg_per_minute"] = distance_high_metabolic_load_avg_per_minute
        if distance_high_metabolic_power_avg_per_minute is not UNSET:
            field_dict["distance_high_metabolic_power_avg_per_minute"] = distance_high_metabolic_power_avg_per_minute
        if distance_from_steps_avg_per_minute is not UNSET:
            field_dict["distance_from_steps_avg_per_minute"] = distance_from_steps_avg_per_minute
        if metabolic_work_avg_per_minute is not UNSET:
            field_dict["metabolic_work_avg_per_minute"] = metabolic_work_avg_per_minute
        if jump_load_avg_per_minute is not UNSET:
            field_dict["jump_load_avg_per_minute"] = jump_load_avg_per_minute
        if jump_load_per_mass_avg_per_minute is not UNSET:
            field_dict["jump_load_per_mass_avg_per_minute"] = jump_load_per_mass_avg_per_minute
        if physio_intensity is not UNSET:
            field_dict["physio_intensity"] = physio_intensity
        if mechanical_intensity is not UNSET:
            field_dict["mechanical_intensity"] = mechanical_intensity
        if mechanical_accel_total_avg_per_minute is not UNSET:
            field_dict["mechanical_accel_total_avg_per_minute"] = mechanical_accel_total_avg_per_minute
        if mechanical_accel_category1_avg_per_minute is not UNSET:
            field_dict["mechanical_accel_category1_avg_per_minute"] = mechanical_accel_category1_avg_per_minute
        if mechanical_accel_category2_avg_per_minute is not UNSET:
            field_dict["mechanical_accel_category2_avg_per_minute"] = mechanical_accel_category2_avg_per_minute
        if mechanical_accel_category3_avg_per_minute is not UNSET:
            field_dict["mechanical_accel_category3_avg_per_minute"] = mechanical_accel_category3_avg_per_minute
        if mechanical_accel_category4_avg_per_minute is not UNSET:
            field_dict["mechanical_accel_category4_avg_per_minute"] = mechanical_accel_category4_avg_per_minute
        if mechanical_decel_total_avg_per_minute is not UNSET:
            field_dict["mechanical_decel_total_avg_per_minute"] = mechanical_decel_total_avg_per_minute
        if mechanical_decel_category1_avg_per_minute is not UNSET:
            field_dict["mechanical_decel_category1_avg_per_minute"] = mechanical_decel_category1_avg_per_minute
        if mechanical_decel_category2_avg_per_minute is not UNSET:
            field_dict["mechanical_decel_category2_avg_per_minute"] = mechanical_decel_category2_avg_per_minute
        if mechanical_decel_category3_avg_per_minute is not UNSET:
            field_dict["mechanical_decel_category3_avg_per_minute"] = mechanical_decel_category3_avg_per_minute
        if mechanical_decel_category4_avg_per_minute is not UNSET:
            field_dict["mechanical_decel_category4_avg_per_minute"] = mechanical_decel_category4_avg_per_minute
        if mechanical_intensity_offence is not UNSET:
            field_dict["mechanical_intensity_offence"] = mechanical_intensity_offence
        if mechanical_intensity_defence is not UNSET:
            field_dict["mechanical_intensity_defence"] = mechanical_intensity_defence
        if playoff_load is not UNSET:
            field_dict["playoff_load"] = playoff_load
        if human_core_temperature_avg is not UNSET:
            field_dict["human_core_temperature_avg"] = human_core_temperature_avg
        if ball_contact_count_avg_per_minute is not UNSET:
            field_dict["ball_contact_count_avg_per_minute"] = ball_contact_count_avg_per_minute
        if distance_total_skating_avg_per_minute is not UNSET:
            field_dict["distance_total_skating_avg_per_minute"] = distance_total_skating_avg_per_minute
        if distance_skating_speed_category1_avg_per_minute is not UNSET:
            field_dict["distance_skating_speed_category1_avg_per_minute"] = (
                distance_skating_speed_category1_avg_per_minute
            )
        if distance_skating_speed_category2_avg_per_minute is not UNSET:
            field_dict["distance_skating_speed_category2_avg_per_minute"] = (
                distance_skating_speed_category2_avg_per_minute
            )
        if distance_skating_speed_category3_avg_per_minute is not UNSET:
            field_dict["distance_skating_speed_category3_avg_per_minute"] = (
                distance_skating_speed_category3_avg_per_minute
            )
        if distance_skating_speed_category4_avg_per_minute is not UNSET:
            field_dict["distance_skating_speed_category4_avg_per_minute"] = (
                distance_skating_speed_category4_avg_per_minute
            )
        if distance_skating_speed_category5_avg_per_minute is not UNSET:
            field_dict["distance_skating_speed_category5_avg_per_minute"] = (
                distance_skating_speed_category5_avg_per_minute
            )
        if distance_skating_speed_category6_avg_per_minute is not UNSET:
            field_dict["distance_skating_speed_category6_avg_per_minute"] = (
                distance_skating_speed_category6_avg_per_minute
            )
        if distance_skating_speed_category7_avg_per_minute is not UNSET:
            field_dict["distance_skating_speed_category7_avg_per_minute"] = (
                distance_skating_speed_category7_avg_per_minute
            )
        if distance_total_gliding_avg_per_minute is not UNSET:
            field_dict["distance_total_gliding_avg_per_minute"] = distance_total_gliding_avg_per_minute
        if distance_gliding_speed_category1_avg_per_minute is not UNSET:
            field_dict["distance_gliding_speed_category1_avg_per_minute"] = (
                distance_gliding_speed_category1_avg_per_minute
            )
        if distance_gliding_speed_category2_avg_per_minute is not UNSET:
            field_dict["distance_gliding_speed_category2_avg_per_minute"] = (
                distance_gliding_speed_category2_avg_per_minute
            )
        if distance_gliding_speed_category3_avg_per_minute is not UNSET:
            field_dict["distance_gliding_speed_category3_avg_per_minute"] = (
                distance_gliding_speed_category3_avg_per_minute
            )
        if distance_gliding_speed_category4_avg_per_minute is not UNSET:
            field_dict["distance_gliding_speed_category4_avg_per_minute"] = (
                distance_gliding_speed_category4_avg_per_minute
            )
        if distance_gliding_speed_category5_avg_per_minute is not UNSET:
            field_dict["distance_gliding_speed_category5_avg_per_minute"] = (
                distance_gliding_speed_category5_avg_per_minute
            )
        if distance_gliding_speed_category6_avg_per_minute is not UNSET:
            field_dict["distance_gliding_speed_category6_avg_per_minute"] = (
                distance_gliding_speed_category6_avg_per_minute
            )
        if distance_gliding_speed_category7_avg_per_minute is not UNSET:
            field_dict["distance_gliding_speed_category7_avg_per_minute"] = (
                distance_gliding_speed_category7_avg_per_minute
            )
        if imu_missing_recording_ratio is not UNSET:
            field_dict["imu_missing_recording_ratio"] = imu_missing_recording_ratio

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        speed_avg = d.pop("speed_avg", UNSET)

        accel_avg = d.pop("accel_avg", UNSET)

        accel_load_avg = d.pop("accel_load_avg", UNSET)

        accel_load_accum_avg_per_minute = d.pop("accel_load_accum_avg_per_minute", UNSET)

        load_acceleration_load_category1_avg_per_minute = d.pop(
            "load_acceleration_load_category1_avg_per_minute", UNSET
        )

        load_acceleration_load_category2_avg_per_minute = d.pop(
            "load_acceleration_load_category2_avg_per_minute", UNSET
        )

        load_acceleration_load_category3_avg_per_minute = d.pop(
            "load_acceleration_load_category3_avg_per_minute", UNSET
        )

        load_acceleration_load_category4_avg_per_minute = d.pop(
            "load_acceleration_load_category4_avg_per_minute", UNSET
        )

        load_acceleration_load_category5_avg_per_minute = d.pop(
            "load_acceleration_load_category5_avg_per_minute", UNSET
        )

        load_acceleration_load_category6_avg_per_minute = d.pop(
            "load_acceleration_load_category6_avg_per_minute", UNSET
        )

        load_acceleration_load_category7_avg_per_minute = d.pop(
            "load_acceleration_load_category7_avg_per_minute", UNSET
        )

        step_balance_avg = d.pop("step_balance_avg", UNSET)

        metabolic_power_avg = d.pop("metabolic_power_avg", UNSET)

        metabolic_power_per_mass_avg = d.pop("metabolic_power_per_mass_avg", UNSET)

        distance_total_avg_per_minute = d.pop("distance_total_avg_per_minute", UNSET)

        distance_speed_category1_avg_per_minute = d.pop("distance_speed_category1_avg_per_minute", UNSET)

        distance_speed_category2_avg_per_minute = d.pop("distance_speed_category2_avg_per_minute", UNSET)

        distance_speed_category3_avg_per_minute = d.pop("distance_speed_category3_avg_per_minute", UNSET)

        distance_speed_category4_avg_per_minute = d.pop("distance_speed_category4_avg_per_minute", UNSET)

        distance_speed_category5_avg_per_minute = d.pop("distance_speed_category5_avg_per_minute", UNSET)

        distance_speed_category6_avg_per_minute = d.pop("distance_speed_category6_avg_per_minute", UNSET)

        distance_speed_category7_avg_per_minute = d.pop("distance_speed_category7_avg_per_minute", UNSET)

        distance_total_relative_avg_per_minute = d.pop("distance_total_relative_avg_per_minute", UNSET)

        distance_speed_relative_category1_avg_per_minute = d.pop(
            "distance_speed_relative_category1_avg_per_minute", UNSET
        )

        distance_speed_relative_category2_avg_per_minute = d.pop(
            "distance_speed_relative_category2_avg_per_minute", UNSET
        )

        distance_speed_relative_category3_avg_per_minute = d.pop(
            "distance_speed_relative_category3_avg_per_minute", UNSET
        )

        distance_speed_relative_category4_avg_per_minute = d.pop(
            "distance_speed_relative_category4_avg_per_minute", UNSET
        )

        distance_speed_relative_category5_avg_per_minute = d.pop(
            "distance_speed_relative_category5_avg_per_minute", UNSET
        )

        distance_speed_relative_category6_avg_per_minute = d.pop(
            "distance_speed_relative_category6_avg_per_minute", UNSET
        )

        distance_speed_relative_category7_avg_per_minute = d.pop(
            "distance_speed_relative_category7_avg_per_minute", UNSET
        )

        distance_high_metabolic_load_avg_per_minute = d.pop("distance_high_metabolic_load_avg_per_minute", UNSET)

        distance_high_metabolic_power_avg_per_minute = d.pop("distance_high_metabolic_power_avg_per_minute", UNSET)

        distance_from_steps_avg_per_minute = d.pop("distance_from_steps_avg_per_minute", UNSET)

        metabolic_work_avg_per_minute = d.pop("metabolic_work_avg_per_minute", UNSET)

        jump_load_avg_per_minute = d.pop("jump_load_avg_per_minute", UNSET)

        jump_load_per_mass_avg_per_minute = d.pop("jump_load_per_mass_avg_per_minute", UNSET)

        physio_intensity = d.pop("physio_intensity", UNSET)

        mechanical_intensity = d.pop("mechanical_intensity", UNSET)

        mechanical_accel_total_avg_per_minute = d.pop("mechanical_accel_total_avg_per_minute", UNSET)

        mechanical_accel_category1_avg_per_minute = d.pop("mechanical_accel_category1_avg_per_minute", UNSET)

        mechanical_accel_category2_avg_per_minute = d.pop("mechanical_accel_category2_avg_per_minute", UNSET)

        mechanical_accel_category3_avg_per_minute = d.pop("mechanical_accel_category3_avg_per_minute", UNSET)

        mechanical_accel_category4_avg_per_minute = d.pop("mechanical_accel_category4_avg_per_minute", UNSET)

        mechanical_decel_total_avg_per_minute = d.pop("mechanical_decel_total_avg_per_minute", UNSET)

        mechanical_decel_category1_avg_per_minute = d.pop("mechanical_decel_category1_avg_per_minute", UNSET)

        mechanical_decel_category2_avg_per_minute = d.pop("mechanical_decel_category2_avg_per_minute", UNSET)

        mechanical_decel_category3_avg_per_minute = d.pop("mechanical_decel_category3_avg_per_minute", UNSET)

        mechanical_decel_category4_avg_per_minute = d.pop("mechanical_decel_category4_avg_per_minute", UNSET)

        mechanical_intensity_offence = d.pop("mechanical_intensity_offence", UNSET)

        mechanical_intensity_defence = d.pop("mechanical_intensity_defence", UNSET)

        playoff_load = d.pop("playoff_load", UNSET)

        human_core_temperature_avg = d.pop("human_core_temperature_avg", UNSET)

        ball_contact_count_avg_per_minute = d.pop("ball_contact_count_avg_per_minute", UNSET)

        distance_total_skating_avg_per_minute = d.pop("distance_total_skating_avg_per_minute", UNSET)

        distance_skating_speed_category1_avg_per_minute = d.pop(
            "distance_skating_speed_category1_avg_per_minute", UNSET
        )

        distance_skating_speed_category2_avg_per_minute = d.pop(
            "distance_skating_speed_category2_avg_per_minute", UNSET
        )

        distance_skating_speed_category3_avg_per_minute = d.pop(
            "distance_skating_speed_category3_avg_per_minute", UNSET
        )

        distance_skating_speed_category4_avg_per_minute = d.pop(
            "distance_skating_speed_category4_avg_per_minute", UNSET
        )

        distance_skating_speed_category5_avg_per_minute = d.pop(
            "distance_skating_speed_category5_avg_per_minute", UNSET
        )

        distance_skating_speed_category6_avg_per_minute = d.pop(
            "distance_skating_speed_category6_avg_per_minute", UNSET
        )

        distance_skating_speed_category7_avg_per_minute = d.pop(
            "distance_skating_speed_category7_avg_per_minute", UNSET
        )

        distance_total_gliding_avg_per_minute = d.pop("distance_total_gliding_avg_per_minute", UNSET)

        distance_gliding_speed_category1_avg_per_minute = d.pop(
            "distance_gliding_speed_category1_avg_per_minute", UNSET
        )

        distance_gliding_speed_category2_avg_per_minute = d.pop(
            "distance_gliding_speed_category2_avg_per_minute", UNSET
        )

        distance_gliding_speed_category3_avg_per_minute = d.pop(
            "distance_gliding_speed_category3_avg_per_minute", UNSET
        )

        distance_gliding_speed_category4_avg_per_minute = d.pop(
            "distance_gliding_speed_category4_avg_per_minute", UNSET
        )

        distance_gliding_speed_category5_avg_per_minute = d.pop(
            "distance_gliding_speed_category5_avg_per_minute", UNSET
        )

        distance_gliding_speed_category6_avg_per_minute = d.pop(
            "distance_gliding_speed_category6_avg_per_minute", UNSET
        )

        distance_gliding_speed_category7_avg_per_minute = d.pop(
            "distance_gliding_speed_category7_avg_per_minute", UNSET
        )

        imu_missing_recording_ratio = d.pop("imu_missing_recording_ratio", UNSET)

        player_statistic = cls(
            speed_avg=speed_avg,
            accel_avg=accel_avg,
            accel_load_avg=accel_load_avg,
            accel_load_accum_avg_per_minute=accel_load_accum_avg_per_minute,
            load_acceleration_load_category1_avg_per_minute=load_acceleration_load_category1_avg_per_minute,
            load_acceleration_load_category2_avg_per_minute=load_acceleration_load_category2_avg_per_minute,
            load_acceleration_load_category3_avg_per_minute=load_acceleration_load_category3_avg_per_minute,
            load_acceleration_load_category4_avg_per_minute=load_acceleration_load_category4_avg_per_minute,
            load_acceleration_load_category5_avg_per_minute=load_acceleration_load_category5_avg_per_minute,
            load_acceleration_load_category6_avg_per_minute=load_acceleration_load_category6_avg_per_minute,
            load_acceleration_load_category7_avg_per_minute=load_acceleration_load_category7_avg_per_minute,
            step_balance_avg=step_balance_avg,
            metabolic_power_avg=metabolic_power_avg,
            metabolic_power_per_mass_avg=metabolic_power_per_mass_avg,
            distance_total_avg_per_minute=distance_total_avg_per_minute,
            distance_speed_category1_avg_per_minute=distance_speed_category1_avg_per_minute,
            distance_speed_category2_avg_per_minute=distance_speed_category2_avg_per_minute,
            distance_speed_category3_avg_per_minute=distance_speed_category3_avg_per_minute,
            distance_speed_category4_avg_per_minute=distance_speed_category4_avg_per_minute,
            distance_speed_category5_avg_per_minute=distance_speed_category5_avg_per_minute,
            distance_speed_category6_avg_per_minute=distance_speed_category6_avg_per_minute,
            distance_speed_category7_avg_per_minute=distance_speed_category7_avg_per_minute,
            distance_total_relative_avg_per_minute=distance_total_relative_avg_per_minute,
            distance_speed_relative_category1_avg_per_minute=distance_speed_relative_category1_avg_per_minute,
            distance_speed_relative_category2_avg_per_minute=distance_speed_relative_category2_avg_per_minute,
            distance_speed_relative_category3_avg_per_minute=distance_speed_relative_category3_avg_per_minute,
            distance_speed_relative_category4_avg_per_minute=distance_speed_relative_category4_avg_per_minute,
            distance_speed_relative_category5_avg_per_minute=distance_speed_relative_category5_avg_per_minute,
            distance_speed_relative_category6_avg_per_minute=distance_speed_relative_category6_avg_per_minute,
            distance_speed_relative_category7_avg_per_minute=distance_speed_relative_category7_avg_per_minute,
            distance_high_metabolic_load_avg_per_minute=distance_high_metabolic_load_avg_per_minute,
            distance_high_metabolic_power_avg_per_minute=distance_high_metabolic_power_avg_per_minute,
            distance_from_steps_avg_per_minute=distance_from_steps_avg_per_minute,
            metabolic_work_avg_per_minute=metabolic_work_avg_per_minute,
            jump_load_avg_per_minute=jump_load_avg_per_minute,
            jump_load_per_mass_avg_per_minute=jump_load_per_mass_avg_per_minute,
            physio_intensity=physio_intensity,
            mechanical_intensity=mechanical_intensity,
            mechanical_accel_total_avg_per_minute=mechanical_accel_total_avg_per_minute,
            mechanical_accel_category1_avg_per_minute=mechanical_accel_category1_avg_per_minute,
            mechanical_accel_category2_avg_per_minute=mechanical_accel_category2_avg_per_minute,
            mechanical_accel_category3_avg_per_minute=mechanical_accel_category3_avg_per_minute,
            mechanical_accel_category4_avg_per_minute=mechanical_accel_category4_avg_per_minute,
            mechanical_decel_total_avg_per_minute=mechanical_decel_total_avg_per_minute,
            mechanical_decel_category1_avg_per_minute=mechanical_decel_category1_avg_per_minute,
            mechanical_decel_category2_avg_per_minute=mechanical_decel_category2_avg_per_minute,
            mechanical_decel_category3_avg_per_minute=mechanical_decel_category3_avg_per_minute,
            mechanical_decel_category4_avg_per_minute=mechanical_decel_category4_avg_per_minute,
            mechanical_intensity_offence=mechanical_intensity_offence,
            mechanical_intensity_defence=mechanical_intensity_defence,
            playoff_load=playoff_load,
            human_core_temperature_avg=human_core_temperature_avg,
            ball_contact_count_avg_per_minute=ball_contact_count_avg_per_minute,
            distance_total_skating_avg_per_minute=distance_total_skating_avg_per_minute,
            distance_skating_speed_category1_avg_per_minute=distance_skating_speed_category1_avg_per_minute,
            distance_skating_speed_category2_avg_per_minute=distance_skating_speed_category2_avg_per_minute,
            distance_skating_speed_category3_avg_per_minute=distance_skating_speed_category3_avg_per_minute,
            distance_skating_speed_category4_avg_per_minute=distance_skating_speed_category4_avg_per_minute,
            distance_skating_speed_category5_avg_per_minute=distance_skating_speed_category5_avg_per_minute,
            distance_skating_speed_category6_avg_per_minute=distance_skating_speed_category6_avg_per_minute,
            distance_skating_speed_category7_avg_per_minute=distance_skating_speed_category7_avg_per_minute,
            distance_total_gliding_avg_per_minute=distance_total_gliding_avg_per_minute,
            distance_gliding_speed_category1_avg_per_minute=distance_gliding_speed_category1_avg_per_minute,
            distance_gliding_speed_category2_avg_per_minute=distance_gliding_speed_category2_avg_per_minute,
            distance_gliding_speed_category3_avg_per_minute=distance_gliding_speed_category3_avg_per_minute,
            distance_gliding_speed_category4_avg_per_minute=distance_gliding_speed_category4_avg_per_minute,
            distance_gliding_speed_category5_avg_per_minute=distance_gliding_speed_category5_avg_per_minute,
            distance_gliding_speed_category6_avg_per_minute=distance_gliding_speed_category6_avg_per_minute,
            distance_gliding_speed_category7_avg_per_minute=distance_gliding_speed_category7_avg_per_minute,
            imu_missing_recording_ratio=imu_missing_recording_ratio,
        )

        player_statistic.additional_properties = d
        return player_statistic

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
