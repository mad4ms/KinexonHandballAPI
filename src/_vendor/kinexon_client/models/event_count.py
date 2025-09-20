from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventCount")


@_attrs_define
class EventCount:
    """
    Attributes:
        count_acceleration (Union[Unset, int]):
        count_ball_contact (Union[Unset, int]):
        count_ball_possession (Union[Unset, int]):
        count_ball_possession_lost (Union[Unset, int]):
        count_ball_possession_recovery (Union[Unset, int]):
        count_cv_shot (Union[Unset, int]):
        count_change_of_direction (Union[Unset, int]):
        count_change_of_orientation (Union[Unset, int]):
        count_change_of_pace (Union[Unset, int]):
        count_corner_kick (Union[Unset, int]):
        count_counter_attack (Union[Unset, int]):
        count_detected_cross (Union[Unset, int]):
        count_cut (Union[Unset, int]):
        count_deceleration (Union[Unset, int]):
        count_defence (Union[Unset, int]):
        count_detected_offside_soccer (Union[Unset, int]):
        count_detected_pass (Union[Unset, int]):
        count_detected_shot_basketball (Union[Unset, int]):
        count_detected_shot_fifa (Union[Unset, int]):
        count_detected_shot_handball (Union[Unset, int]):
        count_detected_shot_ice_hockey (Union[Unset, int]):
        count_detected_shot_intelligence_court (Union[Unset, int]):
        count_detected_shot_soccer (Union[Unset, int]):
        count_dfl_corner_kick (Union[Unset, int]):
        count_dfl_cross (Union[Unset, int]):
        count_dfl_free_kick (Union[Unset, int]):
        count_dfl_goal_kick (Union[Unset, int]):
        count_dfl_kick_off (Union[Unset, int]):
        count_dfl_pass (Union[Unset, int]):
        count_dfl_penalty (Union[Unset, int]):
        count_dfl_shot_at_goal (Union[Unset, int]):
        count_dfl_sprint (Union[Unset, int]):
        count_dfl_tackling (Union[Unset, int]):
        count_dfl_throw_in (Union[Unset, int]):
        count_down_on_pads (Union[Unset, int]):
        count_dribbling_soccer (Union[Unset, int]):
        count_dynamic_defence (Union[Unset, int]):
        count_exertion (Union[Unset, int]):
        count_full_court_transition (Union[Unset, int]):
        count_goal_kick (Union[Unset, int]):
        count_goalkeeper_save_diving (Union[Unset, int]):
        count_goalkeeper_save_down_to_knees (Union[Unset, int]):
        count_goalkeeper_save_tilting (Union[Unset, int]):
        count_group_counter_pressing (Union[Unset, int]):
        count_group_empty_goal_handball (Union[Unset, int]):
        count_heart_rate_recovery (Union[Unset, int]):
        count_impact (Union[Unset, int]):
        count_jump_beach_volleyball (Union[Unset, int]):
        count_jump (Union[Unset, int]):
        count_mid_court_transition (Union[Unset, int]):
        count_noah_shot (Union[Unset, int]):
        count_offence (Union[Unset, int]):
        count_pass_fifa (Union[Unset, int]):
        count_pick_and_pop (Union[Unset, int]):
        count_pick_and_roll (Union[Unset, int]):
        count_pivot_rotation (Union[Unset, int]):
        count_play_by_player (Union[Unset, int]):
        count_play_by_team (Union[Unset, int]):
        count_player_counter_pressing (Union[Unset, int]):
        count_rally_beach_volleyball (Union[Unset, int]):
        count_rspct_shot (Union[Unset, int]):
        count_shift (Union[Unset, int]):
        count_skating_transition (Union[Unset, int]):
        count_speed_zone_entry (Union[Unset, int]):
        count_speed_zone_entry_relative (Union[Unset, int]):
        count_sprint (Union[Unset, int]):
        count_tag (Union[Unset, int]):
        count_tempo_run (Union[Unset, int]):
        count_throw_in (Union[Unset, int]):
        count_turn_ice_hockey (Union[Unset, int]):
    """

    count_acceleration: Union[Unset, int] = UNSET
    count_ball_contact: Union[Unset, int] = UNSET
    count_ball_possession: Union[Unset, int] = UNSET
    count_ball_possession_lost: Union[Unset, int] = UNSET
    count_ball_possession_recovery: Union[Unset, int] = UNSET
    count_cv_shot: Union[Unset, int] = UNSET
    count_change_of_direction: Union[Unset, int] = UNSET
    count_change_of_orientation: Union[Unset, int] = UNSET
    count_change_of_pace: Union[Unset, int] = UNSET
    count_corner_kick: Union[Unset, int] = UNSET
    count_counter_attack: Union[Unset, int] = UNSET
    count_detected_cross: Union[Unset, int] = UNSET
    count_cut: Union[Unset, int] = UNSET
    count_deceleration: Union[Unset, int] = UNSET
    count_defence: Union[Unset, int] = UNSET
    count_detected_offside_soccer: Union[Unset, int] = UNSET
    count_detected_pass: Union[Unset, int] = UNSET
    count_detected_shot_basketball: Union[Unset, int] = UNSET
    count_detected_shot_fifa: Union[Unset, int] = UNSET
    count_detected_shot_handball: Union[Unset, int] = UNSET
    count_detected_shot_ice_hockey: Union[Unset, int] = UNSET
    count_detected_shot_intelligence_court: Union[Unset, int] = UNSET
    count_detected_shot_soccer: Union[Unset, int] = UNSET
    count_dfl_corner_kick: Union[Unset, int] = UNSET
    count_dfl_cross: Union[Unset, int] = UNSET
    count_dfl_free_kick: Union[Unset, int] = UNSET
    count_dfl_goal_kick: Union[Unset, int] = UNSET
    count_dfl_kick_off: Union[Unset, int] = UNSET
    count_dfl_pass: Union[Unset, int] = UNSET
    count_dfl_penalty: Union[Unset, int] = UNSET
    count_dfl_shot_at_goal: Union[Unset, int] = UNSET
    count_dfl_sprint: Union[Unset, int] = UNSET
    count_dfl_tackling: Union[Unset, int] = UNSET
    count_dfl_throw_in: Union[Unset, int] = UNSET
    count_down_on_pads: Union[Unset, int] = UNSET
    count_dribbling_soccer: Union[Unset, int] = UNSET
    count_dynamic_defence: Union[Unset, int] = UNSET
    count_exertion: Union[Unset, int] = UNSET
    count_full_court_transition: Union[Unset, int] = UNSET
    count_goal_kick: Union[Unset, int] = UNSET
    count_goalkeeper_save_diving: Union[Unset, int] = UNSET
    count_goalkeeper_save_down_to_knees: Union[Unset, int] = UNSET
    count_goalkeeper_save_tilting: Union[Unset, int] = UNSET
    count_group_counter_pressing: Union[Unset, int] = UNSET
    count_group_empty_goal_handball: Union[Unset, int] = UNSET
    count_heart_rate_recovery: Union[Unset, int] = UNSET
    count_impact: Union[Unset, int] = UNSET
    count_jump_beach_volleyball: Union[Unset, int] = UNSET
    count_jump: Union[Unset, int] = UNSET
    count_mid_court_transition: Union[Unset, int] = UNSET
    count_noah_shot: Union[Unset, int] = UNSET
    count_offence: Union[Unset, int] = UNSET
    count_pass_fifa: Union[Unset, int] = UNSET
    count_pick_and_pop: Union[Unset, int] = UNSET
    count_pick_and_roll: Union[Unset, int] = UNSET
    count_pivot_rotation: Union[Unset, int] = UNSET
    count_play_by_player: Union[Unset, int] = UNSET
    count_play_by_team: Union[Unset, int] = UNSET
    count_player_counter_pressing: Union[Unset, int] = UNSET
    count_rally_beach_volleyball: Union[Unset, int] = UNSET
    count_rspct_shot: Union[Unset, int] = UNSET
    count_shift: Union[Unset, int] = UNSET
    count_skating_transition: Union[Unset, int] = UNSET
    count_speed_zone_entry: Union[Unset, int] = UNSET
    count_speed_zone_entry_relative: Union[Unset, int] = UNSET
    count_sprint: Union[Unset, int] = UNSET
    count_tag: Union[Unset, int] = UNSET
    count_tempo_run: Union[Unset, int] = UNSET
    count_throw_in: Union[Unset, int] = UNSET
    count_turn_ice_hockey: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count_acceleration = self.count_acceleration

        count_ball_contact = self.count_ball_contact

        count_ball_possession = self.count_ball_possession

        count_ball_possession_lost = self.count_ball_possession_lost

        count_ball_possession_recovery = self.count_ball_possession_recovery

        count_cv_shot = self.count_cv_shot

        count_change_of_direction = self.count_change_of_direction

        count_change_of_orientation = self.count_change_of_orientation

        count_change_of_pace = self.count_change_of_pace

        count_corner_kick = self.count_corner_kick

        count_counter_attack = self.count_counter_attack

        count_detected_cross = self.count_detected_cross

        count_cut = self.count_cut

        count_deceleration = self.count_deceleration

        count_defence = self.count_defence

        count_detected_offside_soccer = self.count_detected_offside_soccer

        count_detected_pass = self.count_detected_pass

        count_detected_shot_basketball = self.count_detected_shot_basketball

        count_detected_shot_fifa = self.count_detected_shot_fifa

        count_detected_shot_handball = self.count_detected_shot_handball

        count_detected_shot_ice_hockey = self.count_detected_shot_ice_hockey

        count_detected_shot_intelligence_court = self.count_detected_shot_intelligence_court

        count_detected_shot_soccer = self.count_detected_shot_soccer

        count_dfl_corner_kick = self.count_dfl_corner_kick

        count_dfl_cross = self.count_dfl_cross

        count_dfl_free_kick = self.count_dfl_free_kick

        count_dfl_goal_kick = self.count_dfl_goal_kick

        count_dfl_kick_off = self.count_dfl_kick_off

        count_dfl_pass = self.count_dfl_pass

        count_dfl_penalty = self.count_dfl_penalty

        count_dfl_shot_at_goal = self.count_dfl_shot_at_goal

        count_dfl_sprint = self.count_dfl_sprint

        count_dfl_tackling = self.count_dfl_tackling

        count_dfl_throw_in = self.count_dfl_throw_in

        count_down_on_pads = self.count_down_on_pads

        count_dribbling_soccer = self.count_dribbling_soccer

        count_dynamic_defence = self.count_dynamic_defence

        count_exertion = self.count_exertion

        count_full_court_transition = self.count_full_court_transition

        count_goal_kick = self.count_goal_kick

        count_goalkeeper_save_diving = self.count_goalkeeper_save_diving

        count_goalkeeper_save_down_to_knees = self.count_goalkeeper_save_down_to_knees

        count_goalkeeper_save_tilting = self.count_goalkeeper_save_tilting

        count_group_counter_pressing = self.count_group_counter_pressing

        count_group_empty_goal_handball = self.count_group_empty_goal_handball

        count_heart_rate_recovery = self.count_heart_rate_recovery

        count_impact = self.count_impact

        count_jump_beach_volleyball = self.count_jump_beach_volleyball

        count_jump = self.count_jump

        count_mid_court_transition = self.count_mid_court_transition

        count_noah_shot = self.count_noah_shot

        count_offence = self.count_offence

        count_pass_fifa = self.count_pass_fifa

        count_pick_and_pop = self.count_pick_and_pop

        count_pick_and_roll = self.count_pick_and_roll

        count_pivot_rotation = self.count_pivot_rotation

        count_play_by_player = self.count_play_by_player

        count_play_by_team = self.count_play_by_team

        count_player_counter_pressing = self.count_player_counter_pressing

        count_rally_beach_volleyball = self.count_rally_beach_volleyball

        count_rspct_shot = self.count_rspct_shot

        count_shift = self.count_shift

        count_skating_transition = self.count_skating_transition

        count_speed_zone_entry = self.count_speed_zone_entry

        count_speed_zone_entry_relative = self.count_speed_zone_entry_relative

        count_sprint = self.count_sprint

        count_tag = self.count_tag

        count_tempo_run = self.count_tempo_run

        count_throw_in = self.count_throw_in

        count_turn_ice_hockey = self.count_turn_ice_hockey

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count_acceleration is not UNSET:
            field_dict["count_acceleration"] = count_acceleration
        if count_ball_contact is not UNSET:
            field_dict["count_ball_contact"] = count_ball_contact
        if count_ball_possession is not UNSET:
            field_dict["count_ball_possession"] = count_ball_possession
        if count_ball_possession_lost is not UNSET:
            field_dict["count_ball_possession_lost"] = count_ball_possession_lost
        if count_ball_possession_recovery is not UNSET:
            field_dict["count_ball_possession_recovery"] = count_ball_possession_recovery
        if count_cv_shot is not UNSET:
            field_dict["count_cv_shot"] = count_cv_shot
        if count_change_of_direction is not UNSET:
            field_dict["count_change_of_direction"] = count_change_of_direction
        if count_change_of_orientation is not UNSET:
            field_dict["count_change_of_orientation"] = count_change_of_orientation
        if count_change_of_pace is not UNSET:
            field_dict["count_change_of_pace"] = count_change_of_pace
        if count_corner_kick is not UNSET:
            field_dict["count_corner_kick"] = count_corner_kick
        if count_counter_attack is not UNSET:
            field_dict["count_counter_attack"] = count_counter_attack
        if count_detected_cross is not UNSET:
            field_dict["count_detected_cross"] = count_detected_cross
        if count_cut is not UNSET:
            field_dict["count_cut"] = count_cut
        if count_deceleration is not UNSET:
            field_dict["count_deceleration"] = count_deceleration
        if count_defence is not UNSET:
            field_dict["count_defence"] = count_defence
        if count_detected_offside_soccer is not UNSET:
            field_dict["count_detected_offside_soccer"] = count_detected_offside_soccer
        if count_detected_pass is not UNSET:
            field_dict["count_detected_pass"] = count_detected_pass
        if count_detected_shot_basketball is not UNSET:
            field_dict["count_detected_shot_basketball"] = count_detected_shot_basketball
        if count_detected_shot_fifa is not UNSET:
            field_dict["count_detected_shot_fifa"] = count_detected_shot_fifa
        if count_detected_shot_handball is not UNSET:
            field_dict["count_detected_shot_handball"] = count_detected_shot_handball
        if count_detected_shot_ice_hockey is not UNSET:
            field_dict["count_detected_shot_ice_hockey"] = count_detected_shot_ice_hockey
        if count_detected_shot_intelligence_court is not UNSET:
            field_dict["count_detected_shot_intelligence_court"] = count_detected_shot_intelligence_court
        if count_detected_shot_soccer is not UNSET:
            field_dict["count_detected_shot_soccer"] = count_detected_shot_soccer
        if count_dfl_corner_kick is not UNSET:
            field_dict["count_dfl_corner_kick"] = count_dfl_corner_kick
        if count_dfl_cross is not UNSET:
            field_dict["count_dfl_cross"] = count_dfl_cross
        if count_dfl_free_kick is not UNSET:
            field_dict["count_dfl_free_kick"] = count_dfl_free_kick
        if count_dfl_goal_kick is not UNSET:
            field_dict["count_dfl_goal_kick"] = count_dfl_goal_kick
        if count_dfl_kick_off is not UNSET:
            field_dict["count_dfl_kick_off"] = count_dfl_kick_off
        if count_dfl_pass is not UNSET:
            field_dict["count_dfl_pass"] = count_dfl_pass
        if count_dfl_penalty is not UNSET:
            field_dict["count_dfl_penalty"] = count_dfl_penalty
        if count_dfl_shot_at_goal is not UNSET:
            field_dict["count_dfl_shot_at_goal"] = count_dfl_shot_at_goal
        if count_dfl_sprint is not UNSET:
            field_dict["count_dfl_sprint"] = count_dfl_sprint
        if count_dfl_tackling is not UNSET:
            field_dict["count_dfl_tackling"] = count_dfl_tackling
        if count_dfl_throw_in is not UNSET:
            field_dict["count_dfl_throw_in"] = count_dfl_throw_in
        if count_down_on_pads is not UNSET:
            field_dict["count_down_on_pads"] = count_down_on_pads
        if count_dribbling_soccer is not UNSET:
            field_dict["count_dribbling_soccer"] = count_dribbling_soccer
        if count_dynamic_defence is not UNSET:
            field_dict["count_dynamic_defence"] = count_dynamic_defence
        if count_exertion is not UNSET:
            field_dict["count_exertion"] = count_exertion
        if count_full_court_transition is not UNSET:
            field_dict["count_full_court_transition"] = count_full_court_transition
        if count_goal_kick is not UNSET:
            field_dict["count_goal_kick"] = count_goal_kick
        if count_goalkeeper_save_diving is not UNSET:
            field_dict["count_goalkeeper_save_diving"] = count_goalkeeper_save_diving
        if count_goalkeeper_save_down_to_knees is not UNSET:
            field_dict["count_goalkeeper_save_down_to_knees"] = count_goalkeeper_save_down_to_knees
        if count_goalkeeper_save_tilting is not UNSET:
            field_dict["count_goalkeeper_save_tilting"] = count_goalkeeper_save_tilting
        if count_group_counter_pressing is not UNSET:
            field_dict["count_group_counter_pressing"] = count_group_counter_pressing
        if count_group_empty_goal_handball is not UNSET:
            field_dict["count_group_empty_goal_handball"] = count_group_empty_goal_handball
        if count_heart_rate_recovery is not UNSET:
            field_dict["count_heart_rate_recovery"] = count_heart_rate_recovery
        if count_impact is not UNSET:
            field_dict["count_impact"] = count_impact
        if count_jump_beach_volleyball is not UNSET:
            field_dict["count_jump_beach_volleyball"] = count_jump_beach_volleyball
        if count_jump is not UNSET:
            field_dict["count_jump"] = count_jump
        if count_mid_court_transition is not UNSET:
            field_dict["count_mid_court_transition"] = count_mid_court_transition
        if count_noah_shot is not UNSET:
            field_dict["count_noah_shot"] = count_noah_shot
        if count_offence is not UNSET:
            field_dict["count_offence"] = count_offence
        if count_pass_fifa is not UNSET:
            field_dict["count_pass_fifa"] = count_pass_fifa
        if count_pick_and_pop is not UNSET:
            field_dict["count_pick_and_pop"] = count_pick_and_pop
        if count_pick_and_roll is not UNSET:
            field_dict["count_pick_and_roll"] = count_pick_and_roll
        if count_pivot_rotation is not UNSET:
            field_dict["count_pivot_rotation"] = count_pivot_rotation
        if count_play_by_player is not UNSET:
            field_dict["count_play_by_player"] = count_play_by_player
        if count_play_by_team is not UNSET:
            field_dict["count_play_by_team"] = count_play_by_team
        if count_player_counter_pressing is not UNSET:
            field_dict["count_player_counter_pressing"] = count_player_counter_pressing
        if count_rally_beach_volleyball is not UNSET:
            field_dict["count_rally_beach_volleyball"] = count_rally_beach_volleyball
        if count_rspct_shot is not UNSET:
            field_dict["count_rspct_shot"] = count_rspct_shot
        if count_shift is not UNSET:
            field_dict["count_shift"] = count_shift
        if count_skating_transition is not UNSET:
            field_dict["count_skating_transition"] = count_skating_transition
        if count_speed_zone_entry is not UNSET:
            field_dict["count_speed_zone_entry"] = count_speed_zone_entry
        if count_speed_zone_entry_relative is not UNSET:
            field_dict["count_speed_zone_entry_relative"] = count_speed_zone_entry_relative
        if count_sprint is not UNSET:
            field_dict["count_sprint"] = count_sprint
        if count_tag is not UNSET:
            field_dict["count_tag"] = count_tag
        if count_tempo_run is not UNSET:
            field_dict["count_tempo_run"] = count_tempo_run
        if count_throw_in is not UNSET:
            field_dict["count_throw_in"] = count_throw_in
        if count_turn_ice_hockey is not UNSET:
            field_dict["count_turn_ice_hockey"] = count_turn_ice_hockey

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count_acceleration = d.pop("count_acceleration", UNSET)

        count_ball_contact = d.pop("count_ball_contact", UNSET)

        count_ball_possession = d.pop("count_ball_possession", UNSET)

        count_ball_possession_lost = d.pop("count_ball_possession_lost", UNSET)

        count_ball_possession_recovery = d.pop("count_ball_possession_recovery", UNSET)

        count_cv_shot = d.pop("count_cv_shot", UNSET)

        count_change_of_direction = d.pop("count_change_of_direction", UNSET)

        count_change_of_orientation = d.pop("count_change_of_orientation", UNSET)

        count_change_of_pace = d.pop("count_change_of_pace", UNSET)

        count_corner_kick = d.pop("count_corner_kick", UNSET)

        count_counter_attack = d.pop("count_counter_attack", UNSET)

        count_detected_cross = d.pop("count_detected_cross", UNSET)

        count_cut = d.pop("count_cut", UNSET)

        count_deceleration = d.pop("count_deceleration", UNSET)

        count_defence = d.pop("count_defence", UNSET)

        count_detected_offside_soccer = d.pop("count_detected_offside_soccer", UNSET)

        count_detected_pass = d.pop("count_detected_pass", UNSET)

        count_detected_shot_basketball = d.pop("count_detected_shot_basketball", UNSET)

        count_detected_shot_fifa = d.pop("count_detected_shot_fifa", UNSET)

        count_detected_shot_handball = d.pop("count_detected_shot_handball", UNSET)

        count_detected_shot_ice_hockey = d.pop("count_detected_shot_ice_hockey", UNSET)

        count_detected_shot_intelligence_court = d.pop("count_detected_shot_intelligence_court", UNSET)

        count_detected_shot_soccer = d.pop("count_detected_shot_soccer", UNSET)

        count_dfl_corner_kick = d.pop("count_dfl_corner_kick", UNSET)

        count_dfl_cross = d.pop("count_dfl_cross", UNSET)

        count_dfl_free_kick = d.pop("count_dfl_free_kick", UNSET)

        count_dfl_goal_kick = d.pop("count_dfl_goal_kick", UNSET)

        count_dfl_kick_off = d.pop("count_dfl_kick_off", UNSET)

        count_dfl_pass = d.pop("count_dfl_pass", UNSET)

        count_dfl_penalty = d.pop("count_dfl_penalty", UNSET)

        count_dfl_shot_at_goal = d.pop("count_dfl_shot_at_goal", UNSET)

        count_dfl_sprint = d.pop("count_dfl_sprint", UNSET)

        count_dfl_tackling = d.pop("count_dfl_tackling", UNSET)

        count_dfl_throw_in = d.pop("count_dfl_throw_in", UNSET)

        count_down_on_pads = d.pop("count_down_on_pads", UNSET)

        count_dribbling_soccer = d.pop("count_dribbling_soccer", UNSET)

        count_dynamic_defence = d.pop("count_dynamic_defence", UNSET)

        count_exertion = d.pop("count_exertion", UNSET)

        count_full_court_transition = d.pop("count_full_court_transition", UNSET)

        count_goal_kick = d.pop("count_goal_kick", UNSET)

        count_goalkeeper_save_diving = d.pop("count_goalkeeper_save_diving", UNSET)

        count_goalkeeper_save_down_to_knees = d.pop("count_goalkeeper_save_down_to_knees", UNSET)

        count_goalkeeper_save_tilting = d.pop("count_goalkeeper_save_tilting", UNSET)

        count_group_counter_pressing = d.pop("count_group_counter_pressing", UNSET)

        count_group_empty_goal_handball = d.pop("count_group_empty_goal_handball", UNSET)

        count_heart_rate_recovery = d.pop("count_heart_rate_recovery", UNSET)

        count_impact = d.pop("count_impact", UNSET)

        count_jump_beach_volleyball = d.pop("count_jump_beach_volleyball", UNSET)

        count_jump = d.pop("count_jump", UNSET)

        count_mid_court_transition = d.pop("count_mid_court_transition", UNSET)

        count_noah_shot = d.pop("count_noah_shot", UNSET)

        count_offence = d.pop("count_offence", UNSET)

        count_pass_fifa = d.pop("count_pass_fifa", UNSET)

        count_pick_and_pop = d.pop("count_pick_and_pop", UNSET)

        count_pick_and_roll = d.pop("count_pick_and_roll", UNSET)

        count_pivot_rotation = d.pop("count_pivot_rotation", UNSET)

        count_play_by_player = d.pop("count_play_by_player", UNSET)

        count_play_by_team = d.pop("count_play_by_team", UNSET)

        count_player_counter_pressing = d.pop("count_player_counter_pressing", UNSET)

        count_rally_beach_volleyball = d.pop("count_rally_beach_volleyball", UNSET)

        count_rspct_shot = d.pop("count_rspct_shot", UNSET)

        count_shift = d.pop("count_shift", UNSET)

        count_skating_transition = d.pop("count_skating_transition", UNSET)

        count_speed_zone_entry = d.pop("count_speed_zone_entry", UNSET)

        count_speed_zone_entry_relative = d.pop("count_speed_zone_entry_relative", UNSET)

        count_sprint = d.pop("count_sprint", UNSET)

        count_tag = d.pop("count_tag", UNSET)

        count_tempo_run = d.pop("count_tempo_run", UNSET)

        count_throw_in = d.pop("count_throw_in", UNSET)

        count_turn_ice_hockey = d.pop("count_turn_ice_hockey", UNSET)

        event_count = cls(
            count_acceleration=count_acceleration,
            count_ball_contact=count_ball_contact,
            count_ball_possession=count_ball_possession,
            count_ball_possession_lost=count_ball_possession_lost,
            count_ball_possession_recovery=count_ball_possession_recovery,
            count_cv_shot=count_cv_shot,
            count_change_of_direction=count_change_of_direction,
            count_change_of_orientation=count_change_of_orientation,
            count_change_of_pace=count_change_of_pace,
            count_corner_kick=count_corner_kick,
            count_counter_attack=count_counter_attack,
            count_detected_cross=count_detected_cross,
            count_cut=count_cut,
            count_deceleration=count_deceleration,
            count_defence=count_defence,
            count_detected_offside_soccer=count_detected_offside_soccer,
            count_detected_pass=count_detected_pass,
            count_detected_shot_basketball=count_detected_shot_basketball,
            count_detected_shot_fifa=count_detected_shot_fifa,
            count_detected_shot_handball=count_detected_shot_handball,
            count_detected_shot_ice_hockey=count_detected_shot_ice_hockey,
            count_detected_shot_intelligence_court=count_detected_shot_intelligence_court,
            count_detected_shot_soccer=count_detected_shot_soccer,
            count_dfl_corner_kick=count_dfl_corner_kick,
            count_dfl_cross=count_dfl_cross,
            count_dfl_free_kick=count_dfl_free_kick,
            count_dfl_goal_kick=count_dfl_goal_kick,
            count_dfl_kick_off=count_dfl_kick_off,
            count_dfl_pass=count_dfl_pass,
            count_dfl_penalty=count_dfl_penalty,
            count_dfl_shot_at_goal=count_dfl_shot_at_goal,
            count_dfl_sprint=count_dfl_sprint,
            count_dfl_tackling=count_dfl_tackling,
            count_dfl_throw_in=count_dfl_throw_in,
            count_down_on_pads=count_down_on_pads,
            count_dribbling_soccer=count_dribbling_soccer,
            count_dynamic_defence=count_dynamic_defence,
            count_exertion=count_exertion,
            count_full_court_transition=count_full_court_transition,
            count_goal_kick=count_goal_kick,
            count_goalkeeper_save_diving=count_goalkeeper_save_diving,
            count_goalkeeper_save_down_to_knees=count_goalkeeper_save_down_to_knees,
            count_goalkeeper_save_tilting=count_goalkeeper_save_tilting,
            count_group_counter_pressing=count_group_counter_pressing,
            count_group_empty_goal_handball=count_group_empty_goal_handball,
            count_heart_rate_recovery=count_heart_rate_recovery,
            count_impact=count_impact,
            count_jump_beach_volleyball=count_jump_beach_volleyball,
            count_jump=count_jump,
            count_mid_court_transition=count_mid_court_transition,
            count_noah_shot=count_noah_shot,
            count_offence=count_offence,
            count_pass_fifa=count_pass_fifa,
            count_pick_and_pop=count_pick_and_pop,
            count_pick_and_roll=count_pick_and_roll,
            count_pivot_rotation=count_pivot_rotation,
            count_play_by_player=count_play_by_player,
            count_play_by_team=count_play_by_team,
            count_player_counter_pressing=count_player_counter_pressing,
            count_rally_beach_volleyball=count_rally_beach_volleyball,
            count_rspct_shot=count_rspct_shot,
            count_shift=count_shift,
            count_skating_transition=count_skating_transition,
            count_speed_zone_entry=count_speed_zone_entry,
            count_speed_zone_entry_relative=count_speed_zone_entry_relative,
            count_sprint=count_sprint,
            count_tag=count_tag,
            count_tempo_run=count_tempo_run,
            count_throw_in=count_throw_in,
            count_turn_ice_hockey=count_turn_ice_hockey,
        )

        event_count.additional_properties = d
        return event_count

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
