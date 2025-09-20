from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerStatistic")


@_attrs_define
class PlayerStatistic:
    """
    Attributes:
        heart_rate_min (Union[Unset, int]):  Example: 72.
        heart_rate_max (Union[Unset, int]): bpm Example: 192.
        heart_rate_avg (Union[Unset, float]): bpm Example: 122.
        speed_max (Union[Unset, float]): m/s Example: 3.1.
        speed_min (Union[Unset, float]): m/s Example: 1.2.
        speed_avg (Union[Unset, float]): m/s Example: 2.4.
        accel_max (Union[Unset, float]): m/s² Example: 2.5.
        accel_min (Union[Unset, float]): m/s² Example: 1.1.
        accel_avg (Union[Unset, float]): m/s² Example: 2.3.
        accel_load_max (Union[Unset, float]):  Example: 5.5.
        accel_load_avg (Union[Unset, float]):  Example: 4.5.
        accel_load_accum (Union[Unset, float]):  Example: 120.
        accel_load_accum_avg_per_minute (Union[Unset, float]): float Example: 2.1.
        load_acceleration_load_category1 (Union[Unset, float]):  Example: 20.
        load_acceleration_load_category1_avg_per_minute (Union[Unset, float]):  Example: 20.
        load_acceleration_load_category2 (Union[Unset, float]):  Example: 20.
        load_acceleration_load_category2_avg_per_minute (Union[Unset, float]):  Example: 20.
        load_acceleration_load_category3 (Union[Unset, float]):  Example: 20.
        load_acceleration_load_category3_avg_per_minute (Union[Unset, float]):  Example: 20.
        load_acceleration_load_category4 (Union[Unset, float]):  Example: 20.
        load_acceleration_load_category4_avg_per_minute (Union[Unset, float]):  Example: 20.
        load_acceleration_load_category5 (Union[Unset, float]):  Example: 20.
        load_acceleration_load_category5_avg_per_minute (Union[Unset, float]):  Example: 20.
        load_acceleration_load_category6 (Union[Unset, float]):  Example: 20.
        load_acceleration_load_category6_avg_per_minute (Union[Unset, float]):  Example: 20.
        load_acceleration_load_category7 (Union[Unset, float]):  Example: 20.
        load_acceleration_load_category7_avg_per_minute (Union[Unset, float]):  Example: 20.
        step_balance_avg (Union[Unset, float]): % Example: 40.
        metabolic_power_max (Union[Unset, float]): W Example: 320.
        metabolic_power_per_mass_max (Union[Unset, float]): W/kg Example: 7.2.
        metabolic_power_min (Union[Unset, float]): W Example: 210.
        metabolic_power_per_mass_min (Union[Unset, float]): W/kg Example: 3.6.
        metabolic_power_avg (Union[Unset, float]):  Example: 280.
        metabolic_power_per_mass_avg (Union[Unset, float]): W/kg Example: 3.9.
        distance_acceleration_load_category1 (Union[Unset, float]): m Example: 120.
        distance_acceleration_load_category2 (Union[Unset, float]): m Example: 120.
        distance_acceleration_load_category3 (Union[Unset, float]): m Example: 120.
        distance_acceleration_load_category4 (Union[Unset, float]): m Example: 120.
        distance_acceleration_load_category5 (Union[Unset, float]): m Example: 120.
        distance_acceleration_load_category6 (Union[Unset, float]): m Example: 120.
        distance_acceleration_load_category7 (Union[Unset, float]): m Example: 120.
        time_acceleration_load_category1 (Union[Unset, float]): s Example: 120.
        time_acceleration_load_category2 (Union[Unset, float]): s Example: 120.
        time_acceleration_load_category3 (Union[Unset, float]): s Example: 120.
        time_acceleration_load_category4 (Union[Unset, float]): s Example: 120.
        time_acceleration_load_category5 (Union[Unset, float]): s Example: 120.
        time_acceleration_load_category6 (Union[Unset, float]): s Example: 120.
        time_acceleration_load_category7 (Union[Unset, float]): s Example: 120.
        distance_total (Union[Unset, float]): m Example: 1500.
        distance_total_avg_per_minute (Union[Unset, float]): m Example: 20.
        distance_speed_category1 (Union[Unset, float]): m Example: 120.
        distance_speed_category2 (Union[Unset, float]): m Example: 120.
        distance_speed_category3 (Union[Unset, float]): m Example: 120.
        distance_speed_category4 (Union[Unset, float]): m Example: 120.
        distance_speed_category5 (Union[Unset, float]): m Example: 120.
        distance_speed_category6 (Union[Unset, float]): m Example: 120.
        distance_speed_category7 (Union[Unset, float]): m Example: 120.
        distance_speed_category1_avg_per_minute (Union[Unset, float]): m Example: 120.
        distance_speed_category2_avg_per_minute (Union[Unset, float]): m Example: 120.
        distance_speed_category3_avg_per_minute (Union[Unset, float]): m Example: 120.
        distance_speed_category4_avg_per_minute (Union[Unset, float]): m Example: 120.
        distance_speed_category5_avg_per_minute (Union[Unset, float]): m Example: 120.
        distance_speed_category6_avg_per_minute (Union[Unset, float]): m Example: 120.
        distance_speed_category7_avg_per_minute (Union[Unset, float]): m Example: 120.
        distance_total_relative (Union[Unset, float]): m Example: 1500.
        distance_total_relative_avg_per_minute (Union[Unset, float]): m Example: 20.
        distance_speed_relative_category1 (Union[Unset, float]): m Example: 120.
        distance_speed_relative_category2 (Union[Unset, float]): m Example: 120.
        distance_speed_relative_category3 (Union[Unset, float]): m Example: 120.
        distance_speed_relative_category4 (Union[Unset, float]): m Example: 120.
        distance_speed_relative_category5 (Union[Unset, float]): m Example: 120.
        distance_speed_relative_category6 (Union[Unset, float]): m Example: 120.
        distance_speed_relative_category7 (Union[Unset, float]): m Example: 120.
        distance_speed_relative_category1_avg_per_minute (Union[Unset, float]): m Example: 120.
        distance_speed_relative_category2_avg_per_minute (Union[Unset, float]): m Example: 120.
        distance_speed_relative_category3_avg_per_minute (Union[Unset, float]): m Example: 120.
        distance_speed_relative_category4_avg_per_minute (Union[Unset, float]): m Example: 120.
        distance_speed_relative_category5_avg_per_minute (Union[Unset, float]): m Example: 120.
        distance_speed_relative_category6_avg_per_minute (Union[Unset, float]): m Example: 120.
        distance_speed_relative_category7_avg_per_minute (Union[Unset, float]): m Example: 120.
        time_total (Union[Unset, float]): s Example: 1200.
        time_speed_category1 (Union[Unset, float]): s Example: 120.
        time_speed_category2 (Union[Unset, float]): s Example: 120.
        time_speed_category3 (Union[Unset, float]): s Example: 120.
        time_speed_category4 (Union[Unset, float]): s Example: 120.
        time_speed_category5 (Union[Unset, float]): s Example: 120.
        time_speed_category6 (Union[Unset, float]): s Example: 120.
        time_speed_category7 (Union[Unset, float]): s Example: 120.
        time_heart_rate_category1 (Union[Unset, float]): s Example: 120.
        time_heart_rate_category2 (Union[Unset, float]): s Example: 120.
        time_heart_rate_category3 (Union[Unset, float]): s Example: 120.
        time_heart_rate_category4 (Union[Unset, float]): s Example: 120.
        time_heart_rate_category5 (Union[Unset, float]): s Example: 120.
        time_heart_rate_category6 (Union[Unset, float]): s Example: 120.
        time_heart_rate_category7 (Union[Unset, float]): s Example: 120.
        distance_high_metabolic_load (Union[Unset, float]): m Example: 120.
        distance_high_metabolic_load_avg_per_minute (Union[Unset, float]): m Example: 4.2.
        distance_high_metabolic_power (Union[Unset, float]): m Example: 120.
        distance_high_metabolic_power_avg_per_minute (Union[Unset, float]): m Example: 4.2.
        distance_anaerobic_activity (Union[Unset, float]): m Example: 120.
        distance_from_steps (Union[Unset, float]): m Example: 120.
        distance_from_steps_avg_per_minute (Union[Unset, float]): m Example: 20.
        time_metabolic_power_category1 (Union[Unset, float]): s Example: 120.
        time_metabolic_power_category2 (Union[Unset, float]): s Example: 120.
        time_metabolic_power_category3 (Union[Unset, float]): s Example: 120.
        time_metabolic_power_category4 (Union[Unset, float]): s Example: 120.
        time_metabolic_power_category5 (Union[Unset, float]): s Example: 120.
        time_metabolic_power_category6 (Union[Unset, float]): s Example: 120.
        time_metabolic_power_category7 (Union[Unset, float]): s Example: 120.
        metabolic_work (Union[Unset, float]): kcal Example: 333.
        metabolic_work_avg_per_minute (Union[Unset, float]): kcal Example: 9.9.
        number_of_steps (Union[Unset, int]): s Example: 300.
        time_on_playing_field (Union[Unset, float]): s Example: 1200.
        time_on_playing_field_defence (Union[Unset, float]): s Example: 600.
        time_on_playing_field_offence (Union[Unset, float]): s Example: 600.
        time_on_playing_field_pp (Union[Unset, float]): s Example: 600.
        time_on_playing_field_pk (Union[Unset, float]): s Example: 600.
        active_game_time (Union[Unset, float]): s Example: 1200.
        jump_load (Union[Unset, float]): J Example: 200.
        jump_load_avg_per_minute (Union[Unset, float]): J Example: 2.1.
        jump_load_per_mass (Union[Unset, float]): J/kg Example: 2.1.
        jump_load_per_mass_avg_per_minute (Union[Unset, float]): J/kg Example: 2.1.
        time_ball_possession (Union[Unset, float]): s Example: 120.
        time_anaerobic_activity (Union[Unset, float]): s Example: 120.
        jump_height_max (Union[Unset, float]): m Example: 1.2.
        trimp (Union[Unset, float]):
        heart_rate_impulse (Union[Unset, float]):
        physio_load (Union[Unset, float]):  Example: 120.1.
        physio_load_speed_category1 (Union[Unset, float]):  Example: 120.1.
        physio_load_speed_category2 (Union[Unset, float]):  Example: 120.1.
        physio_load_speed_category3 (Union[Unset, float]):  Example: 120.1.
        physio_load_speed_category4 (Union[Unset, float]):  Example: 120.1.
        physio_load_speed_category5 (Union[Unset, float]):  Example: 120.1.
        physio_load_speed_category6 (Union[Unset, float]):  Example: 120.1.
        physio_load_speed_category7 (Union[Unset, float]):  Example: 120.1.
        physio_intensity (Union[Unset, float]): physio_load/total_time
        mechanical_load (Union[Unset, float]):  Example: 120.1.
        mechanical_intensity (Union[Unset, float]): mechanical_load/total_time
        mechanical_accel_total (Union[Unset, float]):  Example: 123.
        mechanical_accel_total_avg_per_minute (Union[Unset, float]):  Example: 2.1.
        mechanical_accel_category1 (Union[Unset, float]):  Example: 20.
        mechanical_accel_category1_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        mechanical_accel_category2 (Union[Unset, float]):  Example: 20.
        mechanical_accel_category2_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        mechanical_accel_category3 (Union[Unset, float]):  Example: 20.
        mechanical_accel_category3_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        mechanical_accel_category4 (Union[Unset, float]):  Example: 20.
        mechanical_accel_category4_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        mechanical_decel_total (Union[Unset, float]):  Example: 20.
        mechanical_decel_total_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        mechanical_decel_category1 (Union[Unset, float]):  Example: 20.
        mechanical_decel_category1_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        mechanical_decel_category2 (Union[Unset, float]):  Example: 20.
        mechanical_decel_category2_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        mechanical_decel_category3 (Union[Unset, float]):  Example: 20.
        mechanical_decel_category3_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        mechanical_decel_category4 (Union[Unset, float]):  Example: 20.
        mechanical_decel_category4_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        data_quality (Union[Unset, float]): % Example: 95.
        data_availability (Union[Unset, float]):
        mechanical_load_defence (Union[Unset, float]):  Example: 120.
        mechanical_load_offence (Union[Unset, float]):  Example: 120.
        mechanical_intensity_offence (Union[Unset, float]):  Example: 20.
        mechanical_intensity_defence (Union[Unset, float]):  Example: 20.
        playoff_load (Union[Unset, float]):  Example: 120.
        human_core_temperature_max (Union[Unset, float]): °C Example: 37.9.
        human_core_temperature_avg (Union[Unset, float]): °C Example: 37.6.
        time_high_metabolic_load (Union[Unset, float]): s Example: 120.
        imu_flag (Union[Unset, int]):
        distance_forward (Union[Unset, float]): m Example: 1500.
        distance_backward (Union[Unset, float]): m Example: 1500.
        distance_left (Union[Unset, float]): m Example: 1500.
        distance_right (Union[Unset, float]): m Example: 1500.
        distance_unknown (Union[Unset, float]): m Example: 1500.
        ball_contact_count (Union[Unset, int]):  Example: 85.
        ball_contact_count_avg_per_minute (Union[Unset, float]): float Example: 2.1.
        time_total_skating (Union[Unset, float]): s Example: 1200.
        distance_total_skating (Union[Unset, float]): m Example: 1500.
        distance_total_skating_avg_per_minute (Union[Unset, float]): m Example: 20.
        distance_skating_speed_category1 (Union[Unset, float]):  Example: 20.
        distance_skating_speed_category1_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        distance_skating_speed_category2 (Union[Unset, float]):  Example: 20.
        distance_skating_speed_category2_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        distance_skating_speed_category3 (Union[Unset, float]):  Example: 20.
        distance_skating_speed_category3_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        distance_skating_speed_category4 (Union[Unset, float]):  Example: 20.
        distance_skating_speed_category4_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        distance_skating_speed_category5 (Union[Unset, float]):  Example: 20.
        distance_skating_speed_category5_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        distance_skating_speed_category6 (Union[Unset, float]):  Example: 20.
        distance_skating_speed_category6_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        distance_skating_speed_category7 (Union[Unset, float]):  Example: 20.
        distance_skating_speed_category7_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        time_total_gliding (Union[Unset, float]): s Example: 1200.
        distance_total_gliding (Union[Unset, float]): m Example: 1500.
        distance_total_gliding_avg_per_minute (Union[Unset, float]): m Example: 20.
        distance_gliding_speed_category1 (Union[Unset, float]):  Example: 20.
        distance_gliding_speed_category1_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        distance_gliding_speed_category2 (Union[Unset, float]):  Example: 20.
        distance_gliding_speed_category2_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        distance_gliding_speed_category3 (Union[Unset, float]):  Example: 20.
        distance_gliding_speed_category3_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        distance_gliding_speed_category4 (Union[Unset, float]):  Example: 20.
        distance_gliding_speed_category4_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        distance_gliding_speed_category5 (Union[Unset, float]):  Example: 20.
        distance_gliding_speed_category5_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        distance_gliding_speed_category6 (Union[Unset, float]):  Example: 20.
        distance_gliding_speed_category6_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        distance_gliding_speed_category7 (Union[Unset, float]):  Example: 20.
        distance_gliding_speed_category7_avg_per_minute (Union[Unset, float]):  Example: 1.2.
        time_total_standing (Union[Unset, float]): s Example: 1200.
        time_imu_defective (Union[Unset, float]): s Example: 120.
        imu_missing_recording_ratio (Union[Unset, float]):  Example: 1.5.
    """

    heart_rate_min: Union[Unset, int] = UNSET
    heart_rate_max: Union[Unset, int] = UNSET
    heart_rate_avg: Union[Unset, float] = UNSET
    speed_max: Union[Unset, float] = UNSET
    speed_min: Union[Unset, float] = UNSET
    speed_avg: Union[Unset, float] = UNSET
    accel_max: Union[Unset, float] = UNSET
    accel_min: Union[Unset, float] = UNSET
    accel_avg: Union[Unset, float] = UNSET
    accel_load_max: Union[Unset, float] = UNSET
    accel_load_avg: Union[Unset, float] = UNSET
    accel_load_accum: Union[Unset, float] = UNSET
    accel_load_accum_avg_per_minute: Union[Unset, float] = UNSET
    load_acceleration_load_category1: Union[Unset, float] = UNSET
    load_acceleration_load_category1_avg_per_minute: Union[Unset, float] = UNSET
    load_acceleration_load_category2: Union[Unset, float] = UNSET
    load_acceleration_load_category2_avg_per_minute: Union[Unset, float] = UNSET
    load_acceleration_load_category3: Union[Unset, float] = UNSET
    load_acceleration_load_category3_avg_per_minute: Union[Unset, float] = UNSET
    load_acceleration_load_category4: Union[Unset, float] = UNSET
    load_acceleration_load_category4_avg_per_minute: Union[Unset, float] = UNSET
    load_acceleration_load_category5: Union[Unset, float] = UNSET
    load_acceleration_load_category5_avg_per_minute: Union[Unset, float] = UNSET
    load_acceleration_load_category6: Union[Unset, float] = UNSET
    load_acceleration_load_category6_avg_per_minute: Union[Unset, float] = UNSET
    load_acceleration_load_category7: Union[Unset, float] = UNSET
    load_acceleration_load_category7_avg_per_minute: Union[Unset, float] = UNSET
    step_balance_avg: Union[Unset, float] = UNSET
    metabolic_power_max: Union[Unset, float] = UNSET
    metabolic_power_per_mass_max: Union[Unset, float] = UNSET
    metabolic_power_min: Union[Unset, float] = UNSET
    metabolic_power_per_mass_min: Union[Unset, float] = UNSET
    metabolic_power_avg: Union[Unset, float] = UNSET
    metabolic_power_per_mass_avg: Union[Unset, float] = UNSET
    distance_acceleration_load_category1: Union[Unset, float] = UNSET
    distance_acceleration_load_category2: Union[Unset, float] = UNSET
    distance_acceleration_load_category3: Union[Unset, float] = UNSET
    distance_acceleration_load_category4: Union[Unset, float] = UNSET
    distance_acceleration_load_category5: Union[Unset, float] = UNSET
    distance_acceleration_load_category6: Union[Unset, float] = UNSET
    distance_acceleration_load_category7: Union[Unset, float] = UNSET
    time_acceleration_load_category1: Union[Unset, float] = UNSET
    time_acceleration_load_category2: Union[Unset, float] = UNSET
    time_acceleration_load_category3: Union[Unset, float] = UNSET
    time_acceleration_load_category4: Union[Unset, float] = UNSET
    time_acceleration_load_category5: Union[Unset, float] = UNSET
    time_acceleration_load_category6: Union[Unset, float] = UNSET
    time_acceleration_load_category7: Union[Unset, float] = UNSET
    distance_total: Union[Unset, float] = UNSET
    distance_total_avg_per_minute: Union[Unset, float] = UNSET
    distance_speed_category1: Union[Unset, float] = UNSET
    distance_speed_category2: Union[Unset, float] = UNSET
    distance_speed_category3: Union[Unset, float] = UNSET
    distance_speed_category4: Union[Unset, float] = UNSET
    distance_speed_category5: Union[Unset, float] = UNSET
    distance_speed_category6: Union[Unset, float] = UNSET
    distance_speed_category7: Union[Unset, float] = UNSET
    distance_speed_category1_avg_per_minute: Union[Unset, float] = UNSET
    distance_speed_category2_avg_per_minute: Union[Unset, float] = UNSET
    distance_speed_category3_avg_per_minute: Union[Unset, float] = UNSET
    distance_speed_category4_avg_per_minute: Union[Unset, float] = UNSET
    distance_speed_category5_avg_per_minute: Union[Unset, float] = UNSET
    distance_speed_category6_avg_per_minute: Union[Unset, float] = UNSET
    distance_speed_category7_avg_per_minute: Union[Unset, float] = UNSET
    distance_total_relative: Union[Unset, float] = UNSET
    distance_total_relative_avg_per_minute: Union[Unset, float] = UNSET
    distance_speed_relative_category1: Union[Unset, float] = UNSET
    distance_speed_relative_category2: Union[Unset, float] = UNSET
    distance_speed_relative_category3: Union[Unset, float] = UNSET
    distance_speed_relative_category4: Union[Unset, float] = UNSET
    distance_speed_relative_category5: Union[Unset, float] = UNSET
    distance_speed_relative_category6: Union[Unset, float] = UNSET
    distance_speed_relative_category7: Union[Unset, float] = UNSET
    distance_speed_relative_category1_avg_per_minute: Union[Unset, float] = UNSET
    distance_speed_relative_category2_avg_per_minute: Union[Unset, float] = UNSET
    distance_speed_relative_category3_avg_per_minute: Union[Unset, float] = UNSET
    distance_speed_relative_category4_avg_per_minute: Union[Unset, float] = UNSET
    distance_speed_relative_category5_avg_per_minute: Union[Unset, float] = UNSET
    distance_speed_relative_category6_avg_per_minute: Union[Unset, float] = UNSET
    distance_speed_relative_category7_avg_per_minute: Union[Unset, float] = UNSET
    time_total: Union[Unset, float] = UNSET
    time_speed_category1: Union[Unset, float] = UNSET
    time_speed_category2: Union[Unset, float] = UNSET
    time_speed_category3: Union[Unset, float] = UNSET
    time_speed_category4: Union[Unset, float] = UNSET
    time_speed_category5: Union[Unset, float] = UNSET
    time_speed_category6: Union[Unset, float] = UNSET
    time_speed_category7: Union[Unset, float] = UNSET
    time_heart_rate_category1: Union[Unset, float] = UNSET
    time_heart_rate_category2: Union[Unset, float] = UNSET
    time_heart_rate_category3: Union[Unset, float] = UNSET
    time_heart_rate_category4: Union[Unset, float] = UNSET
    time_heart_rate_category5: Union[Unset, float] = UNSET
    time_heart_rate_category6: Union[Unset, float] = UNSET
    time_heart_rate_category7: Union[Unset, float] = UNSET
    distance_high_metabolic_load: Union[Unset, float] = UNSET
    distance_high_metabolic_load_avg_per_minute: Union[Unset, float] = UNSET
    distance_high_metabolic_power: Union[Unset, float] = UNSET
    distance_high_metabolic_power_avg_per_minute: Union[Unset, float] = UNSET
    distance_anaerobic_activity: Union[Unset, float] = UNSET
    distance_from_steps: Union[Unset, float] = UNSET
    distance_from_steps_avg_per_minute: Union[Unset, float] = UNSET
    time_metabolic_power_category1: Union[Unset, float] = UNSET
    time_metabolic_power_category2: Union[Unset, float] = UNSET
    time_metabolic_power_category3: Union[Unset, float] = UNSET
    time_metabolic_power_category4: Union[Unset, float] = UNSET
    time_metabolic_power_category5: Union[Unset, float] = UNSET
    time_metabolic_power_category6: Union[Unset, float] = UNSET
    time_metabolic_power_category7: Union[Unset, float] = UNSET
    metabolic_work: Union[Unset, float] = UNSET
    metabolic_work_avg_per_minute: Union[Unset, float] = UNSET
    number_of_steps: Union[Unset, int] = UNSET
    time_on_playing_field: Union[Unset, float] = UNSET
    time_on_playing_field_defence: Union[Unset, float] = UNSET
    time_on_playing_field_offence: Union[Unset, float] = UNSET
    time_on_playing_field_pp: Union[Unset, float] = UNSET
    time_on_playing_field_pk: Union[Unset, float] = UNSET
    active_game_time: Union[Unset, float] = UNSET
    jump_load: Union[Unset, float] = UNSET
    jump_load_avg_per_minute: Union[Unset, float] = UNSET
    jump_load_per_mass: Union[Unset, float] = UNSET
    jump_load_per_mass_avg_per_minute: Union[Unset, float] = UNSET
    time_ball_possession: Union[Unset, float] = UNSET
    time_anaerobic_activity: Union[Unset, float] = UNSET
    jump_height_max: Union[Unset, float] = UNSET
    trimp: Union[Unset, float] = UNSET
    heart_rate_impulse: Union[Unset, float] = UNSET
    physio_load: Union[Unset, float] = UNSET
    physio_load_speed_category1: Union[Unset, float] = UNSET
    physio_load_speed_category2: Union[Unset, float] = UNSET
    physio_load_speed_category3: Union[Unset, float] = UNSET
    physio_load_speed_category4: Union[Unset, float] = UNSET
    physio_load_speed_category5: Union[Unset, float] = UNSET
    physio_load_speed_category6: Union[Unset, float] = UNSET
    physio_load_speed_category7: Union[Unset, float] = UNSET
    physio_intensity: Union[Unset, float] = UNSET
    mechanical_load: Union[Unset, float] = UNSET
    mechanical_intensity: Union[Unset, float] = UNSET
    mechanical_accel_total: Union[Unset, float] = UNSET
    mechanical_accel_total_avg_per_minute: Union[Unset, float] = UNSET
    mechanical_accel_category1: Union[Unset, float] = UNSET
    mechanical_accel_category1_avg_per_minute: Union[Unset, float] = UNSET
    mechanical_accel_category2: Union[Unset, float] = UNSET
    mechanical_accel_category2_avg_per_minute: Union[Unset, float] = UNSET
    mechanical_accel_category3: Union[Unset, float] = UNSET
    mechanical_accel_category3_avg_per_minute: Union[Unset, float] = UNSET
    mechanical_accel_category4: Union[Unset, float] = UNSET
    mechanical_accel_category4_avg_per_minute: Union[Unset, float] = UNSET
    mechanical_decel_total: Union[Unset, float] = UNSET
    mechanical_decel_total_avg_per_minute: Union[Unset, float] = UNSET
    mechanical_decel_category1: Union[Unset, float] = UNSET
    mechanical_decel_category1_avg_per_minute: Union[Unset, float] = UNSET
    mechanical_decel_category2: Union[Unset, float] = UNSET
    mechanical_decel_category2_avg_per_minute: Union[Unset, float] = UNSET
    mechanical_decel_category3: Union[Unset, float] = UNSET
    mechanical_decel_category3_avg_per_minute: Union[Unset, float] = UNSET
    mechanical_decel_category4: Union[Unset, float] = UNSET
    mechanical_decel_category4_avg_per_minute: Union[Unset, float] = UNSET
    data_quality: Union[Unset, float] = UNSET
    data_availability: Union[Unset, float] = UNSET
    mechanical_load_defence: Union[Unset, float] = UNSET
    mechanical_load_offence: Union[Unset, float] = UNSET
    mechanical_intensity_offence: Union[Unset, float] = UNSET
    mechanical_intensity_defence: Union[Unset, float] = UNSET
    playoff_load: Union[Unset, float] = UNSET
    human_core_temperature_max: Union[Unset, float] = UNSET
    human_core_temperature_avg: Union[Unset, float] = UNSET
    time_high_metabolic_load: Union[Unset, float] = UNSET
    imu_flag: Union[Unset, int] = UNSET
    distance_forward: Union[Unset, float] = UNSET
    distance_backward: Union[Unset, float] = UNSET
    distance_left: Union[Unset, float] = UNSET
    distance_right: Union[Unset, float] = UNSET
    distance_unknown: Union[Unset, float] = UNSET
    ball_contact_count: Union[Unset, int] = UNSET
    ball_contact_count_avg_per_minute: Union[Unset, float] = UNSET
    time_total_skating: Union[Unset, float] = UNSET
    distance_total_skating: Union[Unset, float] = UNSET
    distance_total_skating_avg_per_minute: Union[Unset, float] = UNSET
    distance_skating_speed_category1: Union[Unset, float] = UNSET
    distance_skating_speed_category1_avg_per_minute: Union[Unset, float] = UNSET
    distance_skating_speed_category2: Union[Unset, float] = UNSET
    distance_skating_speed_category2_avg_per_minute: Union[Unset, float] = UNSET
    distance_skating_speed_category3: Union[Unset, float] = UNSET
    distance_skating_speed_category3_avg_per_minute: Union[Unset, float] = UNSET
    distance_skating_speed_category4: Union[Unset, float] = UNSET
    distance_skating_speed_category4_avg_per_minute: Union[Unset, float] = UNSET
    distance_skating_speed_category5: Union[Unset, float] = UNSET
    distance_skating_speed_category5_avg_per_minute: Union[Unset, float] = UNSET
    distance_skating_speed_category6: Union[Unset, float] = UNSET
    distance_skating_speed_category6_avg_per_minute: Union[Unset, float] = UNSET
    distance_skating_speed_category7: Union[Unset, float] = UNSET
    distance_skating_speed_category7_avg_per_minute: Union[Unset, float] = UNSET
    time_total_gliding: Union[Unset, float] = UNSET
    distance_total_gliding: Union[Unset, float] = UNSET
    distance_total_gliding_avg_per_minute: Union[Unset, float] = UNSET
    distance_gliding_speed_category1: Union[Unset, float] = UNSET
    distance_gliding_speed_category1_avg_per_minute: Union[Unset, float] = UNSET
    distance_gliding_speed_category2: Union[Unset, float] = UNSET
    distance_gliding_speed_category2_avg_per_minute: Union[Unset, float] = UNSET
    distance_gliding_speed_category3: Union[Unset, float] = UNSET
    distance_gliding_speed_category3_avg_per_minute: Union[Unset, float] = UNSET
    distance_gliding_speed_category4: Union[Unset, float] = UNSET
    distance_gliding_speed_category4_avg_per_minute: Union[Unset, float] = UNSET
    distance_gliding_speed_category5: Union[Unset, float] = UNSET
    distance_gliding_speed_category5_avg_per_minute: Union[Unset, float] = UNSET
    distance_gliding_speed_category6: Union[Unset, float] = UNSET
    distance_gliding_speed_category6_avg_per_minute: Union[Unset, float] = UNSET
    distance_gliding_speed_category7: Union[Unset, float] = UNSET
    distance_gliding_speed_category7_avg_per_minute: Union[Unset, float] = UNSET
    time_total_standing: Union[Unset, float] = UNSET
    time_imu_defective: Union[Unset, float] = UNSET
    imu_missing_recording_ratio: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        heart_rate_min = self.heart_rate_min

        heart_rate_max = self.heart_rate_max

        heart_rate_avg = self.heart_rate_avg

        speed_max = self.speed_max

        speed_min = self.speed_min

        speed_avg = self.speed_avg

        accel_max = self.accel_max

        accel_min = self.accel_min

        accel_avg = self.accel_avg

        accel_load_max = self.accel_load_max

        accel_load_avg = self.accel_load_avg

        accel_load_accum = self.accel_load_accum

        accel_load_accum_avg_per_minute = self.accel_load_accum_avg_per_minute

        load_acceleration_load_category1 = self.load_acceleration_load_category1

        load_acceleration_load_category1_avg_per_minute = self.load_acceleration_load_category1_avg_per_minute

        load_acceleration_load_category2 = self.load_acceleration_load_category2

        load_acceleration_load_category2_avg_per_minute = self.load_acceleration_load_category2_avg_per_minute

        load_acceleration_load_category3 = self.load_acceleration_load_category3

        load_acceleration_load_category3_avg_per_minute = self.load_acceleration_load_category3_avg_per_minute

        load_acceleration_load_category4 = self.load_acceleration_load_category4

        load_acceleration_load_category4_avg_per_minute = self.load_acceleration_load_category4_avg_per_minute

        load_acceleration_load_category5 = self.load_acceleration_load_category5

        load_acceleration_load_category5_avg_per_minute = self.load_acceleration_load_category5_avg_per_minute

        load_acceleration_load_category6 = self.load_acceleration_load_category6

        load_acceleration_load_category6_avg_per_minute = self.load_acceleration_load_category6_avg_per_minute

        load_acceleration_load_category7 = self.load_acceleration_load_category7

        load_acceleration_load_category7_avg_per_minute = self.load_acceleration_load_category7_avg_per_minute

        step_balance_avg = self.step_balance_avg

        metabolic_power_max = self.metabolic_power_max

        metabolic_power_per_mass_max = self.metabolic_power_per_mass_max

        metabolic_power_min = self.metabolic_power_min

        metabolic_power_per_mass_min = self.metabolic_power_per_mass_min

        metabolic_power_avg = self.metabolic_power_avg

        metabolic_power_per_mass_avg = self.metabolic_power_per_mass_avg

        distance_acceleration_load_category1 = self.distance_acceleration_load_category1

        distance_acceleration_load_category2 = self.distance_acceleration_load_category2

        distance_acceleration_load_category3 = self.distance_acceleration_load_category3

        distance_acceleration_load_category4 = self.distance_acceleration_load_category4

        distance_acceleration_load_category5 = self.distance_acceleration_load_category5

        distance_acceleration_load_category6 = self.distance_acceleration_load_category6

        distance_acceleration_load_category7 = self.distance_acceleration_load_category7

        time_acceleration_load_category1 = self.time_acceleration_load_category1

        time_acceleration_load_category2 = self.time_acceleration_load_category2

        time_acceleration_load_category3 = self.time_acceleration_load_category3

        time_acceleration_load_category4 = self.time_acceleration_load_category4

        time_acceleration_load_category5 = self.time_acceleration_load_category5

        time_acceleration_load_category6 = self.time_acceleration_load_category6

        time_acceleration_load_category7 = self.time_acceleration_load_category7

        distance_total = self.distance_total

        distance_total_avg_per_minute = self.distance_total_avg_per_minute

        distance_speed_category1 = self.distance_speed_category1

        distance_speed_category2 = self.distance_speed_category2

        distance_speed_category3 = self.distance_speed_category3

        distance_speed_category4 = self.distance_speed_category4

        distance_speed_category5 = self.distance_speed_category5

        distance_speed_category6 = self.distance_speed_category6

        distance_speed_category7 = self.distance_speed_category7

        distance_speed_category1_avg_per_minute = self.distance_speed_category1_avg_per_minute

        distance_speed_category2_avg_per_minute = self.distance_speed_category2_avg_per_minute

        distance_speed_category3_avg_per_minute = self.distance_speed_category3_avg_per_minute

        distance_speed_category4_avg_per_minute = self.distance_speed_category4_avg_per_minute

        distance_speed_category5_avg_per_minute = self.distance_speed_category5_avg_per_minute

        distance_speed_category6_avg_per_minute = self.distance_speed_category6_avg_per_minute

        distance_speed_category7_avg_per_minute = self.distance_speed_category7_avg_per_minute

        distance_total_relative = self.distance_total_relative

        distance_total_relative_avg_per_minute = self.distance_total_relative_avg_per_minute

        distance_speed_relative_category1 = self.distance_speed_relative_category1

        distance_speed_relative_category2 = self.distance_speed_relative_category2

        distance_speed_relative_category3 = self.distance_speed_relative_category3

        distance_speed_relative_category4 = self.distance_speed_relative_category4

        distance_speed_relative_category5 = self.distance_speed_relative_category5

        distance_speed_relative_category6 = self.distance_speed_relative_category6

        distance_speed_relative_category7 = self.distance_speed_relative_category7

        distance_speed_relative_category1_avg_per_minute = self.distance_speed_relative_category1_avg_per_minute

        distance_speed_relative_category2_avg_per_minute = self.distance_speed_relative_category2_avg_per_minute

        distance_speed_relative_category3_avg_per_minute = self.distance_speed_relative_category3_avg_per_minute

        distance_speed_relative_category4_avg_per_minute = self.distance_speed_relative_category4_avg_per_minute

        distance_speed_relative_category5_avg_per_minute = self.distance_speed_relative_category5_avg_per_minute

        distance_speed_relative_category6_avg_per_minute = self.distance_speed_relative_category6_avg_per_minute

        distance_speed_relative_category7_avg_per_minute = self.distance_speed_relative_category7_avg_per_minute

        time_total = self.time_total

        time_speed_category1 = self.time_speed_category1

        time_speed_category2 = self.time_speed_category2

        time_speed_category3 = self.time_speed_category3

        time_speed_category4 = self.time_speed_category4

        time_speed_category5 = self.time_speed_category5

        time_speed_category6 = self.time_speed_category6

        time_speed_category7 = self.time_speed_category7

        time_heart_rate_category1 = self.time_heart_rate_category1

        time_heart_rate_category2 = self.time_heart_rate_category2

        time_heart_rate_category3 = self.time_heart_rate_category3

        time_heart_rate_category4 = self.time_heart_rate_category4

        time_heart_rate_category5 = self.time_heart_rate_category5

        time_heart_rate_category6 = self.time_heart_rate_category6

        time_heart_rate_category7 = self.time_heart_rate_category7

        distance_high_metabolic_load = self.distance_high_metabolic_load

        distance_high_metabolic_load_avg_per_minute = self.distance_high_metabolic_load_avg_per_minute

        distance_high_metabolic_power = self.distance_high_metabolic_power

        distance_high_metabolic_power_avg_per_minute = self.distance_high_metabolic_power_avg_per_minute

        distance_anaerobic_activity = self.distance_anaerobic_activity

        distance_from_steps = self.distance_from_steps

        distance_from_steps_avg_per_minute = self.distance_from_steps_avg_per_minute

        time_metabolic_power_category1 = self.time_metabolic_power_category1

        time_metabolic_power_category2 = self.time_metabolic_power_category2

        time_metabolic_power_category3 = self.time_metabolic_power_category3

        time_metabolic_power_category4 = self.time_metabolic_power_category4

        time_metabolic_power_category5 = self.time_metabolic_power_category5

        time_metabolic_power_category6 = self.time_metabolic_power_category6

        time_metabolic_power_category7 = self.time_metabolic_power_category7

        metabolic_work = self.metabolic_work

        metabolic_work_avg_per_minute = self.metabolic_work_avg_per_minute

        number_of_steps = self.number_of_steps

        time_on_playing_field = self.time_on_playing_field

        time_on_playing_field_defence = self.time_on_playing_field_defence

        time_on_playing_field_offence = self.time_on_playing_field_offence

        time_on_playing_field_pp = self.time_on_playing_field_pp

        time_on_playing_field_pk = self.time_on_playing_field_pk

        active_game_time = self.active_game_time

        jump_load = self.jump_load

        jump_load_avg_per_minute = self.jump_load_avg_per_minute

        jump_load_per_mass = self.jump_load_per_mass

        jump_load_per_mass_avg_per_minute = self.jump_load_per_mass_avg_per_minute

        time_ball_possession = self.time_ball_possession

        time_anaerobic_activity = self.time_anaerobic_activity

        jump_height_max = self.jump_height_max

        trimp = self.trimp

        heart_rate_impulse = self.heart_rate_impulse

        physio_load = self.physio_load

        physio_load_speed_category1 = self.physio_load_speed_category1

        physio_load_speed_category2 = self.physio_load_speed_category2

        physio_load_speed_category3 = self.physio_load_speed_category3

        physio_load_speed_category4 = self.physio_load_speed_category4

        physio_load_speed_category5 = self.physio_load_speed_category5

        physio_load_speed_category6 = self.physio_load_speed_category6

        physio_load_speed_category7 = self.physio_load_speed_category7

        physio_intensity = self.physio_intensity

        mechanical_load = self.mechanical_load

        mechanical_intensity = self.mechanical_intensity

        mechanical_accel_total = self.mechanical_accel_total

        mechanical_accel_total_avg_per_minute = self.mechanical_accel_total_avg_per_minute

        mechanical_accel_category1 = self.mechanical_accel_category1

        mechanical_accel_category1_avg_per_minute = self.mechanical_accel_category1_avg_per_minute

        mechanical_accel_category2 = self.mechanical_accel_category2

        mechanical_accel_category2_avg_per_minute = self.mechanical_accel_category2_avg_per_minute

        mechanical_accel_category3 = self.mechanical_accel_category3

        mechanical_accel_category3_avg_per_minute = self.mechanical_accel_category3_avg_per_minute

        mechanical_accel_category4 = self.mechanical_accel_category4

        mechanical_accel_category4_avg_per_minute = self.mechanical_accel_category4_avg_per_minute

        mechanical_decel_total = self.mechanical_decel_total

        mechanical_decel_total_avg_per_minute = self.mechanical_decel_total_avg_per_minute

        mechanical_decel_category1 = self.mechanical_decel_category1

        mechanical_decel_category1_avg_per_minute = self.mechanical_decel_category1_avg_per_minute

        mechanical_decel_category2 = self.mechanical_decel_category2

        mechanical_decel_category2_avg_per_minute = self.mechanical_decel_category2_avg_per_minute

        mechanical_decel_category3 = self.mechanical_decel_category3

        mechanical_decel_category3_avg_per_minute = self.mechanical_decel_category3_avg_per_minute

        mechanical_decel_category4 = self.mechanical_decel_category4

        mechanical_decel_category4_avg_per_minute = self.mechanical_decel_category4_avg_per_minute

        data_quality = self.data_quality

        data_availability = self.data_availability

        mechanical_load_defence = self.mechanical_load_defence

        mechanical_load_offence = self.mechanical_load_offence

        mechanical_intensity_offence = self.mechanical_intensity_offence

        mechanical_intensity_defence = self.mechanical_intensity_defence

        playoff_load = self.playoff_load

        human_core_temperature_max = self.human_core_temperature_max

        human_core_temperature_avg = self.human_core_temperature_avg

        time_high_metabolic_load = self.time_high_metabolic_load

        imu_flag = self.imu_flag

        distance_forward = self.distance_forward

        distance_backward = self.distance_backward

        distance_left = self.distance_left

        distance_right = self.distance_right

        distance_unknown = self.distance_unknown

        ball_contact_count = self.ball_contact_count

        ball_contact_count_avg_per_minute = self.ball_contact_count_avg_per_minute

        time_total_skating = self.time_total_skating

        distance_total_skating = self.distance_total_skating

        distance_total_skating_avg_per_minute = self.distance_total_skating_avg_per_minute

        distance_skating_speed_category1 = self.distance_skating_speed_category1

        distance_skating_speed_category1_avg_per_minute = self.distance_skating_speed_category1_avg_per_minute

        distance_skating_speed_category2 = self.distance_skating_speed_category2

        distance_skating_speed_category2_avg_per_minute = self.distance_skating_speed_category2_avg_per_minute

        distance_skating_speed_category3 = self.distance_skating_speed_category3

        distance_skating_speed_category3_avg_per_minute = self.distance_skating_speed_category3_avg_per_minute

        distance_skating_speed_category4 = self.distance_skating_speed_category4

        distance_skating_speed_category4_avg_per_minute = self.distance_skating_speed_category4_avg_per_minute

        distance_skating_speed_category5 = self.distance_skating_speed_category5

        distance_skating_speed_category5_avg_per_minute = self.distance_skating_speed_category5_avg_per_minute

        distance_skating_speed_category6 = self.distance_skating_speed_category6

        distance_skating_speed_category6_avg_per_minute = self.distance_skating_speed_category6_avg_per_minute

        distance_skating_speed_category7 = self.distance_skating_speed_category7

        distance_skating_speed_category7_avg_per_minute = self.distance_skating_speed_category7_avg_per_minute

        time_total_gliding = self.time_total_gliding

        distance_total_gliding = self.distance_total_gliding

        distance_total_gliding_avg_per_minute = self.distance_total_gliding_avg_per_minute

        distance_gliding_speed_category1 = self.distance_gliding_speed_category1

        distance_gliding_speed_category1_avg_per_minute = self.distance_gliding_speed_category1_avg_per_minute

        distance_gliding_speed_category2 = self.distance_gliding_speed_category2

        distance_gliding_speed_category2_avg_per_minute = self.distance_gliding_speed_category2_avg_per_minute

        distance_gliding_speed_category3 = self.distance_gliding_speed_category3

        distance_gliding_speed_category3_avg_per_minute = self.distance_gliding_speed_category3_avg_per_minute

        distance_gliding_speed_category4 = self.distance_gliding_speed_category4

        distance_gliding_speed_category4_avg_per_minute = self.distance_gliding_speed_category4_avg_per_minute

        distance_gliding_speed_category5 = self.distance_gliding_speed_category5

        distance_gliding_speed_category5_avg_per_minute = self.distance_gliding_speed_category5_avg_per_minute

        distance_gliding_speed_category6 = self.distance_gliding_speed_category6

        distance_gliding_speed_category6_avg_per_minute = self.distance_gliding_speed_category6_avg_per_minute

        distance_gliding_speed_category7 = self.distance_gliding_speed_category7

        distance_gliding_speed_category7_avg_per_minute = self.distance_gliding_speed_category7_avg_per_minute

        time_total_standing = self.time_total_standing

        time_imu_defective = self.time_imu_defective

        imu_missing_recording_ratio = self.imu_missing_recording_ratio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if heart_rate_min is not UNSET:
            field_dict["heart_rate_min"] = heart_rate_min
        if heart_rate_max is not UNSET:
            field_dict["heart_rate_max"] = heart_rate_max
        if heart_rate_avg is not UNSET:
            field_dict["heart_rate_avg"] = heart_rate_avg
        if speed_max is not UNSET:
            field_dict["speed_max"] = speed_max
        if speed_min is not UNSET:
            field_dict["speed_min"] = speed_min
        if speed_avg is not UNSET:
            field_dict["speed_avg"] = speed_avg
        if accel_max is not UNSET:
            field_dict["accel_max"] = accel_max
        if accel_min is not UNSET:
            field_dict["accel_min"] = accel_min
        if accel_avg is not UNSET:
            field_dict["accel_avg"] = accel_avg
        if accel_load_max is not UNSET:
            field_dict["accel_load_max"] = accel_load_max
        if accel_load_avg is not UNSET:
            field_dict["accel_load_avg"] = accel_load_avg
        if accel_load_accum is not UNSET:
            field_dict["accel_load_accum"] = accel_load_accum
        if accel_load_accum_avg_per_minute is not UNSET:
            field_dict["accel_load_accum_avg_per_minute"] = accel_load_accum_avg_per_minute
        if load_acceleration_load_category1 is not UNSET:
            field_dict["load_acceleration_load_category1"] = load_acceleration_load_category1
        if load_acceleration_load_category1_avg_per_minute is not UNSET:
            field_dict["load_acceleration_load_category1_avg_per_minute"] = (
                load_acceleration_load_category1_avg_per_minute
            )
        if load_acceleration_load_category2 is not UNSET:
            field_dict["load_acceleration_load_category2"] = load_acceleration_load_category2
        if load_acceleration_load_category2_avg_per_minute is not UNSET:
            field_dict["load_acceleration_load_category2_avg_per_minute"] = (
                load_acceleration_load_category2_avg_per_minute
            )
        if load_acceleration_load_category3 is not UNSET:
            field_dict["load_acceleration_load_category3"] = load_acceleration_load_category3
        if load_acceleration_load_category3_avg_per_minute is not UNSET:
            field_dict["load_acceleration_load_category3_avg_per_minute"] = (
                load_acceleration_load_category3_avg_per_minute
            )
        if load_acceleration_load_category4 is not UNSET:
            field_dict["load_acceleration_load_category4"] = load_acceleration_load_category4
        if load_acceleration_load_category4_avg_per_minute is not UNSET:
            field_dict["load_acceleration_load_category4_avg_per_minute"] = (
                load_acceleration_load_category4_avg_per_minute
            )
        if load_acceleration_load_category5 is not UNSET:
            field_dict["load_acceleration_load_category5"] = load_acceleration_load_category5
        if load_acceleration_load_category5_avg_per_minute is not UNSET:
            field_dict["load_acceleration_load_category5_avg_per_minute"] = (
                load_acceleration_load_category5_avg_per_minute
            )
        if load_acceleration_load_category6 is not UNSET:
            field_dict["load_acceleration_load_category6"] = load_acceleration_load_category6
        if load_acceleration_load_category6_avg_per_minute is not UNSET:
            field_dict["load_acceleration_load_category6_avg_per_minute"] = (
                load_acceleration_load_category6_avg_per_minute
            )
        if load_acceleration_load_category7 is not UNSET:
            field_dict["load_acceleration_load_category7"] = load_acceleration_load_category7
        if load_acceleration_load_category7_avg_per_minute is not UNSET:
            field_dict["load_acceleration_load_category7_avg_per_minute"] = (
                load_acceleration_load_category7_avg_per_minute
            )
        if step_balance_avg is not UNSET:
            field_dict["step_balance_avg"] = step_balance_avg
        if metabolic_power_max is not UNSET:
            field_dict["metabolic_power_max"] = metabolic_power_max
        if metabolic_power_per_mass_max is not UNSET:
            field_dict["metabolic_power_per_mass_max"] = metabolic_power_per_mass_max
        if metabolic_power_min is not UNSET:
            field_dict["metabolic_power_min"] = metabolic_power_min
        if metabolic_power_per_mass_min is not UNSET:
            field_dict["metabolic_power_per_mass_min"] = metabolic_power_per_mass_min
        if metabolic_power_avg is not UNSET:
            field_dict["metabolic_power_avg"] = metabolic_power_avg
        if metabolic_power_per_mass_avg is not UNSET:
            field_dict["metabolic_power_per_mass_avg"] = metabolic_power_per_mass_avg
        if distance_acceleration_load_category1 is not UNSET:
            field_dict["distance_acceleration_load_category1"] = distance_acceleration_load_category1
        if distance_acceleration_load_category2 is not UNSET:
            field_dict["distance_acceleration_load_category2"] = distance_acceleration_load_category2
        if distance_acceleration_load_category3 is not UNSET:
            field_dict["distance_acceleration_load_category3"] = distance_acceleration_load_category3
        if distance_acceleration_load_category4 is not UNSET:
            field_dict["distance_acceleration_load_category4"] = distance_acceleration_load_category4
        if distance_acceleration_load_category5 is not UNSET:
            field_dict["distance_acceleration_load_category5"] = distance_acceleration_load_category5
        if distance_acceleration_load_category6 is not UNSET:
            field_dict["distance_acceleration_load_category6"] = distance_acceleration_load_category6
        if distance_acceleration_load_category7 is not UNSET:
            field_dict["distance_acceleration_load_category7"] = distance_acceleration_load_category7
        if time_acceleration_load_category1 is not UNSET:
            field_dict["time_acceleration_load_category1"] = time_acceleration_load_category1
        if time_acceleration_load_category2 is not UNSET:
            field_dict["time_acceleration_load_category2"] = time_acceleration_load_category2
        if time_acceleration_load_category3 is not UNSET:
            field_dict["time_acceleration_load_category3"] = time_acceleration_load_category3
        if time_acceleration_load_category4 is not UNSET:
            field_dict["time_acceleration_load_category4"] = time_acceleration_load_category4
        if time_acceleration_load_category5 is not UNSET:
            field_dict["time_acceleration_load_category5"] = time_acceleration_load_category5
        if time_acceleration_load_category6 is not UNSET:
            field_dict["time_acceleration_load_category6"] = time_acceleration_load_category6
        if time_acceleration_load_category7 is not UNSET:
            field_dict["time_acceleration_load_category7"] = time_acceleration_load_category7
        if distance_total is not UNSET:
            field_dict["distance_total"] = distance_total
        if distance_total_avg_per_minute is not UNSET:
            field_dict["distance_total_avg_per_minute"] = distance_total_avg_per_minute
        if distance_speed_category1 is not UNSET:
            field_dict["distance_speed_category1"] = distance_speed_category1
        if distance_speed_category2 is not UNSET:
            field_dict["distance_speed_category2"] = distance_speed_category2
        if distance_speed_category3 is not UNSET:
            field_dict["distance_speed_category3"] = distance_speed_category3
        if distance_speed_category4 is not UNSET:
            field_dict["distance_speed_category4"] = distance_speed_category4
        if distance_speed_category5 is not UNSET:
            field_dict["distance_speed_category5"] = distance_speed_category5
        if distance_speed_category6 is not UNSET:
            field_dict["distance_speed_category6"] = distance_speed_category6
        if distance_speed_category7 is not UNSET:
            field_dict["distance_speed_category7"] = distance_speed_category7
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
        if distance_total_relative is not UNSET:
            field_dict["distance_total_relative"] = distance_total_relative
        if distance_total_relative_avg_per_minute is not UNSET:
            field_dict["distance_total_relative_avg_per_minute"] = distance_total_relative_avg_per_minute
        if distance_speed_relative_category1 is not UNSET:
            field_dict["distance_speed_relative_category1"] = distance_speed_relative_category1
        if distance_speed_relative_category2 is not UNSET:
            field_dict["distance_speed_relative_category2"] = distance_speed_relative_category2
        if distance_speed_relative_category3 is not UNSET:
            field_dict["distance_speed_relative_category3"] = distance_speed_relative_category3
        if distance_speed_relative_category4 is not UNSET:
            field_dict["distance_speed_relative_category4"] = distance_speed_relative_category4
        if distance_speed_relative_category5 is not UNSET:
            field_dict["distance_speed_relative_category5"] = distance_speed_relative_category5
        if distance_speed_relative_category6 is not UNSET:
            field_dict["distance_speed_relative_category6"] = distance_speed_relative_category6
        if distance_speed_relative_category7 is not UNSET:
            field_dict["distance_speed_relative_category7"] = distance_speed_relative_category7
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
        if time_total is not UNSET:
            field_dict["time_total"] = time_total
        if time_speed_category1 is not UNSET:
            field_dict["time_speed_category1"] = time_speed_category1
        if time_speed_category2 is not UNSET:
            field_dict["time_speed_category2"] = time_speed_category2
        if time_speed_category3 is not UNSET:
            field_dict["time_speed_category3"] = time_speed_category3
        if time_speed_category4 is not UNSET:
            field_dict["time_speed_category4"] = time_speed_category4
        if time_speed_category5 is not UNSET:
            field_dict["time_speed_category5"] = time_speed_category5
        if time_speed_category6 is not UNSET:
            field_dict["time_speed_category6"] = time_speed_category6
        if time_speed_category7 is not UNSET:
            field_dict["time_speed_category7"] = time_speed_category7
        if time_heart_rate_category1 is not UNSET:
            field_dict["time_heart_rate_category1"] = time_heart_rate_category1
        if time_heart_rate_category2 is not UNSET:
            field_dict["time_heart_rate_category2"] = time_heart_rate_category2
        if time_heart_rate_category3 is not UNSET:
            field_dict["time_heart_rate_category3"] = time_heart_rate_category3
        if time_heart_rate_category4 is not UNSET:
            field_dict["time_heart_rate_category4"] = time_heart_rate_category4
        if time_heart_rate_category5 is not UNSET:
            field_dict["time_heart_rate_category5"] = time_heart_rate_category5
        if time_heart_rate_category6 is not UNSET:
            field_dict["time_heart_rate_category6"] = time_heart_rate_category6
        if time_heart_rate_category7 is not UNSET:
            field_dict["time_heart_rate_category7"] = time_heart_rate_category7
        if distance_high_metabolic_load is not UNSET:
            field_dict["distance_high_metabolic_load"] = distance_high_metabolic_load
        if distance_high_metabolic_load_avg_per_minute is not UNSET:
            field_dict["distance_high_metabolic_load_avg_per_minute"] = distance_high_metabolic_load_avg_per_minute
        if distance_high_metabolic_power is not UNSET:
            field_dict["distance_high_metabolic_power"] = distance_high_metabolic_power
        if distance_high_metabolic_power_avg_per_minute is not UNSET:
            field_dict["distance_high_metabolic_power_avg_per_minute"] = distance_high_metabolic_power_avg_per_minute
        if distance_anaerobic_activity is not UNSET:
            field_dict["distance_anaerobic_activity"] = distance_anaerobic_activity
        if distance_from_steps is not UNSET:
            field_dict["distance_from_steps"] = distance_from_steps
        if distance_from_steps_avg_per_minute is not UNSET:
            field_dict["distance_from_steps_avg_per_minute"] = distance_from_steps_avg_per_minute
        if time_metabolic_power_category1 is not UNSET:
            field_dict["time_metabolic_power_category1"] = time_metabolic_power_category1
        if time_metabolic_power_category2 is not UNSET:
            field_dict["time_metabolic_power_category2"] = time_metabolic_power_category2
        if time_metabolic_power_category3 is not UNSET:
            field_dict["time_metabolic_power_category3"] = time_metabolic_power_category3
        if time_metabolic_power_category4 is not UNSET:
            field_dict["time_metabolic_power_category4"] = time_metabolic_power_category4
        if time_metabolic_power_category5 is not UNSET:
            field_dict["time_metabolic_power_category5"] = time_metabolic_power_category5
        if time_metabolic_power_category6 is not UNSET:
            field_dict["time_metabolic_power_category6"] = time_metabolic_power_category6
        if time_metabolic_power_category7 is not UNSET:
            field_dict["time_metabolic_power_category7"] = time_metabolic_power_category7
        if metabolic_work is not UNSET:
            field_dict["metabolic_work"] = metabolic_work
        if metabolic_work_avg_per_minute is not UNSET:
            field_dict["metabolic_work_avg_per_minute"] = metabolic_work_avg_per_minute
        if number_of_steps is not UNSET:
            field_dict["number_of_steps"] = number_of_steps
        if time_on_playing_field is not UNSET:
            field_dict["time_on_playing_field"] = time_on_playing_field
        if time_on_playing_field_defence is not UNSET:
            field_dict["time_on_playing_field_defence"] = time_on_playing_field_defence
        if time_on_playing_field_offence is not UNSET:
            field_dict["time_on_playing_field_offence"] = time_on_playing_field_offence
        if time_on_playing_field_pp is not UNSET:
            field_dict["time_on_playing_field_pp"] = time_on_playing_field_pp
        if time_on_playing_field_pk is not UNSET:
            field_dict["time_on_playing_field_pk"] = time_on_playing_field_pk
        if active_game_time is not UNSET:
            field_dict["active_game_time"] = active_game_time
        if jump_load is not UNSET:
            field_dict["jump_load"] = jump_load
        if jump_load_avg_per_minute is not UNSET:
            field_dict["jump_load_avg_per_minute"] = jump_load_avg_per_minute
        if jump_load_per_mass is not UNSET:
            field_dict["jump_load_per_mass"] = jump_load_per_mass
        if jump_load_per_mass_avg_per_minute is not UNSET:
            field_dict["jump_load_per_mass_avg_per_minute"] = jump_load_per_mass_avg_per_minute
        if time_ball_possession is not UNSET:
            field_dict["time_ball_possession"] = time_ball_possession
        if time_anaerobic_activity is not UNSET:
            field_dict["time_anaerobic_activity"] = time_anaerobic_activity
        if jump_height_max is not UNSET:
            field_dict["jump_height_max"] = jump_height_max
        if trimp is not UNSET:
            field_dict["trimp"] = trimp
        if heart_rate_impulse is not UNSET:
            field_dict["heart_rate_impulse"] = heart_rate_impulse
        if physio_load is not UNSET:
            field_dict["physio_load"] = physio_load
        if physio_load_speed_category1 is not UNSET:
            field_dict["physio_load_speed_category1"] = physio_load_speed_category1
        if physio_load_speed_category2 is not UNSET:
            field_dict["physio_load_speed_category2"] = physio_load_speed_category2
        if physio_load_speed_category3 is not UNSET:
            field_dict["physio_load_speed_category3"] = physio_load_speed_category3
        if physio_load_speed_category4 is not UNSET:
            field_dict["physio_load_speed_category4"] = physio_load_speed_category4
        if physio_load_speed_category5 is not UNSET:
            field_dict["physio_load_speed_category5"] = physio_load_speed_category5
        if physio_load_speed_category6 is not UNSET:
            field_dict["physio_load_speed_category6"] = physio_load_speed_category6
        if physio_load_speed_category7 is not UNSET:
            field_dict["physio_load_speed_category7"] = physio_load_speed_category7
        if physio_intensity is not UNSET:
            field_dict["physio_intensity"] = physio_intensity
        if mechanical_load is not UNSET:
            field_dict["mechanical_load"] = mechanical_load
        if mechanical_intensity is not UNSET:
            field_dict["mechanical_intensity"] = mechanical_intensity
        if mechanical_accel_total is not UNSET:
            field_dict["mechanical_accel_total"] = mechanical_accel_total
        if mechanical_accel_total_avg_per_minute is not UNSET:
            field_dict["mechanical_accel_total_avg_per_minute"] = mechanical_accel_total_avg_per_minute
        if mechanical_accel_category1 is not UNSET:
            field_dict["mechanical_accel_category1"] = mechanical_accel_category1
        if mechanical_accel_category1_avg_per_minute is not UNSET:
            field_dict["mechanical_accel_category1_avg_per_minute"] = mechanical_accel_category1_avg_per_minute
        if mechanical_accel_category2 is not UNSET:
            field_dict["mechanical_accel_category2"] = mechanical_accel_category2
        if mechanical_accel_category2_avg_per_minute is not UNSET:
            field_dict["mechanical_accel_category2_avg_per_minute"] = mechanical_accel_category2_avg_per_minute
        if mechanical_accel_category3 is not UNSET:
            field_dict["mechanical_accel_category3"] = mechanical_accel_category3
        if mechanical_accel_category3_avg_per_minute is not UNSET:
            field_dict["mechanical_accel_category3_avg_per_minute"] = mechanical_accel_category3_avg_per_minute
        if mechanical_accel_category4 is not UNSET:
            field_dict["mechanical_accel_category4"] = mechanical_accel_category4
        if mechanical_accel_category4_avg_per_minute is not UNSET:
            field_dict["mechanical_accel_category4_avg_per_minute"] = mechanical_accel_category4_avg_per_minute
        if mechanical_decel_total is not UNSET:
            field_dict["mechanical_decel_total"] = mechanical_decel_total
        if mechanical_decel_total_avg_per_minute is not UNSET:
            field_dict["mechanical_decel_total_avg_per_minute"] = mechanical_decel_total_avg_per_minute
        if mechanical_decel_category1 is not UNSET:
            field_dict["mechanical_decel_category1"] = mechanical_decel_category1
        if mechanical_decel_category1_avg_per_minute is not UNSET:
            field_dict["mechanical_decel_category1_avg_per_minute"] = mechanical_decel_category1_avg_per_minute
        if mechanical_decel_category2 is not UNSET:
            field_dict["mechanical_decel_category2"] = mechanical_decel_category2
        if mechanical_decel_category2_avg_per_minute is not UNSET:
            field_dict["mechanical_decel_category2_avg_per_minute"] = mechanical_decel_category2_avg_per_minute
        if mechanical_decel_category3 is not UNSET:
            field_dict["mechanical_decel_category3"] = mechanical_decel_category3
        if mechanical_decel_category3_avg_per_minute is not UNSET:
            field_dict["mechanical_decel_category3_avg_per_minute"] = mechanical_decel_category3_avg_per_minute
        if mechanical_decel_category4 is not UNSET:
            field_dict["mechanical_decel_category4"] = mechanical_decel_category4
        if mechanical_decel_category4_avg_per_minute is not UNSET:
            field_dict["mechanical_decel_category4_avg_per_minute"] = mechanical_decel_category4_avg_per_minute
        if data_quality is not UNSET:
            field_dict["data_quality"] = data_quality
        if data_availability is not UNSET:
            field_dict["data_availability"] = data_availability
        if mechanical_load_defence is not UNSET:
            field_dict["mechanical_load_defence"] = mechanical_load_defence
        if mechanical_load_offence is not UNSET:
            field_dict["mechanical_load_offence"] = mechanical_load_offence
        if mechanical_intensity_offence is not UNSET:
            field_dict["mechanical_intensity_offence"] = mechanical_intensity_offence
        if mechanical_intensity_defence is not UNSET:
            field_dict["mechanical_intensity_defence"] = mechanical_intensity_defence
        if playoff_load is not UNSET:
            field_dict["playoff_load"] = playoff_load
        if human_core_temperature_max is not UNSET:
            field_dict["human_core_temperature_max"] = human_core_temperature_max
        if human_core_temperature_avg is not UNSET:
            field_dict["human_core_temperature_avg"] = human_core_temperature_avg
        if time_high_metabolic_load is not UNSET:
            field_dict["time_high_metabolic_load"] = time_high_metabolic_load
        if imu_flag is not UNSET:
            field_dict["imu_flag"] = imu_flag
        if distance_forward is not UNSET:
            field_dict["distance_forward"] = distance_forward
        if distance_backward is not UNSET:
            field_dict["distance_backward"] = distance_backward
        if distance_left is not UNSET:
            field_dict["distance_left"] = distance_left
        if distance_right is not UNSET:
            field_dict["distance_right"] = distance_right
        if distance_unknown is not UNSET:
            field_dict["distance_unknown"] = distance_unknown
        if ball_contact_count is not UNSET:
            field_dict["ball_contact_count"] = ball_contact_count
        if ball_contact_count_avg_per_minute is not UNSET:
            field_dict["ball_contact_count_avg_per_minute"] = ball_contact_count_avg_per_minute
        if time_total_skating is not UNSET:
            field_dict["time_total_skating"] = time_total_skating
        if distance_total_skating is not UNSET:
            field_dict["distance_total_skating"] = distance_total_skating
        if distance_total_skating_avg_per_minute is not UNSET:
            field_dict["distance_total_skating_avg_per_minute"] = distance_total_skating_avg_per_minute
        if distance_skating_speed_category1 is not UNSET:
            field_dict["distance_skating_speed_category1"] = distance_skating_speed_category1
        if distance_skating_speed_category1_avg_per_minute is not UNSET:
            field_dict["distance_skating_speed_category1_avg_per_minute"] = (
                distance_skating_speed_category1_avg_per_minute
            )
        if distance_skating_speed_category2 is not UNSET:
            field_dict["distance_skating_speed_category2"] = distance_skating_speed_category2
        if distance_skating_speed_category2_avg_per_minute is not UNSET:
            field_dict["distance_skating_speed_category2_avg_per_minute"] = (
                distance_skating_speed_category2_avg_per_minute
            )
        if distance_skating_speed_category3 is not UNSET:
            field_dict["distance_skating_speed_category3"] = distance_skating_speed_category3
        if distance_skating_speed_category3_avg_per_minute is not UNSET:
            field_dict["distance_skating_speed_category3_avg_per_minute"] = (
                distance_skating_speed_category3_avg_per_minute
            )
        if distance_skating_speed_category4 is not UNSET:
            field_dict["distance_skating_speed_category4"] = distance_skating_speed_category4
        if distance_skating_speed_category4_avg_per_minute is not UNSET:
            field_dict["distance_skating_speed_category4_avg_per_minute"] = (
                distance_skating_speed_category4_avg_per_minute
            )
        if distance_skating_speed_category5 is not UNSET:
            field_dict["distance_skating_speed_category5"] = distance_skating_speed_category5
        if distance_skating_speed_category5_avg_per_minute is not UNSET:
            field_dict["distance_skating_speed_category5_avg_per_minute"] = (
                distance_skating_speed_category5_avg_per_minute
            )
        if distance_skating_speed_category6 is not UNSET:
            field_dict["distance_skating_speed_category6"] = distance_skating_speed_category6
        if distance_skating_speed_category6_avg_per_minute is not UNSET:
            field_dict["distance_skating_speed_category6_avg_per_minute"] = (
                distance_skating_speed_category6_avg_per_minute
            )
        if distance_skating_speed_category7 is not UNSET:
            field_dict["distance_skating_speed_category7"] = distance_skating_speed_category7
        if distance_skating_speed_category7_avg_per_minute is not UNSET:
            field_dict["distance_skating_speed_category7_avg_per_minute"] = (
                distance_skating_speed_category7_avg_per_minute
            )
        if time_total_gliding is not UNSET:
            field_dict["time_total_gliding"] = time_total_gliding
        if distance_total_gliding is not UNSET:
            field_dict["distance_total_gliding"] = distance_total_gliding
        if distance_total_gliding_avg_per_minute is not UNSET:
            field_dict["distance_total_gliding_avg_per_minute"] = distance_total_gliding_avg_per_minute
        if distance_gliding_speed_category1 is not UNSET:
            field_dict["distance_gliding_speed_category1"] = distance_gliding_speed_category1
        if distance_gliding_speed_category1_avg_per_minute is not UNSET:
            field_dict["distance_gliding_speed_category1_avg_per_minute"] = (
                distance_gliding_speed_category1_avg_per_minute
            )
        if distance_gliding_speed_category2 is not UNSET:
            field_dict["distance_gliding_speed_category2"] = distance_gliding_speed_category2
        if distance_gliding_speed_category2_avg_per_minute is not UNSET:
            field_dict["distance_gliding_speed_category2_avg_per_minute"] = (
                distance_gliding_speed_category2_avg_per_minute
            )
        if distance_gliding_speed_category3 is not UNSET:
            field_dict["distance_gliding_speed_category3"] = distance_gliding_speed_category3
        if distance_gliding_speed_category3_avg_per_minute is not UNSET:
            field_dict["distance_gliding_speed_category3_avg_per_minute"] = (
                distance_gliding_speed_category3_avg_per_minute
            )
        if distance_gliding_speed_category4 is not UNSET:
            field_dict["distance_gliding_speed_category4"] = distance_gliding_speed_category4
        if distance_gliding_speed_category4_avg_per_minute is not UNSET:
            field_dict["distance_gliding_speed_category4_avg_per_minute"] = (
                distance_gliding_speed_category4_avg_per_minute
            )
        if distance_gliding_speed_category5 is not UNSET:
            field_dict["distance_gliding_speed_category5"] = distance_gliding_speed_category5
        if distance_gliding_speed_category5_avg_per_minute is not UNSET:
            field_dict["distance_gliding_speed_category5_avg_per_minute"] = (
                distance_gliding_speed_category5_avg_per_minute
            )
        if distance_gliding_speed_category6 is not UNSET:
            field_dict["distance_gliding_speed_category6"] = distance_gliding_speed_category6
        if distance_gliding_speed_category6_avg_per_minute is not UNSET:
            field_dict["distance_gliding_speed_category6_avg_per_minute"] = (
                distance_gliding_speed_category6_avg_per_minute
            )
        if distance_gliding_speed_category7 is not UNSET:
            field_dict["distance_gliding_speed_category7"] = distance_gliding_speed_category7
        if distance_gliding_speed_category7_avg_per_minute is not UNSET:
            field_dict["distance_gliding_speed_category7_avg_per_minute"] = (
                distance_gliding_speed_category7_avg_per_minute
            )
        if time_total_standing is not UNSET:
            field_dict["time_total_standing"] = time_total_standing
        if time_imu_defective is not UNSET:
            field_dict["time_imu_defective"] = time_imu_defective
        if imu_missing_recording_ratio is not UNSET:
            field_dict["imu_missing_recording_ratio"] = imu_missing_recording_ratio

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        heart_rate_min = d.pop("heart_rate_min", UNSET)

        heart_rate_max = d.pop("heart_rate_max", UNSET)

        heart_rate_avg = d.pop("heart_rate_avg", UNSET)

        speed_max = d.pop("speed_max", UNSET)

        speed_min = d.pop("speed_min", UNSET)

        speed_avg = d.pop("speed_avg", UNSET)

        accel_max = d.pop("accel_max", UNSET)

        accel_min = d.pop("accel_min", UNSET)

        accel_avg = d.pop("accel_avg", UNSET)

        accel_load_max = d.pop("accel_load_max", UNSET)

        accel_load_avg = d.pop("accel_load_avg", UNSET)

        accel_load_accum = d.pop("accel_load_accum", UNSET)

        accel_load_accum_avg_per_minute = d.pop("accel_load_accum_avg_per_minute", UNSET)

        load_acceleration_load_category1 = d.pop("load_acceleration_load_category1", UNSET)

        load_acceleration_load_category1_avg_per_minute = d.pop(
            "load_acceleration_load_category1_avg_per_minute", UNSET
        )

        load_acceleration_load_category2 = d.pop("load_acceleration_load_category2", UNSET)

        load_acceleration_load_category2_avg_per_minute = d.pop(
            "load_acceleration_load_category2_avg_per_minute", UNSET
        )

        load_acceleration_load_category3 = d.pop("load_acceleration_load_category3", UNSET)

        load_acceleration_load_category3_avg_per_minute = d.pop(
            "load_acceleration_load_category3_avg_per_minute", UNSET
        )

        load_acceleration_load_category4 = d.pop("load_acceleration_load_category4", UNSET)

        load_acceleration_load_category4_avg_per_minute = d.pop(
            "load_acceleration_load_category4_avg_per_minute", UNSET
        )

        load_acceleration_load_category5 = d.pop("load_acceleration_load_category5", UNSET)

        load_acceleration_load_category5_avg_per_minute = d.pop(
            "load_acceleration_load_category5_avg_per_minute", UNSET
        )

        load_acceleration_load_category6 = d.pop("load_acceleration_load_category6", UNSET)

        load_acceleration_load_category6_avg_per_minute = d.pop(
            "load_acceleration_load_category6_avg_per_minute", UNSET
        )

        load_acceleration_load_category7 = d.pop("load_acceleration_load_category7", UNSET)

        load_acceleration_load_category7_avg_per_minute = d.pop(
            "load_acceleration_load_category7_avg_per_minute", UNSET
        )

        step_balance_avg = d.pop("step_balance_avg", UNSET)

        metabolic_power_max = d.pop("metabolic_power_max", UNSET)

        metabolic_power_per_mass_max = d.pop("metabolic_power_per_mass_max", UNSET)

        metabolic_power_min = d.pop("metabolic_power_min", UNSET)

        metabolic_power_per_mass_min = d.pop("metabolic_power_per_mass_min", UNSET)

        metabolic_power_avg = d.pop("metabolic_power_avg", UNSET)

        metabolic_power_per_mass_avg = d.pop("metabolic_power_per_mass_avg", UNSET)

        distance_acceleration_load_category1 = d.pop("distance_acceleration_load_category1", UNSET)

        distance_acceleration_load_category2 = d.pop("distance_acceleration_load_category2", UNSET)

        distance_acceleration_load_category3 = d.pop("distance_acceleration_load_category3", UNSET)

        distance_acceleration_load_category4 = d.pop("distance_acceleration_load_category4", UNSET)

        distance_acceleration_load_category5 = d.pop("distance_acceleration_load_category5", UNSET)

        distance_acceleration_load_category6 = d.pop("distance_acceleration_load_category6", UNSET)

        distance_acceleration_load_category7 = d.pop("distance_acceleration_load_category7", UNSET)

        time_acceleration_load_category1 = d.pop("time_acceleration_load_category1", UNSET)

        time_acceleration_load_category2 = d.pop("time_acceleration_load_category2", UNSET)

        time_acceleration_load_category3 = d.pop("time_acceleration_load_category3", UNSET)

        time_acceleration_load_category4 = d.pop("time_acceleration_load_category4", UNSET)

        time_acceleration_load_category5 = d.pop("time_acceleration_load_category5", UNSET)

        time_acceleration_load_category6 = d.pop("time_acceleration_load_category6", UNSET)

        time_acceleration_load_category7 = d.pop("time_acceleration_load_category7", UNSET)

        distance_total = d.pop("distance_total", UNSET)

        distance_total_avg_per_minute = d.pop("distance_total_avg_per_minute", UNSET)

        distance_speed_category1 = d.pop("distance_speed_category1", UNSET)

        distance_speed_category2 = d.pop("distance_speed_category2", UNSET)

        distance_speed_category3 = d.pop("distance_speed_category3", UNSET)

        distance_speed_category4 = d.pop("distance_speed_category4", UNSET)

        distance_speed_category5 = d.pop("distance_speed_category5", UNSET)

        distance_speed_category6 = d.pop("distance_speed_category6", UNSET)

        distance_speed_category7 = d.pop("distance_speed_category7", UNSET)

        distance_speed_category1_avg_per_minute = d.pop("distance_speed_category1_avg_per_minute", UNSET)

        distance_speed_category2_avg_per_minute = d.pop("distance_speed_category2_avg_per_minute", UNSET)

        distance_speed_category3_avg_per_minute = d.pop("distance_speed_category3_avg_per_minute", UNSET)

        distance_speed_category4_avg_per_minute = d.pop("distance_speed_category4_avg_per_minute", UNSET)

        distance_speed_category5_avg_per_minute = d.pop("distance_speed_category5_avg_per_minute", UNSET)

        distance_speed_category6_avg_per_minute = d.pop("distance_speed_category6_avg_per_minute", UNSET)

        distance_speed_category7_avg_per_minute = d.pop("distance_speed_category7_avg_per_minute", UNSET)

        distance_total_relative = d.pop("distance_total_relative", UNSET)

        distance_total_relative_avg_per_minute = d.pop("distance_total_relative_avg_per_minute", UNSET)

        distance_speed_relative_category1 = d.pop("distance_speed_relative_category1", UNSET)

        distance_speed_relative_category2 = d.pop("distance_speed_relative_category2", UNSET)

        distance_speed_relative_category3 = d.pop("distance_speed_relative_category3", UNSET)

        distance_speed_relative_category4 = d.pop("distance_speed_relative_category4", UNSET)

        distance_speed_relative_category5 = d.pop("distance_speed_relative_category5", UNSET)

        distance_speed_relative_category6 = d.pop("distance_speed_relative_category6", UNSET)

        distance_speed_relative_category7 = d.pop("distance_speed_relative_category7", UNSET)

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

        time_total = d.pop("time_total", UNSET)

        time_speed_category1 = d.pop("time_speed_category1", UNSET)

        time_speed_category2 = d.pop("time_speed_category2", UNSET)

        time_speed_category3 = d.pop("time_speed_category3", UNSET)

        time_speed_category4 = d.pop("time_speed_category4", UNSET)

        time_speed_category5 = d.pop("time_speed_category5", UNSET)

        time_speed_category6 = d.pop("time_speed_category6", UNSET)

        time_speed_category7 = d.pop("time_speed_category7", UNSET)

        time_heart_rate_category1 = d.pop("time_heart_rate_category1", UNSET)

        time_heart_rate_category2 = d.pop("time_heart_rate_category2", UNSET)

        time_heart_rate_category3 = d.pop("time_heart_rate_category3", UNSET)

        time_heart_rate_category4 = d.pop("time_heart_rate_category4", UNSET)

        time_heart_rate_category5 = d.pop("time_heart_rate_category5", UNSET)

        time_heart_rate_category6 = d.pop("time_heart_rate_category6", UNSET)

        time_heart_rate_category7 = d.pop("time_heart_rate_category7", UNSET)

        distance_high_metabolic_load = d.pop("distance_high_metabolic_load", UNSET)

        distance_high_metabolic_load_avg_per_minute = d.pop("distance_high_metabolic_load_avg_per_minute", UNSET)

        distance_high_metabolic_power = d.pop("distance_high_metabolic_power", UNSET)

        distance_high_metabolic_power_avg_per_minute = d.pop("distance_high_metabolic_power_avg_per_minute", UNSET)

        distance_anaerobic_activity = d.pop("distance_anaerobic_activity", UNSET)

        distance_from_steps = d.pop("distance_from_steps", UNSET)

        distance_from_steps_avg_per_minute = d.pop("distance_from_steps_avg_per_minute", UNSET)

        time_metabolic_power_category1 = d.pop("time_metabolic_power_category1", UNSET)

        time_metabolic_power_category2 = d.pop("time_metabolic_power_category2", UNSET)

        time_metabolic_power_category3 = d.pop("time_metabolic_power_category3", UNSET)

        time_metabolic_power_category4 = d.pop("time_metabolic_power_category4", UNSET)

        time_metabolic_power_category5 = d.pop("time_metabolic_power_category5", UNSET)

        time_metabolic_power_category6 = d.pop("time_metabolic_power_category6", UNSET)

        time_metabolic_power_category7 = d.pop("time_metabolic_power_category7", UNSET)

        metabolic_work = d.pop("metabolic_work", UNSET)

        metabolic_work_avg_per_minute = d.pop("metabolic_work_avg_per_minute", UNSET)

        number_of_steps = d.pop("number_of_steps", UNSET)

        time_on_playing_field = d.pop("time_on_playing_field", UNSET)

        time_on_playing_field_defence = d.pop("time_on_playing_field_defence", UNSET)

        time_on_playing_field_offence = d.pop("time_on_playing_field_offence", UNSET)

        time_on_playing_field_pp = d.pop("time_on_playing_field_pp", UNSET)

        time_on_playing_field_pk = d.pop("time_on_playing_field_pk", UNSET)

        active_game_time = d.pop("active_game_time", UNSET)

        jump_load = d.pop("jump_load", UNSET)

        jump_load_avg_per_minute = d.pop("jump_load_avg_per_minute", UNSET)

        jump_load_per_mass = d.pop("jump_load_per_mass", UNSET)

        jump_load_per_mass_avg_per_minute = d.pop("jump_load_per_mass_avg_per_minute", UNSET)

        time_ball_possession = d.pop("time_ball_possession", UNSET)

        time_anaerobic_activity = d.pop("time_anaerobic_activity", UNSET)

        jump_height_max = d.pop("jump_height_max", UNSET)

        trimp = d.pop("trimp", UNSET)

        heart_rate_impulse = d.pop("heart_rate_impulse", UNSET)

        physio_load = d.pop("physio_load", UNSET)

        physio_load_speed_category1 = d.pop("physio_load_speed_category1", UNSET)

        physio_load_speed_category2 = d.pop("physio_load_speed_category2", UNSET)

        physio_load_speed_category3 = d.pop("physio_load_speed_category3", UNSET)

        physio_load_speed_category4 = d.pop("physio_load_speed_category4", UNSET)

        physio_load_speed_category5 = d.pop("physio_load_speed_category5", UNSET)

        physio_load_speed_category6 = d.pop("physio_load_speed_category6", UNSET)

        physio_load_speed_category7 = d.pop("physio_load_speed_category7", UNSET)

        physio_intensity = d.pop("physio_intensity", UNSET)

        mechanical_load = d.pop("mechanical_load", UNSET)

        mechanical_intensity = d.pop("mechanical_intensity", UNSET)

        mechanical_accel_total = d.pop("mechanical_accel_total", UNSET)

        mechanical_accel_total_avg_per_minute = d.pop("mechanical_accel_total_avg_per_minute", UNSET)

        mechanical_accel_category1 = d.pop("mechanical_accel_category1", UNSET)

        mechanical_accel_category1_avg_per_minute = d.pop("mechanical_accel_category1_avg_per_minute", UNSET)

        mechanical_accel_category2 = d.pop("mechanical_accel_category2", UNSET)

        mechanical_accel_category2_avg_per_minute = d.pop("mechanical_accel_category2_avg_per_minute", UNSET)

        mechanical_accel_category3 = d.pop("mechanical_accel_category3", UNSET)

        mechanical_accel_category3_avg_per_minute = d.pop("mechanical_accel_category3_avg_per_minute", UNSET)

        mechanical_accel_category4 = d.pop("mechanical_accel_category4", UNSET)

        mechanical_accel_category4_avg_per_minute = d.pop("mechanical_accel_category4_avg_per_minute", UNSET)

        mechanical_decel_total = d.pop("mechanical_decel_total", UNSET)

        mechanical_decel_total_avg_per_minute = d.pop("mechanical_decel_total_avg_per_minute", UNSET)

        mechanical_decel_category1 = d.pop("mechanical_decel_category1", UNSET)

        mechanical_decel_category1_avg_per_minute = d.pop("mechanical_decel_category1_avg_per_minute", UNSET)

        mechanical_decel_category2 = d.pop("mechanical_decel_category2", UNSET)

        mechanical_decel_category2_avg_per_minute = d.pop("mechanical_decel_category2_avg_per_minute", UNSET)

        mechanical_decel_category3 = d.pop("mechanical_decel_category3", UNSET)

        mechanical_decel_category3_avg_per_minute = d.pop("mechanical_decel_category3_avg_per_minute", UNSET)

        mechanical_decel_category4 = d.pop("mechanical_decel_category4", UNSET)

        mechanical_decel_category4_avg_per_minute = d.pop("mechanical_decel_category4_avg_per_minute", UNSET)

        data_quality = d.pop("data_quality", UNSET)

        data_availability = d.pop("data_availability", UNSET)

        mechanical_load_defence = d.pop("mechanical_load_defence", UNSET)

        mechanical_load_offence = d.pop("mechanical_load_offence", UNSET)

        mechanical_intensity_offence = d.pop("mechanical_intensity_offence", UNSET)

        mechanical_intensity_defence = d.pop("mechanical_intensity_defence", UNSET)

        playoff_load = d.pop("playoff_load", UNSET)

        human_core_temperature_max = d.pop("human_core_temperature_max", UNSET)

        human_core_temperature_avg = d.pop("human_core_temperature_avg", UNSET)

        time_high_metabolic_load = d.pop("time_high_metabolic_load", UNSET)

        imu_flag = d.pop("imu_flag", UNSET)

        distance_forward = d.pop("distance_forward", UNSET)

        distance_backward = d.pop("distance_backward", UNSET)

        distance_left = d.pop("distance_left", UNSET)

        distance_right = d.pop("distance_right", UNSET)

        distance_unknown = d.pop("distance_unknown", UNSET)

        ball_contact_count = d.pop("ball_contact_count", UNSET)

        ball_contact_count_avg_per_minute = d.pop("ball_contact_count_avg_per_minute", UNSET)

        time_total_skating = d.pop("time_total_skating", UNSET)

        distance_total_skating = d.pop("distance_total_skating", UNSET)

        distance_total_skating_avg_per_minute = d.pop("distance_total_skating_avg_per_minute", UNSET)

        distance_skating_speed_category1 = d.pop("distance_skating_speed_category1", UNSET)

        distance_skating_speed_category1_avg_per_minute = d.pop(
            "distance_skating_speed_category1_avg_per_minute", UNSET
        )

        distance_skating_speed_category2 = d.pop("distance_skating_speed_category2", UNSET)

        distance_skating_speed_category2_avg_per_minute = d.pop(
            "distance_skating_speed_category2_avg_per_minute", UNSET
        )

        distance_skating_speed_category3 = d.pop("distance_skating_speed_category3", UNSET)

        distance_skating_speed_category3_avg_per_minute = d.pop(
            "distance_skating_speed_category3_avg_per_minute", UNSET
        )

        distance_skating_speed_category4 = d.pop("distance_skating_speed_category4", UNSET)

        distance_skating_speed_category4_avg_per_minute = d.pop(
            "distance_skating_speed_category4_avg_per_minute", UNSET
        )

        distance_skating_speed_category5 = d.pop("distance_skating_speed_category5", UNSET)

        distance_skating_speed_category5_avg_per_minute = d.pop(
            "distance_skating_speed_category5_avg_per_minute", UNSET
        )

        distance_skating_speed_category6 = d.pop("distance_skating_speed_category6", UNSET)

        distance_skating_speed_category6_avg_per_minute = d.pop(
            "distance_skating_speed_category6_avg_per_minute", UNSET
        )

        distance_skating_speed_category7 = d.pop("distance_skating_speed_category7", UNSET)

        distance_skating_speed_category7_avg_per_minute = d.pop(
            "distance_skating_speed_category7_avg_per_minute", UNSET
        )

        time_total_gliding = d.pop("time_total_gliding", UNSET)

        distance_total_gliding = d.pop("distance_total_gliding", UNSET)

        distance_total_gliding_avg_per_minute = d.pop("distance_total_gliding_avg_per_minute", UNSET)

        distance_gliding_speed_category1 = d.pop("distance_gliding_speed_category1", UNSET)

        distance_gliding_speed_category1_avg_per_minute = d.pop(
            "distance_gliding_speed_category1_avg_per_minute", UNSET
        )

        distance_gliding_speed_category2 = d.pop("distance_gliding_speed_category2", UNSET)

        distance_gliding_speed_category2_avg_per_minute = d.pop(
            "distance_gliding_speed_category2_avg_per_minute", UNSET
        )

        distance_gliding_speed_category3 = d.pop("distance_gliding_speed_category3", UNSET)

        distance_gliding_speed_category3_avg_per_minute = d.pop(
            "distance_gliding_speed_category3_avg_per_minute", UNSET
        )

        distance_gliding_speed_category4 = d.pop("distance_gliding_speed_category4", UNSET)

        distance_gliding_speed_category4_avg_per_minute = d.pop(
            "distance_gliding_speed_category4_avg_per_minute", UNSET
        )

        distance_gliding_speed_category5 = d.pop("distance_gliding_speed_category5", UNSET)

        distance_gliding_speed_category5_avg_per_minute = d.pop(
            "distance_gliding_speed_category5_avg_per_minute", UNSET
        )

        distance_gliding_speed_category6 = d.pop("distance_gliding_speed_category6", UNSET)

        distance_gliding_speed_category6_avg_per_minute = d.pop(
            "distance_gliding_speed_category6_avg_per_minute", UNSET
        )

        distance_gliding_speed_category7 = d.pop("distance_gliding_speed_category7", UNSET)

        distance_gliding_speed_category7_avg_per_minute = d.pop(
            "distance_gliding_speed_category7_avg_per_minute", UNSET
        )

        time_total_standing = d.pop("time_total_standing", UNSET)

        time_imu_defective = d.pop("time_imu_defective", UNSET)

        imu_missing_recording_ratio = d.pop("imu_missing_recording_ratio", UNSET)

        player_statistic = cls(
            heart_rate_min=heart_rate_min,
            heart_rate_max=heart_rate_max,
            heart_rate_avg=heart_rate_avg,
            speed_max=speed_max,
            speed_min=speed_min,
            speed_avg=speed_avg,
            accel_max=accel_max,
            accel_min=accel_min,
            accel_avg=accel_avg,
            accel_load_max=accel_load_max,
            accel_load_avg=accel_load_avg,
            accel_load_accum=accel_load_accum,
            accel_load_accum_avg_per_minute=accel_load_accum_avg_per_minute,
            load_acceleration_load_category1=load_acceleration_load_category1,
            load_acceleration_load_category1_avg_per_minute=load_acceleration_load_category1_avg_per_minute,
            load_acceleration_load_category2=load_acceleration_load_category2,
            load_acceleration_load_category2_avg_per_minute=load_acceleration_load_category2_avg_per_minute,
            load_acceleration_load_category3=load_acceleration_load_category3,
            load_acceleration_load_category3_avg_per_minute=load_acceleration_load_category3_avg_per_minute,
            load_acceleration_load_category4=load_acceleration_load_category4,
            load_acceleration_load_category4_avg_per_minute=load_acceleration_load_category4_avg_per_minute,
            load_acceleration_load_category5=load_acceleration_load_category5,
            load_acceleration_load_category5_avg_per_minute=load_acceleration_load_category5_avg_per_minute,
            load_acceleration_load_category6=load_acceleration_load_category6,
            load_acceleration_load_category6_avg_per_minute=load_acceleration_load_category6_avg_per_minute,
            load_acceleration_load_category7=load_acceleration_load_category7,
            load_acceleration_load_category7_avg_per_minute=load_acceleration_load_category7_avg_per_minute,
            step_balance_avg=step_balance_avg,
            metabolic_power_max=metabolic_power_max,
            metabolic_power_per_mass_max=metabolic_power_per_mass_max,
            metabolic_power_min=metabolic_power_min,
            metabolic_power_per_mass_min=metabolic_power_per_mass_min,
            metabolic_power_avg=metabolic_power_avg,
            metabolic_power_per_mass_avg=metabolic_power_per_mass_avg,
            distance_acceleration_load_category1=distance_acceleration_load_category1,
            distance_acceleration_load_category2=distance_acceleration_load_category2,
            distance_acceleration_load_category3=distance_acceleration_load_category3,
            distance_acceleration_load_category4=distance_acceleration_load_category4,
            distance_acceleration_load_category5=distance_acceleration_load_category5,
            distance_acceleration_load_category6=distance_acceleration_load_category6,
            distance_acceleration_load_category7=distance_acceleration_load_category7,
            time_acceleration_load_category1=time_acceleration_load_category1,
            time_acceleration_load_category2=time_acceleration_load_category2,
            time_acceleration_load_category3=time_acceleration_load_category3,
            time_acceleration_load_category4=time_acceleration_load_category4,
            time_acceleration_load_category5=time_acceleration_load_category5,
            time_acceleration_load_category6=time_acceleration_load_category6,
            time_acceleration_load_category7=time_acceleration_load_category7,
            distance_total=distance_total,
            distance_total_avg_per_minute=distance_total_avg_per_minute,
            distance_speed_category1=distance_speed_category1,
            distance_speed_category2=distance_speed_category2,
            distance_speed_category3=distance_speed_category3,
            distance_speed_category4=distance_speed_category4,
            distance_speed_category5=distance_speed_category5,
            distance_speed_category6=distance_speed_category6,
            distance_speed_category7=distance_speed_category7,
            distance_speed_category1_avg_per_minute=distance_speed_category1_avg_per_minute,
            distance_speed_category2_avg_per_minute=distance_speed_category2_avg_per_minute,
            distance_speed_category3_avg_per_minute=distance_speed_category3_avg_per_minute,
            distance_speed_category4_avg_per_minute=distance_speed_category4_avg_per_minute,
            distance_speed_category5_avg_per_minute=distance_speed_category5_avg_per_minute,
            distance_speed_category6_avg_per_minute=distance_speed_category6_avg_per_minute,
            distance_speed_category7_avg_per_minute=distance_speed_category7_avg_per_minute,
            distance_total_relative=distance_total_relative,
            distance_total_relative_avg_per_minute=distance_total_relative_avg_per_minute,
            distance_speed_relative_category1=distance_speed_relative_category1,
            distance_speed_relative_category2=distance_speed_relative_category2,
            distance_speed_relative_category3=distance_speed_relative_category3,
            distance_speed_relative_category4=distance_speed_relative_category4,
            distance_speed_relative_category5=distance_speed_relative_category5,
            distance_speed_relative_category6=distance_speed_relative_category6,
            distance_speed_relative_category7=distance_speed_relative_category7,
            distance_speed_relative_category1_avg_per_minute=distance_speed_relative_category1_avg_per_minute,
            distance_speed_relative_category2_avg_per_minute=distance_speed_relative_category2_avg_per_minute,
            distance_speed_relative_category3_avg_per_minute=distance_speed_relative_category3_avg_per_minute,
            distance_speed_relative_category4_avg_per_minute=distance_speed_relative_category4_avg_per_minute,
            distance_speed_relative_category5_avg_per_minute=distance_speed_relative_category5_avg_per_minute,
            distance_speed_relative_category6_avg_per_minute=distance_speed_relative_category6_avg_per_minute,
            distance_speed_relative_category7_avg_per_minute=distance_speed_relative_category7_avg_per_minute,
            time_total=time_total,
            time_speed_category1=time_speed_category1,
            time_speed_category2=time_speed_category2,
            time_speed_category3=time_speed_category3,
            time_speed_category4=time_speed_category4,
            time_speed_category5=time_speed_category5,
            time_speed_category6=time_speed_category6,
            time_speed_category7=time_speed_category7,
            time_heart_rate_category1=time_heart_rate_category1,
            time_heart_rate_category2=time_heart_rate_category2,
            time_heart_rate_category3=time_heart_rate_category3,
            time_heart_rate_category4=time_heart_rate_category4,
            time_heart_rate_category5=time_heart_rate_category5,
            time_heart_rate_category6=time_heart_rate_category6,
            time_heart_rate_category7=time_heart_rate_category7,
            distance_high_metabolic_load=distance_high_metabolic_load,
            distance_high_metabolic_load_avg_per_minute=distance_high_metabolic_load_avg_per_minute,
            distance_high_metabolic_power=distance_high_metabolic_power,
            distance_high_metabolic_power_avg_per_minute=distance_high_metabolic_power_avg_per_minute,
            distance_anaerobic_activity=distance_anaerobic_activity,
            distance_from_steps=distance_from_steps,
            distance_from_steps_avg_per_minute=distance_from_steps_avg_per_minute,
            time_metabolic_power_category1=time_metabolic_power_category1,
            time_metabolic_power_category2=time_metabolic_power_category2,
            time_metabolic_power_category3=time_metabolic_power_category3,
            time_metabolic_power_category4=time_metabolic_power_category4,
            time_metabolic_power_category5=time_metabolic_power_category5,
            time_metabolic_power_category6=time_metabolic_power_category6,
            time_metabolic_power_category7=time_metabolic_power_category7,
            metabolic_work=metabolic_work,
            metabolic_work_avg_per_minute=metabolic_work_avg_per_minute,
            number_of_steps=number_of_steps,
            time_on_playing_field=time_on_playing_field,
            time_on_playing_field_defence=time_on_playing_field_defence,
            time_on_playing_field_offence=time_on_playing_field_offence,
            time_on_playing_field_pp=time_on_playing_field_pp,
            time_on_playing_field_pk=time_on_playing_field_pk,
            active_game_time=active_game_time,
            jump_load=jump_load,
            jump_load_avg_per_minute=jump_load_avg_per_minute,
            jump_load_per_mass=jump_load_per_mass,
            jump_load_per_mass_avg_per_minute=jump_load_per_mass_avg_per_minute,
            time_ball_possession=time_ball_possession,
            time_anaerobic_activity=time_anaerobic_activity,
            jump_height_max=jump_height_max,
            trimp=trimp,
            heart_rate_impulse=heart_rate_impulse,
            physio_load=physio_load,
            physio_load_speed_category1=physio_load_speed_category1,
            physio_load_speed_category2=physio_load_speed_category2,
            physio_load_speed_category3=physio_load_speed_category3,
            physio_load_speed_category4=physio_load_speed_category4,
            physio_load_speed_category5=physio_load_speed_category5,
            physio_load_speed_category6=physio_load_speed_category6,
            physio_load_speed_category7=physio_load_speed_category7,
            physio_intensity=physio_intensity,
            mechanical_load=mechanical_load,
            mechanical_intensity=mechanical_intensity,
            mechanical_accel_total=mechanical_accel_total,
            mechanical_accel_total_avg_per_minute=mechanical_accel_total_avg_per_minute,
            mechanical_accel_category1=mechanical_accel_category1,
            mechanical_accel_category1_avg_per_minute=mechanical_accel_category1_avg_per_minute,
            mechanical_accel_category2=mechanical_accel_category2,
            mechanical_accel_category2_avg_per_minute=mechanical_accel_category2_avg_per_minute,
            mechanical_accel_category3=mechanical_accel_category3,
            mechanical_accel_category3_avg_per_minute=mechanical_accel_category3_avg_per_minute,
            mechanical_accel_category4=mechanical_accel_category4,
            mechanical_accel_category4_avg_per_minute=mechanical_accel_category4_avg_per_minute,
            mechanical_decel_total=mechanical_decel_total,
            mechanical_decel_total_avg_per_minute=mechanical_decel_total_avg_per_minute,
            mechanical_decel_category1=mechanical_decel_category1,
            mechanical_decel_category1_avg_per_minute=mechanical_decel_category1_avg_per_minute,
            mechanical_decel_category2=mechanical_decel_category2,
            mechanical_decel_category2_avg_per_minute=mechanical_decel_category2_avg_per_minute,
            mechanical_decel_category3=mechanical_decel_category3,
            mechanical_decel_category3_avg_per_minute=mechanical_decel_category3_avg_per_minute,
            mechanical_decel_category4=mechanical_decel_category4,
            mechanical_decel_category4_avg_per_minute=mechanical_decel_category4_avg_per_minute,
            data_quality=data_quality,
            data_availability=data_availability,
            mechanical_load_defence=mechanical_load_defence,
            mechanical_load_offence=mechanical_load_offence,
            mechanical_intensity_offence=mechanical_intensity_offence,
            mechanical_intensity_defence=mechanical_intensity_defence,
            playoff_load=playoff_load,
            human_core_temperature_max=human_core_temperature_max,
            human_core_temperature_avg=human_core_temperature_avg,
            time_high_metabolic_load=time_high_metabolic_load,
            imu_flag=imu_flag,
            distance_forward=distance_forward,
            distance_backward=distance_backward,
            distance_left=distance_left,
            distance_right=distance_right,
            distance_unknown=distance_unknown,
            ball_contact_count=ball_contact_count,
            ball_contact_count_avg_per_minute=ball_contact_count_avg_per_minute,
            time_total_skating=time_total_skating,
            distance_total_skating=distance_total_skating,
            distance_total_skating_avg_per_minute=distance_total_skating_avg_per_minute,
            distance_skating_speed_category1=distance_skating_speed_category1,
            distance_skating_speed_category1_avg_per_minute=distance_skating_speed_category1_avg_per_minute,
            distance_skating_speed_category2=distance_skating_speed_category2,
            distance_skating_speed_category2_avg_per_minute=distance_skating_speed_category2_avg_per_minute,
            distance_skating_speed_category3=distance_skating_speed_category3,
            distance_skating_speed_category3_avg_per_minute=distance_skating_speed_category3_avg_per_minute,
            distance_skating_speed_category4=distance_skating_speed_category4,
            distance_skating_speed_category4_avg_per_minute=distance_skating_speed_category4_avg_per_minute,
            distance_skating_speed_category5=distance_skating_speed_category5,
            distance_skating_speed_category5_avg_per_minute=distance_skating_speed_category5_avg_per_minute,
            distance_skating_speed_category6=distance_skating_speed_category6,
            distance_skating_speed_category6_avg_per_minute=distance_skating_speed_category6_avg_per_minute,
            distance_skating_speed_category7=distance_skating_speed_category7,
            distance_skating_speed_category7_avg_per_minute=distance_skating_speed_category7_avg_per_minute,
            time_total_gliding=time_total_gliding,
            distance_total_gliding=distance_total_gliding,
            distance_total_gliding_avg_per_minute=distance_total_gliding_avg_per_minute,
            distance_gliding_speed_category1=distance_gliding_speed_category1,
            distance_gliding_speed_category1_avg_per_minute=distance_gliding_speed_category1_avg_per_minute,
            distance_gliding_speed_category2=distance_gliding_speed_category2,
            distance_gliding_speed_category2_avg_per_minute=distance_gliding_speed_category2_avg_per_minute,
            distance_gliding_speed_category3=distance_gliding_speed_category3,
            distance_gliding_speed_category3_avg_per_minute=distance_gliding_speed_category3_avg_per_minute,
            distance_gliding_speed_category4=distance_gliding_speed_category4,
            distance_gliding_speed_category4_avg_per_minute=distance_gliding_speed_category4_avg_per_minute,
            distance_gliding_speed_category5=distance_gliding_speed_category5,
            distance_gliding_speed_category5_avg_per_minute=distance_gliding_speed_category5_avg_per_minute,
            distance_gliding_speed_category6=distance_gliding_speed_category6,
            distance_gliding_speed_category6_avg_per_minute=distance_gliding_speed_category6_avg_per_minute,
            distance_gliding_speed_category7=distance_gliding_speed_category7,
            distance_gliding_speed_category7_avg_per_minute=distance_gliding_speed_category7_avg_per_minute,
            time_total_standing=time_total_standing,
            time_imu_defective=time_imu_defective,
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
