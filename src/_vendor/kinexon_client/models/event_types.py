from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_acceleration import EventAcceleration
    from ..models.event_ball_contact import EventBallContact
    from ..models.event_ball_possession import EventBallPossession
    from ..models.event_ball_possession_lost import EventBallPossessionLost
    from ..models.event_ball_possession_recovery import EventBallPossessionRecovery
    from ..models.event_change_of_direction import EventChangeOfDirection
    from ..models.event_change_of_orientation import EventChangeOfOrientation
    from ..models.event_change_of_pace import EventChangeOfPace
    from ..models.event_corner_kick import EventCornerKick
    from ..models.event_counter_attack import EventCounterAttack
    from ..models.event_cut import EventCut
    from ..models.event_cv_shot import EventCvShot
    from ..models.event_deceleration import EventDeceleration
    from ..models.event_defence import EventDefence
    from ..models.event_detected_cross import EventDetectedCross
    from ..models.event_detected_offside_soccer import EventDetectedOffsideSoccer
    from ..models.event_detected_pass import EventDetectedPass
    from ..models.event_detected_shot_basketball import EventDetectedShotBasketball
    from ..models.event_detected_shot_fifa import EventDetectedShotFifa
    from ..models.event_detected_shot_handball import EventDetectedShotHandball
    from ..models.event_detected_shot_ice_hockey import EventDetectedShotIceHockey
    from ..models.event_detected_shot_intelligence_court import (
        EventDetectedShotIntelligenceCourt,
    )
    from ..models.event_detected_shot_soccer import EventDetectedShotSoccer
    from ..models.event_dfl_corner_kick import EventDflCornerKick
    from ..models.event_dfl_cross import EventDflCross
    from ..models.event_dfl_free_kick import EventDflFreeKick
    from ..models.event_dfl_goal_kick import EventDflGoalKick
    from ..models.event_dfl_kick_off import EventDflKickOff
    from ..models.event_dfl_pass import EventDflPass
    from ..models.event_dfl_penalty import EventDflPenalty
    from ..models.event_dfl_shot_at_goal import EventDflShotAtGoal
    from ..models.event_dfl_sprint import EventDflSprint
    from ..models.event_dfl_tackling import EventDflTackling
    from ..models.event_dfl_throw_in import EventDflThrowIn
    from ..models.event_down_on_pads import EventDownOnPads
    from ..models.event_dribbling_soccer import EventDribblingSoccer
    from ..models.event_dynamic_defence import EventDynamicDefence
    from ..models.event_exertion import EventExertion
    from ..models.event_full_court_transition import EventFullCourtTransition
    from ..models.event_goal_kick import EventGoalKick
    from ..models.event_goalkeeper_save_diving import EventGoalkeeperSaveDiving
    from ..models.event_goalkeeper_save_down_to_knees import (
        EventGoalkeeperSaveDownToKnees,
    )
    from ..models.event_goalkeeper_save_tilting import EventGoalkeeperSaveTilting
    from ..models.event_group_counter_pressing import EventGroupCounterPressing
    from ..models.event_group_empty_goal_handball import EventGroupEmptyGoalHandball
    from ..models.event_heart_rate_recovery import EventHeartRateRecovery
    from ..models.event_impact import EventImpact
    from ..models.event_jump import EventJump
    from ..models.event_jump_beach_volleyball import EventJumpBeachVolleyball
    from ..models.event_mid_court_transition import EventMidCourtTransition
    from ..models.event_noah_shot import EventNoahShot
    from ..models.event_offence import EventOffence
    from ..models.event_pass_fifa import EventPassFifa
    from ..models.event_pick_and_pop import EventPickAndPop
    from ..models.event_pick_and_roll import EventPickAndRoll
    from ..models.event_pivot_rotation import EventPivotRotation
    from ..models.event_play_by_player import EventPlayByPlayer
    from ..models.event_play_by_team import EventPlayByTeam
    from ..models.event_player_counter_pressing import EventPlayerCounterPressing
    from ..models.event_rally_beach_volleyball import EventRallyBeachVolleyball
    from ..models.event_rspct_shot import EventRspctShot
    from ..models.event_shift import EventShift
    from ..models.event_skating_transition import EventSkatingTransition
    from ..models.event_speed_zone_entry import EventSpeedZoneEntry
    from ..models.event_speed_zone_entry_relative import EventSpeedZoneEntryRelative
    from ..models.event_sprint import EventSprint
    from ..models.event_tag import EventTag
    from ..models.event_tempo_run import EventTempoRun
    from ..models.event_throw_in import EventThrowIn
    from ..models.event_turn_ice_hockey import EventTurnIceHockey


T = TypeVar("T", bound="EventTypes")


@_attrs_define
class EventTypes:
    """
    Attributes:
        acceleration (Union[Unset, EventAcceleration]):
        ball_contact (Union[Unset, EventBallContact]):
        ball_possession (Union[Unset, EventBallPossession]):
        ball_possession_lost (Union[Unset, EventBallPossessionLost]):
        ball_possession_recovery (Union[Unset, EventBallPossessionRecovery]):
        cv_shot (Union[Unset, EventCvShot]):
        change_of_direction (Union[Unset, EventChangeOfDirection]):
        change_of_orientation (Union[Unset, EventChangeOfOrientation]):
        change_of_pace (Union[Unset, EventChangeOfPace]):
        corner_kick (Union[Unset, EventCornerKick]):
        counter_attack (Union[Unset, EventCounterAttack]):
        detected_cross (Union[Unset, EventDetectedCross]):
        cut (Union[Unset, EventCut]):
        deceleration (Union[Unset, EventDeceleration]):
        defence (Union[Unset, EventDefence]):
        detected_offside_soccer (Union[Unset, EventDetectedOffsideSoccer]):
        detected_pass (Union[Unset, EventDetectedPass]):
        detected_shot_basketball (Union[Unset, EventDetectedShotBasketball]):
        detected_shot_fifa (Union[Unset, EventDetectedShotFifa]):
        detected_shot_handball (Union[Unset, EventDetectedShotHandball]):
        detected_shot_ice_hockey (Union[Unset, EventDetectedShotIceHockey]):
        detected_shot_intelligence_court (Union[Unset, EventDetectedShotIntelligenceCourt]):
        detected_shot_soccer (Union[Unset, EventDetectedShotSoccer]):
        dfl_corner_kick (Union[Unset, EventDflCornerKick]):
        dfl_cross (Union[Unset, EventDflCross]):
        dfl_free_kick (Union[Unset, EventDflFreeKick]):
        dfl_goal_kick (Union[Unset, EventDflGoalKick]):
        dfl_kick_off (Union[Unset, EventDflKickOff]):
        dfl_pass (Union[Unset, EventDflPass]):
        dfl_penalty (Union[Unset, EventDflPenalty]):
        dfl_shot_at_goal (Union[Unset, EventDflShotAtGoal]):
        dfl_sprint (Union[Unset, EventDflSprint]):
        dfl_tackling (Union[Unset, EventDflTackling]):
        dfl_throw_in (Union[Unset, EventDflThrowIn]):
        down_on_pads (Union[Unset, EventDownOnPads]):
        dribbling_soccer (Union[Unset, EventDribblingSoccer]):
        dynamic_defence (Union[Unset, EventDynamicDefence]):
        exertion (Union[Unset, EventExertion]):
        full_court_transition (Union[Unset, EventFullCourtTransition]):
        goal_kick (Union[Unset, EventGoalKick]):
        goalkeeper_save_diving (Union[Unset, EventGoalkeeperSaveDiving]):
        goalkeeper_save_down_to_knees (Union[Unset, EventGoalkeeperSaveDownToKnees]):
        goalkeeper_save_tilting (Union[Unset, EventGoalkeeperSaveTilting]):
        group_counter_pressing (Union[Unset, EventGroupCounterPressing]):
        group_empty_goal_handball (Union[Unset, EventGroupEmptyGoalHandball]):
        heart_rate_recovery (Union[Unset, EventHeartRateRecovery]):
        impact (Union[Unset, EventImpact]):
        jump_beach_volleyball (Union[Unset, EventJumpBeachVolleyball]):
        jump (Union[Unset, EventJump]):
        mid_court_transition (Union[Unset, EventMidCourtTransition]):
        noah_shot (Union[Unset, EventNoahShot]):
        offence (Union[Unset, EventOffence]):
        pass_fifa (Union[Unset, EventPassFifa]):
        pick_and_pop (Union[Unset, EventPickAndPop]):
        pick_and_roll (Union[Unset, EventPickAndRoll]):
        pivot_rotation (Union[Unset, EventPivotRotation]):
        play_by_player (Union[Unset, EventPlayByPlayer]):
        play_by_team (Union[Unset, EventPlayByTeam]):
        player_counter_pressing (Union[Unset, EventPlayerCounterPressing]):
        rally_beach_volleyball (Union[Unset, EventRallyBeachVolleyball]):
        rspct_shot (Union[Unset, EventRspctShot]):
        shift (Union[Unset, EventShift]):
        skating_transition (Union[Unset, EventSkatingTransition]):
        speed_zone_entry (Union[Unset, EventSpeedZoneEntry]):
        speed_zone_entry_relative (Union[Unset, EventSpeedZoneEntryRelative]):
        sprint (Union[Unset, EventSprint]):
        tag (Union[Unset, EventTag]):
        tempo_run (Union[Unset, EventTempoRun]):
        throw_in (Union[Unset, EventThrowIn]):
        turn_ice_hockey (Union[Unset, EventTurnIceHockey]):
    """

    acceleration: Union[Unset, "EventAcceleration"] = UNSET
    ball_contact: Union[Unset, "EventBallContact"] = UNSET
    ball_possession: Union[Unset, "EventBallPossession"] = UNSET
    ball_possession_lost: Union[Unset, "EventBallPossessionLost"] = UNSET
    ball_possession_recovery: Union[Unset, "EventBallPossessionRecovery"] = UNSET
    cv_shot: Union[Unset, "EventCvShot"] = UNSET
    change_of_direction: Union[Unset, "EventChangeOfDirection"] = UNSET
    change_of_orientation: Union[Unset, "EventChangeOfOrientation"] = UNSET
    change_of_pace: Union[Unset, "EventChangeOfPace"] = UNSET
    corner_kick: Union[Unset, "EventCornerKick"] = UNSET
    counter_attack: Union[Unset, "EventCounterAttack"] = UNSET
    detected_cross: Union[Unset, "EventDetectedCross"] = UNSET
    cut: Union[Unset, "EventCut"] = UNSET
    deceleration: Union[Unset, "EventDeceleration"] = UNSET
    defence: Union[Unset, "EventDefence"] = UNSET
    detected_offside_soccer: Union[Unset, "EventDetectedOffsideSoccer"] = UNSET
    detected_pass: Union[Unset, "EventDetectedPass"] = UNSET
    detected_shot_basketball: Union[Unset, "EventDetectedShotBasketball"] = UNSET
    detected_shot_fifa: Union[Unset, "EventDetectedShotFifa"] = UNSET
    detected_shot_handball: Union[Unset, "EventDetectedShotHandball"] = UNSET
    detected_shot_ice_hockey: Union[Unset, "EventDetectedShotIceHockey"] = UNSET
    detected_shot_intelligence_court: Union[Unset, "EventDetectedShotIntelligenceCourt"] = UNSET
    detected_shot_soccer: Union[Unset, "EventDetectedShotSoccer"] = UNSET
    dfl_corner_kick: Union[Unset, "EventDflCornerKick"] = UNSET
    dfl_cross: Union[Unset, "EventDflCross"] = UNSET
    dfl_free_kick: Union[Unset, "EventDflFreeKick"] = UNSET
    dfl_goal_kick: Union[Unset, "EventDflGoalKick"] = UNSET
    dfl_kick_off: Union[Unset, "EventDflKickOff"] = UNSET
    dfl_pass: Union[Unset, "EventDflPass"] = UNSET
    dfl_penalty: Union[Unset, "EventDflPenalty"] = UNSET
    dfl_shot_at_goal: Union[Unset, "EventDflShotAtGoal"] = UNSET
    dfl_sprint: Union[Unset, "EventDflSprint"] = UNSET
    dfl_tackling: Union[Unset, "EventDflTackling"] = UNSET
    dfl_throw_in: Union[Unset, "EventDflThrowIn"] = UNSET
    down_on_pads: Union[Unset, "EventDownOnPads"] = UNSET
    dribbling_soccer: Union[Unset, "EventDribblingSoccer"] = UNSET
    dynamic_defence: Union[Unset, "EventDynamicDefence"] = UNSET
    exertion: Union[Unset, "EventExertion"] = UNSET
    full_court_transition: Union[Unset, "EventFullCourtTransition"] = UNSET
    goal_kick: Union[Unset, "EventGoalKick"] = UNSET
    goalkeeper_save_diving: Union[Unset, "EventGoalkeeperSaveDiving"] = UNSET
    goalkeeper_save_down_to_knees: Union[Unset, "EventGoalkeeperSaveDownToKnees"] = UNSET
    goalkeeper_save_tilting: Union[Unset, "EventGoalkeeperSaveTilting"] = UNSET
    group_counter_pressing: Union[Unset, "EventGroupCounterPressing"] = UNSET
    group_empty_goal_handball: Union[Unset, "EventGroupEmptyGoalHandball"] = UNSET
    heart_rate_recovery: Union[Unset, "EventHeartRateRecovery"] = UNSET
    impact: Union[Unset, "EventImpact"] = UNSET
    jump_beach_volleyball: Union[Unset, "EventJumpBeachVolleyball"] = UNSET
    jump: Union[Unset, "EventJump"] = UNSET
    mid_court_transition: Union[Unset, "EventMidCourtTransition"] = UNSET
    noah_shot: Union[Unset, "EventNoahShot"] = UNSET
    offence: Union[Unset, "EventOffence"] = UNSET
    pass_fifa: Union[Unset, "EventPassFifa"] = UNSET
    pick_and_pop: Union[Unset, "EventPickAndPop"] = UNSET
    pick_and_roll: Union[Unset, "EventPickAndRoll"] = UNSET
    pivot_rotation: Union[Unset, "EventPivotRotation"] = UNSET
    play_by_player: Union[Unset, "EventPlayByPlayer"] = UNSET
    play_by_team: Union[Unset, "EventPlayByTeam"] = UNSET
    player_counter_pressing: Union[Unset, "EventPlayerCounterPressing"] = UNSET
    rally_beach_volleyball: Union[Unset, "EventRallyBeachVolleyball"] = UNSET
    rspct_shot: Union[Unset, "EventRspctShot"] = UNSET
    shift: Union[Unset, "EventShift"] = UNSET
    skating_transition: Union[Unset, "EventSkatingTransition"] = UNSET
    speed_zone_entry: Union[Unset, "EventSpeedZoneEntry"] = UNSET
    speed_zone_entry_relative: Union[Unset, "EventSpeedZoneEntryRelative"] = UNSET
    sprint: Union[Unset, "EventSprint"] = UNSET
    tag: Union[Unset, "EventTag"] = UNSET
    tempo_run: Union[Unset, "EventTempoRun"] = UNSET
    throw_in: Union[Unset, "EventThrowIn"] = UNSET
    turn_ice_hockey: Union[Unset, "EventTurnIceHockey"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acceleration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.acceleration, Unset):
            acceleration = self.acceleration.to_dict()

        ball_contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ball_contact, Unset):
            ball_contact = self.ball_contact.to_dict()

        ball_possession: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ball_possession, Unset):
            ball_possession = self.ball_possession.to_dict()

        ball_possession_lost: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ball_possession_lost, Unset):
            ball_possession_lost = self.ball_possession_lost.to_dict()

        ball_possession_recovery: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ball_possession_recovery, Unset):
            ball_possession_recovery = self.ball_possession_recovery.to_dict()

        cv_shot: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cv_shot, Unset):
            cv_shot = self.cv_shot.to_dict()

        change_of_direction: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.change_of_direction, Unset):
            change_of_direction = self.change_of_direction.to_dict()

        change_of_orientation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.change_of_orientation, Unset):
            change_of_orientation = self.change_of_orientation.to_dict()

        change_of_pace: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.change_of_pace, Unset):
            change_of_pace = self.change_of_pace.to_dict()

        corner_kick: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.corner_kick, Unset):
            corner_kick = self.corner_kick.to_dict()

        counter_attack: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.counter_attack, Unset):
            counter_attack = self.counter_attack.to_dict()

        detected_cross: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.detected_cross, Unset):
            detected_cross = self.detected_cross.to_dict()

        cut: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cut, Unset):
            cut = self.cut.to_dict()

        deceleration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.deceleration, Unset):
            deceleration = self.deceleration.to_dict()

        defence: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.defence, Unset):
            defence = self.defence.to_dict()

        detected_offside_soccer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.detected_offside_soccer, Unset):
            detected_offside_soccer = self.detected_offside_soccer.to_dict()

        detected_pass: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.detected_pass, Unset):
            detected_pass = self.detected_pass.to_dict()

        detected_shot_basketball: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.detected_shot_basketball, Unset):
            detected_shot_basketball = self.detected_shot_basketball.to_dict()

        detected_shot_fifa: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.detected_shot_fifa, Unset):
            detected_shot_fifa = self.detected_shot_fifa.to_dict()

        detected_shot_handball: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.detected_shot_handball, Unset):
            detected_shot_handball = self.detected_shot_handball.to_dict()

        detected_shot_ice_hockey: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.detected_shot_ice_hockey, Unset):
            detected_shot_ice_hockey = self.detected_shot_ice_hockey.to_dict()

        detected_shot_intelligence_court: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.detected_shot_intelligence_court, Unset):
            detected_shot_intelligence_court = self.detected_shot_intelligence_court.to_dict()

        detected_shot_soccer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.detected_shot_soccer, Unset):
            detected_shot_soccer = self.detected_shot_soccer.to_dict()

        dfl_corner_kick: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dfl_corner_kick, Unset):
            dfl_corner_kick = self.dfl_corner_kick.to_dict()

        dfl_cross: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dfl_cross, Unset):
            dfl_cross = self.dfl_cross.to_dict()

        dfl_free_kick: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dfl_free_kick, Unset):
            dfl_free_kick = self.dfl_free_kick.to_dict()

        dfl_goal_kick: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dfl_goal_kick, Unset):
            dfl_goal_kick = self.dfl_goal_kick.to_dict()

        dfl_kick_off: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dfl_kick_off, Unset):
            dfl_kick_off = self.dfl_kick_off.to_dict()

        dfl_pass: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dfl_pass, Unset):
            dfl_pass = self.dfl_pass.to_dict()

        dfl_penalty: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dfl_penalty, Unset):
            dfl_penalty = self.dfl_penalty.to_dict()

        dfl_shot_at_goal: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dfl_shot_at_goal, Unset):
            dfl_shot_at_goal = self.dfl_shot_at_goal.to_dict()

        dfl_sprint: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dfl_sprint, Unset):
            dfl_sprint = self.dfl_sprint.to_dict()

        dfl_tackling: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dfl_tackling, Unset):
            dfl_tackling = self.dfl_tackling.to_dict()

        dfl_throw_in: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dfl_throw_in, Unset):
            dfl_throw_in = self.dfl_throw_in.to_dict()

        down_on_pads: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.down_on_pads, Unset):
            down_on_pads = self.down_on_pads.to_dict()

        dribbling_soccer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dribbling_soccer, Unset):
            dribbling_soccer = self.dribbling_soccer.to_dict()

        dynamic_defence: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dynamic_defence, Unset):
            dynamic_defence = self.dynamic_defence.to_dict()

        exertion: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.exertion, Unset):
            exertion = self.exertion.to_dict()

        full_court_transition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.full_court_transition, Unset):
            full_court_transition = self.full_court_transition.to_dict()

        goal_kick: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.goal_kick, Unset):
            goal_kick = self.goal_kick.to_dict()

        goalkeeper_save_diving: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.goalkeeper_save_diving, Unset):
            goalkeeper_save_diving = self.goalkeeper_save_diving.to_dict()

        goalkeeper_save_down_to_knees: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.goalkeeper_save_down_to_knees, Unset):
            goalkeeper_save_down_to_knees = self.goalkeeper_save_down_to_knees.to_dict()

        goalkeeper_save_tilting: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.goalkeeper_save_tilting, Unset):
            goalkeeper_save_tilting = self.goalkeeper_save_tilting.to_dict()

        group_counter_pressing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group_counter_pressing, Unset):
            group_counter_pressing = self.group_counter_pressing.to_dict()

        group_empty_goal_handball: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group_empty_goal_handball, Unset):
            group_empty_goal_handball = self.group_empty_goal_handball.to_dict()

        heart_rate_recovery: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.heart_rate_recovery, Unset):
            heart_rate_recovery = self.heart_rate_recovery.to_dict()

        impact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.impact, Unset):
            impact = self.impact.to_dict()

        jump_beach_volleyball: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.jump_beach_volleyball, Unset):
            jump_beach_volleyball = self.jump_beach_volleyball.to_dict()

        jump: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.jump, Unset):
            jump = self.jump.to_dict()

        mid_court_transition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mid_court_transition, Unset):
            mid_court_transition = self.mid_court_transition.to_dict()

        noah_shot: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.noah_shot, Unset):
            noah_shot = self.noah_shot.to_dict()

        offence: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.offence, Unset):
            offence = self.offence.to_dict()

        pass_fifa: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pass_fifa, Unset):
            pass_fifa = self.pass_fifa.to_dict()

        pick_and_pop: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pick_and_pop, Unset):
            pick_and_pop = self.pick_and_pop.to_dict()

        pick_and_roll: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pick_and_roll, Unset):
            pick_and_roll = self.pick_and_roll.to_dict()

        pivot_rotation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pivot_rotation, Unset):
            pivot_rotation = self.pivot_rotation.to_dict()

        play_by_player: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.play_by_player, Unset):
            play_by_player = self.play_by_player.to_dict()

        play_by_team: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.play_by_team, Unset):
            play_by_team = self.play_by_team.to_dict()

        player_counter_pressing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.player_counter_pressing, Unset):
            player_counter_pressing = self.player_counter_pressing.to_dict()

        rally_beach_volleyball: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rally_beach_volleyball, Unset):
            rally_beach_volleyball = self.rally_beach_volleyball.to_dict()

        rspct_shot: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rspct_shot, Unset):
            rspct_shot = self.rspct_shot.to_dict()

        shift: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shift, Unset):
            shift = self.shift.to_dict()

        skating_transition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.skating_transition, Unset):
            skating_transition = self.skating_transition.to_dict()

        speed_zone_entry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.speed_zone_entry, Unset):
            speed_zone_entry = self.speed_zone_entry.to_dict()

        speed_zone_entry_relative: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.speed_zone_entry_relative, Unset):
            speed_zone_entry_relative = self.speed_zone_entry_relative.to_dict()

        sprint: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sprint, Unset):
            sprint = self.sprint.to_dict()

        tag: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag.to_dict()

        tempo_run: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tempo_run, Unset):
            tempo_run = self.tempo_run.to_dict()

        throw_in: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.throw_in, Unset):
            throw_in = self.throw_in.to_dict()

        turn_ice_hockey: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.turn_ice_hockey, Unset):
            turn_ice_hockey = self.turn_ice_hockey.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acceleration is not UNSET:
            field_dict["acceleration"] = acceleration
        if ball_contact is not UNSET:
            field_dict["ball_contact"] = ball_contact
        if ball_possession is not UNSET:
            field_dict["ball_possession"] = ball_possession
        if ball_possession_lost is not UNSET:
            field_dict["ball_possession_lost"] = ball_possession_lost
        if ball_possession_recovery is not UNSET:
            field_dict["ball_possession_recovery"] = ball_possession_recovery
        if cv_shot is not UNSET:
            field_dict["cv_shot"] = cv_shot
        if change_of_direction is not UNSET:
            field_dict["change_of_direction"] = change_of_direction
        if change_of_orientation is not UNSET:
            field_dict["change_of_orientation"] = change_of_orientation
        if change_of_pace is not UNSET:
            field_dict["change_of_pace"] = change_of_pace
        if corner_kick is not UNSET:
            field_dict["corner_kick"] = corner_kick
        if counter_attack is not UNSET:
            field_dict["counter_attack"] = counter_attack
        if detected_cross is not UNSET:
            field_dict["detected_cross"] = detected_cross
        if cut is not UNSET:
            field_dict["cut"] = cut
        if deceleration is not UNSET:
            field_dict["deceleration"] = deceleration
        if defence is not UNSET:
            field_dict["defence"] = defence
        if detected_offside_soccer is not UNSET:
            field_dict["detected_offside_soccer"] = detected_offside_soccer
        if detected_pass is not UNSET:
            field_dict["detected_pass"] = detected_pass
        if detected_shot_basketball is not UNSET:
            field_dict["detected_shot_basketball"] = detected_shot_basketball
        if detected_shot_fifa is not UNSET:
            field_dict["detected_shot_fifa"] = detected_shot_fifa
        if detected_shot_handball is not UNSET:
            field_dict["detected_shot_handball"] = detected_shot_handball
        if detected_shot_ice_hockey is not UNSET:
            field_dict["detected_shot_ice_hockey"] = detected_shot_ice_hockey
        if detected_shot_intelligence_court is not UNSET:
            field_dict["detected_shot_intelligence_court"] = detected_shot_intelligence_court
        if detected_shot_soccer is not UNSET:
            field_dict["detected_shot_soccer"] = detected_shot_soccer
        if dfl_corner_kick is not UNSET:
            field_dict["dfl_corner_kick"] = dfl_corner_kick
        if dfl_cross is not UNSET:
            field_dict["dfl_cross"] = dfl_cross
        if dfl_free_kick is not UNSET:
            field_dict["dfl_free_kick"] = dfl_free_kick
        if dfl_goal_kick is not UNSET:
            field_dict["dfl_goal_kick"] = dfl_goal_kick
        if dfl_kick_off is not UNSET:
            field_dict["dfl_kick_off"] = dfl_kick_off
        if dfl_pass is not UNSET:
            field_dict["dfl_pass"] = dfl_pass
        if dfl_penalty is not UNSET:
            field_dict["dfl_penalty"] = dfl_penalty
        if dfl_shot_at_goal is not UNSET:
            field_dict["dfl_shot_at_goal"] = dfl_shot_at_goal
        if dfl_sprint is not UNSET:
            field_dict["dfl_sprint"] = dfl_sprint
        if dfl_tackling is not UNSET:
            field_dict["dfl_tackling"] = dfl_tackling
        if dfl_throw_in is not UNSET:
            field_dict["dfl_throw_in"] = dfl_throw_in
        if down_on_pads is not UNSET:
            field_dict["down_on_pads"] = down_on_pads
        if dribbling_soccer is not UNSET:
            field_dict["dribbling_soccer"] = dribbling_soccer
        if dynamic_defence is not UNSET:
            field_dict["dynamic_defence"] = dynamic_defence
        if exertion is not UNSET:
            field_dict["exertion"] = exertion
        if full_court_transition is not UNSET:
            field_dict["full_court_transition"] = full_court_transition
        if goal_kick is not UNSET:
            field_dict["goal_kick"] = goal_kick
        if goalkeeper_save_diving is not UNSET:
            field_dict["goalkeeper_save_diving"] = goalkeeper_save_diving
        if goalkeeper_save_down_to_knees is not UNSET:
            field_dict["goalkeeper_save_down_to_knees"] = goalkeeper_save_down_to_knees
        if goalkeeper_save_tilting is not UNSET:
            field_dict["goalkeeper_save_tilting"] = goalkeeper_save_tilting
        if group_counter_pressing is not UNSET:
            field_dict["group_counter_pressing"] = group_counter_pressing
        if group_empty_goal_handball is not UNSET:
            field_dict["group_empty_goal_handball"] = group_empty_goal_handball
        if heart_rate_recovery is not UNSET:
            field_dict["heart_rate_recovery"] = heart_rate_recovery
        if impact is not UNSET:
            field_dict["impact"] = impact
        if jump_beach_volleyball is not UNSET:
            field_dict["jump_beach_volleyball"] = jump_beach_volleyball
        if jump is not UNSET:
            field_dict["jump"] = jump
        if mid_court_transition is not UNSET:
            field_dict["mid_court_transition"] = mid_court_transition
        if noah_shot is not UNSET:
            field_dict["noah_shot"] = noah_shot
        if offence is not UNSET:
            field_dict["offence"] = offence
        if pass_fifa is not UNSET:
            field_dict["pass_fifa"] = pass_fifa
        if pick_and_pop is not UNSET:
            field_dict["pick_and_pop"] = pick_and_pop
        if pick_and_roll is not UNSET:
            field_dict["pick_and_roll"] = pick_and_roll
        if pivot_rotation is not UNSET:
            field_dict["pivot_rotation"] = pivot_rotation
        if play_by_player is not UNSET:
            field_dict["play_by_player"] = play_by_player
        if play_by_team is not UNSET:
            field_dict["play_by_team"] = play_by_team
        if player_counter_pressing is not UNSET:
            field_dict["player_counter_pressing"] = player_counter_pressing
        if rally_beach_volleyball is not UNSET:
            field_dict["rally_beach_volleyball"] = rally_beach_volleyball
        if rspct_shot is not UNSET:
            field_dict["rspct_shot"] = rspct_shot
        if shift is not UNSET:
            field_dict["shift"] = shift
        if skating_transition is not UNSET:
            field_dict["skating_transition"] = skating_transition
        if speed_zone_entry is not UNSET:
            field_dict["speed_zone_entry"] = speed_zone_entry
        if speed_zone_entry_relative is not UNSET:
            field_dict["speed_zone_entry_relative"] = speed_zone_entry_relative
        if sprint is not UNSET:
            field_dict["sprint"] = sprint
        if tag is not UNSET:
            field_dict["tag"] = tag
        if tempo_run is not UNSET:
            field_dict["tempo_run"] = tempo_run
        if throw_in is not UNSET:
            field_dict["throw_in"] = throw_in
        if turn_ice_hockey is not UNSET:
            field_dict["turn_ice_hockey"] = turn_ice_hockey

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_acceleration import EventAcceleration
        from ..models.event_ball_contact import EventBallContact
        from ..models.event_ball_possession import EventBallPossession
        from ..models.event_ball_possession_lost import EventBallPossessionLost
        from ..models.event_ball_possession_recovery import EventBallPossessionRecovery
        from ..models.event_change_of_direction import EventChangeOfDirection
        from ..models.event_change_of_orientation import EventChangeOfOrientation
        from ..models.event_change_of_pace import EventChangeOfPace
        from ..models.event_corner_kick import EventCornerKick
        from ..models.event_counter_attack import EventCounterAttack
        from ..models.event_cut import EventCut
        from ..models.event_cv_shot import EventCvShot
        from ..models.event_deceleration import EventDeceleration
        from ..models.event_defence import EventDefence
        from ..models.event_detected_cross import EventDetectedCross
        from ..models.event_detected_offside_soccer import EventDetectedOffsideSoccer
        from ..models.event_detected_pass import EventDetectedPass
        from ..models.event_detected_shot_basketball import EventDetectedShotBasketball
        from ..models.event_detected_shot_fifa import EventDetectedShotFifa
        from ..models.event_detected_shot_handball import EventDetectedShotHandball
        from ..models.event_detected_shot_ice_hockey import EventDetectedShotIceHockey
        from ..models.event_detected_shot_intelligence_court import (
            EventDetectedShotIntelligenceCourt,
        )
        from ..models.event_detected_shot_soccer import EventDetectedShotSoccer
        from ..models.event_dfl_corner_kick import EventDflCornerKick
        from ..models.event_dfl_cross import EventDflCross
        from ..models.event_dfl_free_kick import EventDflFreeKick
        from ..models.event_dfl_goal_kick import EventDflGoalKick
        from ..models.event_dfl_kick_off import EventDflKickOff
        from ..models.event_dfl_pass import EventDflPass
        from ..models.event_dfl_penalty import EventDflPenalty
        from ..models.event_dfl_shot_at_goal import EventDflShotAtGoal
        from ..models.event_dfl_sprint import EventDflSprint
        from ..models.event_dfl_tackling import EventDflTackling
        from ..models.event_dfl_throw_in import EventDflThrowIn
        from ..models.event_down_on_pads import EventDownOnPads
        from ..models.event_dribbling_soccer import EventDribblingSoccer
        from ..models.event_dynamic_defence import EventDynamicDefence
        from ..models.event_exertion import EventExertion
        from ..models.event_full_court_transition import EventFullCourtTransition
        from ..models.event_goal_kick import EventGoalKick
        from ..models.event_goalkeeper_save_diving import EventGoalkeeperSaveDiving
        from ..models.event_goalkeeper_save_down_to_knees import (
            EventGoalkeeperSaveDownToKnees,
        )
        from ..models.event_goalkeeper_save_tilting import EventGoalkeeperSaveTilting
        from ..models.event_group_counter_pressing import EventGroupCounterPressing
        from ..models.event_group_empty_goal_handball import EventGroupEmptyGoalHandball
        from ..models.event_heart_rate_recovery import EventHeartRateRecovery
        from ..models.event_impact import EventImpact
        from ..models.event_jump import EventJump
        from ..models.event_jump_beach_volleyball import EventJumpBeachVolleyball
        from ..models.event_mid_court_transition import EventMidCourtTransition
        from ..models.event_noah_shot import EventNoahShot
        from ..models.event_offence import EventOffence
        from ..models.event_pass_fifa import EventPassFifa
        from ..models.event_pick_and_pop import EventPickAndPop
        from ..models.event_pick_and_roll import EventPickAndRoll
        from ..models.event_pivot_rotation import EventPivotRotation
        from ..models.event_play_by_player import EventPlayByPlayer
        from ..models.event_play_by_team import EventPlayByTeam
        from ..models.event_player_counter_pressing import EventPlayerCounterPressing
        from ..models.event_rally_beach_volleyball import EventRallyBeachVolleyball
        from ..models.event_rspct_shot import EventRspctShot
        from ..models.event_shift import EventShift
        from ..models.event_skating_transition import EventSkatingTransition
        from ..models.event_speed_zone_entry import EventSpeedZoneEntry
        from ..models.event_speed_zone_entry_relative import EventSpeedZoneEntryRelative
        from ..models.event_sprint import EventSprint
        from ..models.event_tag import EventTag
        from ..models.event_tempo_run import EventTempoRun
        from ..models.event_throw_in import EventThrowIn
        from ..models.event_turn_ice_hockey import EventTurnIceHockey

        d = dict(src_dict)
        _acceleration = d.pop("acceleration", UNSET)
        acceleration: Union[Unset, EventAcceleration]
        if isinstance(_acceleration, Unset):
            acceleration = UNSET
        else:
            acceleration = EventAcceleration.from_dict(_acceleration)

        _ball_contact = d.pop("ball_contact", UNSET)
        ball_contact: Union[Unset, EventBallContact]
        if isinstance(_ball_contact, Unset):
            ball_contact = UNSET
        else:
            ball_contact = EventBallContact.from_dict(_ball_contact)

        _ball_possession = d.pop("ball_possession", UNSET)
        ball_possession: Union[Unset, EventBallPossession]
        if isinstance(_ball_possession, Unset):
            ball_possession = UNSET
        else:
            ball_possession = EventBallPossession.from_dict(_ball_possession)

        _ball_possession_lost = d.pop("ball_possession_lost", UNSET)
        ball_possession_lost: Union[Unset, EventBallPossessionLost]
        if isinstance(_ball_possession_lost, Unset):
            ball_possession_lost = UNSET
        else:
            ball_possession_lost = EventBallPossessionLost.from_dict(_ball_possession_lost)

        _ball_possession_recovery = d.pop("ball_possession_recovery", UNSET)
        ball_possession_recovery: Union[Unset, EventBallPossessionRecovery]
        if isinstance(_ball_possession_recovery, Unset):
            ball_possession_recovery = UNSET
        else:
            ball_possession_recovery = EventBallPossessionRecovery.from_dict(_ball_possession_recovery)

        _cv_shot = d.pop("cv_shot", UNSET)
        cv_shot: Union[Unset, EventCvShot]
        if isinstance(_cv_shot, Unset):
            cv_shot = UNSET
        else:
            cv_shot = EventCvShot.from_dict(_cv_shot)

        _change_of_direction = d.pop("change_of_direction", UNSET)
        change_of_direction: Union[Unset, EventChangeOfDirection]
        if isinstance(_change_of_direction, Unset):
            change_of_direction = UNSET
        else:
            change_of_direction = EventChangeOfDirection.from_dict(_change_of_direction)

        _change_of_orientation = d.pop("change_of_orientation", UNSET)
        change_of_orientation: Union[Unset, EventChangeOfOrientation]
        if isinstance(_change_of_orientation, Unset):
            change_of_orientation = UNSET
        else:
            change_of_orientation = EventChangeOfOrientation.from_dict(_change_of_orientation)

        _change_of_pace = d.pop("change_of_pace", UNSET)
        change_of_pace: Union[Unset, EventChangeOfPace]
        if isinstance(_change_of_pace, Unset):
            change_of_pace = UNSET
        else:
            change_of_pace = EventChangeOfPace.from_dict(_change_of_pace)

        _corner_kick = d.pop("corner_kick", UNSET)
        corner_kick: Union[Unset, EventCornerKick]
        if isinstance(_corner_kick, Unset):
            corner_kick = UNSET
        else:
            corner_kick = EventCornerKick.from_dict(_corner_kick)

        _counter_attack = d.pop("counter_attack", UNSET)
        counter_attack: Union[Unset, EventCounterAttack]
        if isinstance(_counter_attack, Unset):
            counter_attack = UNSET
        else:
            counter_attack = EventCounterAttack.from_dict(_counter_attack)

        _detected_cross = d.pop("detected_cross", UNSET)
        detected_cross: Union[Unset, EventDetectedCross]
        if isinstance(_detected_cross, Unset):
            detected_cross = UNSET
        else:
            detected_cross = EventDetectedCross.from_dict(_detected_cross)

        _cut = d.pop("cut", UNSET)
        cut: Union[Unset, EventCut]
        if isinstance(_cut, Unset):
            cut = UNSET
        else:
            cut = EventCut.from_dict(_cut)

        _deceleration = d.pop("deceleration", UNSET)
        deceleration: Union[Unset, EventDeceleration]
        if isinstance(_deceleration, Unset):
            deceleration = UNSET
        else:
            deceleration = EventDeceleration.from_dict(_deceleration)

        _defence = d.pop("defence", UNSET)
        defence: Union[Unset, EventDefence]
        if isinstance(_defence, Unset):
            defence = UNSET
        else:
            defence = EventDefence.from_dict(_defence)

        _detected_offside_soccer = d.pop("detected_offside_soccer", UNSET)
        detected_offside_soccer: Union[Unset, EventDetectedOffsideSoccer]
        if isinstance(_detected_offside_soccer, Unset):
            detected_offside_soccer = UNSET
        else:
            detected_offside_soccer = EventDetectedOffsideSoccer.from_dict(_detected_offside_soccer)

        _detected_pass = d.pop("detected_pass", UNSET)
        detected_pass: Union[Unset, EventDetectedPass]
        if isinstance(_detected_pass, Unset):
            detected_pass = UNSET
        else:
            detected_pass = EventDetectedPass.from_dict(_detected_pass)

        _detected_shot_basketball = d.pop("detected_shot_basketball", UNSET)
        detected_shot_basketball: Union[Unset, EventDetectedShotBasketball]
        if isinstance(_detected_shot_basketball, Unset):
            detected_shot_basketball = UNSET
        else:
            detected_shot_basketball = EventDetectedShotBasketball.from_dict(_detected_shot_basketball)

        _detected_shot_fifa = d.pop("detected_shot_fifa", UNSET)
        detected_shot_fifa: Union[Unset, EventDetectedShotFifa]
        if isinstance(_detected_shot_fifa, Unset):
            detected_shot_fifa = UNSET
        else:
            detected_shot_fifa = EventDetectedShotFifa.from_dict(_detected_shot_fifa)

        _detected_shot_handball = d.pop("detected_shot_handball", UNSET)
        detected_shot_handball: Union[Unset, EventDetectedShotHandball]
        if isinstance(_detected_shot_handball, Unset):
            detected_shot_handball = UNSET
        else:
            detected_shot_handball = EventDetectedShotHandball.from_dict(_detected_shot_handball)

        _detected_shot_ice_hockey = d.pop("detected_shot_ice_hockey", UNSET)
        detected_shot_ice_hockey: Union[Unset, EventDetectedShotIceHockey]
        if isinstance(_detected_shot_ice_hockey, Unset):
            detected_shot_ice_hockey = UNSET
        else:
            detected_shot_ice_hockey = EventDetectedShotIceHockey.from_dict(_detected_shot_ice_hockey)

        _detected_shot_intelligence_court = d.pop("detected_shot_intelligence_court", UNSET)
        detected_shot_intelligence_court: Union[Unset, EventDetectedShotIntelligenceCourt]
        if isinstance(_detected_shot_intelligence_court, Unset):
            detected_shot_intelligence_court = UNSET
        else:
            detected_shot_intelligence_court = EventDetectedShotIntelligenceCourt.from_dict(
                _detected_shot_intelligence_court
            )

        _detected_shot_soccer = d.pop("detected_shot_soccer", UNSET)
        detected_shot_soccer: Union[Unset, EventDetectedShotSoccer]
        if isinstance(_detected_shot_soccer, Unset):
            detected_shot_soccer = UNSET
        else:
            detected_shot_soccer = EventDetectedShotSoccer.from_dict(_detected_shot_soccer)

        _dfl_corner_kick = d.pop("dfl_corner_kick", UNSET)
        dfl_corner_kick: Union[Unset, EventDflCornerKick]
        if isinstance(_dfl_corner_kick, Unset):
            dfl_corner_kick = UNSET
        else:
            dfl_corner_kick = EventDflCornerKick.from_dict(_dfl_corner_kick)

        _dfl_cross = d.pop("dfl_cross", UNSET)
        dfl_cross: Union[Unset, EventDflCross]
        if isinstance(_dfl_cross, Unset):
            dfl_cross = UNSET
        else:
            dfl_cross = EventDflCross.from_dict(_dfl_cross)

        _dfl_free_kick = d.pop("dfl_free_kick", UNSET)
        dfl_free_kick: Union[Unset, EventDflFreeKick]
        if isinstance(_dfl_free_kick, Unset):
            dfl_free_kick = UNSET
        else:
            dfl_free_kick = EventDflFreeKick.from_dict(_dfl_free_kick)

        _dfl_goal_kick = d.pop("dfl_goal_kick", UNSET)
        dfl_goal_kick: Union[Unset, EventDflGoalKick]
        if isinstance(_dfl_goal_kick, Unset):
            dfl_goal_kick = UNSET
        else:
            dfl_goal_kick = EventDflGoalKick.from_dict(_dfl_goal_kick)

        _dfl_kick_off = d.pop("dfl_kick_off", UNSET)
        dfl_kick_off: Union[Unset, EventDflKickOff]
        if isinstance(_dfl_kick_off, Unset):
            dfl_kick_off = UNSET
        else:
            dfl_kick_off = EventDflKickOff.from_dict(_dfl_kick_off)

        _dfl_pass = d.pop("dfl_pass", UNSET)
        dfl_pass: Union[Unset, EventDflPass]
        if isinstance(_dfl_pass, Unset):
            dfl_pass = UNSET
        else:
            dfl_pass = EventDflPass.from_dict(_dfl_pass)

        _dfl_penalty = d.pop("dfl_penalty", UNSET)
        dfl_penalty: Union[Unset, EventDflPenalty]
        if isinstance(_dfl_penalty, Unset):
            dfl_penalty = UNSET
        else:
            dfl_penalty = EventDflPenalty.from_dict(_dfl_penalty)

        _dfl_shot_at_goal = d.pop("dfl_shot_at_goal", UNSET)
        dfl_shot_at_goal: Union[Unset, EventDflShotAtGoal]
        if isinstance(_dfl_shot_at_goal, Unset):
            dfl_shot_at_goal = UNSET
        else:
            dfl_shot_at_goal = EventDflShotAtGoal.from_dict(_dfl_shot_at_goal)

        _dfl_sprint = d.pop("dfl_sprint", UNSET)
        dfl_sprint: Union[Unset, EventDflSprint]
        if isinstance(_dfl_sprint, Unset):
            dfl_sprint = UNSET
        else:
            dfl_sprint = EventDflSprint.from_dict(_dfl_sprint)

        _dfl_tackling = d.pop("dfl_tackling", UNSET)
        dfl_tackling: Union[Unset, EventDflTackling]
        if isinstance(_dfl_tackling, Unset):
            dfl_tackling = UNSET
        else:
            dfl_tackling = EventDflTackling.from_dict(_dfl_tackling)

        _dfl_throw_in = d.pop("dfl_throw_in", UNSET)
        dfl_throw_in: Union[Unset, EventDflThrowIn]
        if isinstance(_dfl_throw_in, Unset):
            dfl_throw_in = UNSET
        else:
            dfl_throw_in = EventDflThrowIn.from_dict(_dfl_throw_in)

        _down_on_pads = d.pop("down_on_pads", UNSET)
        down_on_pads: Union[Unset, EventDownOnPads]
        if isinstance(_down_on_pads, Unset):
            down_on_pads = UNSET
        else:
            down_on_pads = EventDownOnPads.from_dict(_down_on_pads)

        _dribbling_soccer = d.pop("dribbling_soccer", UNSET)
        dribbling_soccer: Union[Unset, EventDribblingSoccer]
        if isinstance(_dribbling_soccer, Unset):
            dribbling_soccer = UNSET
        else:
            dribbling_soccer = EventDribblingSoccer.from_dict(_dribbling_soccer)

        _dynamic_defence = d.pop("dynamic_defence", UNSET)
        dynamic_defence: Union[Unset, EventDynamicDefence]
        if isinstance(_dynamic_defence, Unset):
            dynamic_defence = UNSET
        else:
            dynamic_defence = EventDynamicDefence.from_dict(_dynamic_defence)

        _exertion = d.pop("exertion", UNSET)
        exertion: Union[Unset, EventExertion]
        if isinstance(_exertion, Unset):
            exertion = UNSET
        else:
            exertion = EventExertion.from_dict(_exertion)

        _full_court_transition = d.pop("full_court_transition", UNSET)
        full_court_transition: Union[Unset, EventFullCourtTransition]
        if isinstance(_full_court_transition, Unset):
            full_court_transition = UNSET
        else:
            full_court_transition = EventFullCourtTransition.from_dict(_full_court_transition)

        _goal_kick = d.pop("goal_kick", UNSET)
        goal_kick: Union[Unset, EventGoalKick]
        if isinstance(_goal_kick, Unset):
            goal_kick = UNSET
        else:
            goal_kick = EventGoalKick.from_dict(_goal_kick)

        _goalkeeper_save_diving = d.pop("goalkeeper_save_diving", UNSET)
        goalkeeper_save_diving: Union[Unset, EventGoalkeeperSaveDiving]
        if isinstance(_goalkeeper_save_diving, Unset):
            goalkeeper_save_diving = UNSET
        else:
            goalkeeper_save_diving = EventGoalkeeperSaveDiving.from_dict(_goalkeeper_save_diving)

        _goalkeeper_save_down_to_knees = d.pop("goalkeeper_save_down_to_knees", UNSET)
        goalkeeper_save_down_to_knees: Union[Unset, EventGoalkeeperSaveDownToKnees]
        if isinstance(_goalkeeper_save_down_to_knees, Unset):
            goalkeeper_save_down_to_knees = UNSET
        else:
            goalkeeper_save_down_to_knees = EventGoalkeeperSaveDownToKnees.from_dict(_goalkeeper_save_down_to_knees)

        _goalkeeper_save_tilting = d.pop("goalkeeper_save_tilting", UNSET)
        goalkeeper_save_tilting: Union[Unset, EventGoalkeeperSaveTilting]
        if isinstance(_goalkeeper_save_tilting, Unset):
            goalkeeper_save_tilting = UNSET
        else:
            goalkeeper_save_tilting = EventGoalkeeperSaveTilting.from_dict(_goalkeeper_save_tilting)

        _group_counter_pressing = d.pop("group_counter_pressing", UNSET)
        group_counter_pressing: Union[Unset, EventGroupCounterPressing]
        if isinstance(_group_counter_pressing, Unset):
            group_counter_pressing = UNSET
        else:
            group_counter_pressing = EventGroupCounterPressing.from_dict(_group_counter_pressing)

        _group_empty_goal_handball = d.pop("group_empty_goal_handball", UNSET)
        group_empty_goal_handball: Union[Unset, EventGroupEmptyGoalHandball]
        if isinstance(_group_empty_goal_handball, Unset):
            group_empty_goal_handball = UNSET
        else:
            group_empty_goal_handball = EventGroupEmptyGoalHandball.from_dict(_group_empty_goal_handball)

        _heart_rate_recovery = d.pop("heart_rate_recovery", UNSET)
        heart_rate_recovery: Union[Unset, EventHeartRateRecovery]
        if isinstance(_heart_rate_recovery, Unset):
            heart_rate_recovery = UNSET
        else:
            heart_rate_recovery = EventHeartRateRecovery.from_dict(_heart_rate_recovery)

        _impact = d.pop("impact", UNSET)
        impact: Union[Unset, EventImpact]
        if isinstance(_impact, Unset):
            impact = UNSET
        else:
            impact = EventImpact.from_dict(_impact)

        _jump_beach_volleyball = d.pop("jump_beach_volleyball", UNSET)
        jump_beach_volleyball: Union[Unset, EventJumpBeachVolleyball]
        if isinstance(_jump_beach_volleyball, Unset):
            jump_beach_volleyball = UNSET
        else:
            jump_beach_volleyball = EventJumpBeachVolleyball.from_dict(_jump_beach_volleyball)

        _jump = d.pop("jump", UNSET)
        jump: Union[Unset, EventJump]
        if isinstance(_jump, Unset):
            jump = UNSET
        else:
            jump = EventJump.from_dict(_jump)

        _mid_court_transition = d.pop("mid_court_transition", UNSET)
        mid_court_transition: Union[Unset, EventMidCourtTransition]
        if isinstance(_mid_court_transition, Unset):
            mid_court_transition = UNSET
        else:
            mid_court_transition = EventMidCourtTransition.from_dict(_mid_court_transition)

        _noah_shot = d.pop("noah_shot", UNSET)
        noah_shot: Union[Unset, EventNoahShot]
        if isinstance(_noah_shot, Unset):
            noah_shot = UNSET
        else:
            noah_shot = EventNoahShot.from_dict(_noah_shot)

        _offence = d.pop("offence", UNSET)
        offence: Union[Unset, EventOffence]
        if isinstance(_offence, Unset):
            offence = UNSET
        else:
            offence = EventOffence.from_dict(_offence)

        _pass_fifa = d.pop("pass_fifa", UNSET)
        pass_fifa: Union[Unset, EventPassFifa]
        if isinstance(_pass_fifa, Unset):
            pass_fifa = UNSET
        else:
            pass_fifa = EventPassFifa.from_dict(_pass_fifa)

        _pick_and_pop = d.pop("pick_and_pop", UNSET)
        pick_and_pop: Union[Unset, EventPickAndPop]
        if isinstance(_pick_and_pop, Unset):
            pick_and_pop = UNSET
        else:
            pick_and_pop = EventPickAndPop.from_dict(_pick_and_pop)

        _pick_and_roll = d.pop("pick_and_roll", UNSET)
        pick_and_roll: Union[Unset, EventPickAndRoll]
        if isinstance(_pick_and_roll, Unset):
            pick_and_roll = UNSET
        else:
            pick_and_roll = EventPickAndRoll.from_dict(_pick_and_roll)

        _pivot_rotation = d.pop("pivot_rotation", UNSET)
        pivot_rotation: Union[Unset, EventPivotRotation]
        if isinstance(_pivot_rotation, Unset):
            pivot_rotation = UNSET
        else:
            pivot_rotation = EventPivotRotation.from_dict(_pivot_rotation)

        _play_by_player = d.pop("play_by_player", UNSET)
        play_by_player: Union[Unset, EventPlayByPlayer]
        if isinstance(_play_by_player, Unset):
            play_by_player = UNSET
        else:
            play_by_player = EventPlayByPlayer.from_dict(_play_by_player)

        _play_by_team = d.pop("play_by_team", UNSET)
        play_by_team: Union[Unset, EventPlayByTeam]
        if isinstance(_play_by_team, Unset):
            play_by_team = UNSET
        else:
            play_by_team = EventPlayByTeam.from_dict(_play_by_team)

        _player_counter_pressing = d.pop("player_counter_pressing", UNSET)
        player_counter_pressing: Union[Unset, EventPlayerCounterPressing]
        if isinstance(_player_counter_pressing, Unset):
            player_counter_pressing = UNSET
        else:
            player_counter_pressing = EventPlayerCounterPressing.from_dict(_player_counter_pressing)

        _rally_beach_volleyball = d.pop("rally_beach_volleyball", UNSET)
        rally_beach_volleyball: Union[Unset, EventRallyBeachVolleyball]
        if isinstance(_rally_beach_volleyball, Unset):
            rally_beach_volleyball = UNSET
        else:
            rally_beach_volleyball = EventRallyBeachVolleyball.from_dict(_rally_beach_volleyball)

        _rspct_shot = d.pop("rspct_shot", UNSET)
        rspct_shot: Union[Unset, EventRspctShot]
        if isinstance(_rspct_shot, Unset):
            rspct_shot = UNSET
        else:
            rspct_shot = EventRspctShot.from_dict(_rspct_shot)

        _shift = d.pop("shift", UNSET)
        shift: Union[Unset, EventShift]
        if isinstance(_shift, Unset):
            shift = UNSET
        else:
            shift = EventShift.from_dict(_shift)

        _skating_transition = d.pop("skating_transition", UNSET)
        skating_transition: Union[Unset, EventSkatingTransition]
        if isinstance(_skating_transition, Unset):
            skating_transition = UNSET
        else:
            skating_transition = EventSkatingTransition.from_dict(_skating_transition)

        _speed_zone_entry = d.pop("speed_zone_entry", UNSET)
        speed_zone_entry: Union[Unset, EventSpeedZoneEntry]
        if isinstance(_speed_zone_entry, Unset):
            speed_zone_entry = UNSET
        else:
            speed_zone_entry = EventSpeedZoneEntry.from_dict(_speed_zone_entry)

        _speed_zone_entry_relative = d.pop("speed_zone_entry_relative", UNSET)
        speed_zone_entry_relative: Union[Unset, EventSpeedZoneEntryRelative]
        if isinstance(_speed_zone_entry_relative, Unset):
            speed_zone_entry_relative = UNSET
        else:
            speed_zone_entry_relative = EventSpeedZoneEntryRelative.from_dict(_speed_zone_entry_relative)

        _sprint = d.pop("sprint", UNSET)
        sprint: Union[Unset, EventSprint]
        if isinstance(_sprint, Unset):
            sprint = UNSET
        else:
            sprint = EventSprint.from_dict(_sprint)

        _tag = d.pop("tag", UNSET)
        tag: Union[Unset, EventTag]
        if isinstance(_tag, Unset):
            tag = UNSET
        else:
            tag = EventTag.from_dict(_tag)

        _tempo_run = d.pop("tempo_run", UNSET)
        tempo_run: Union[Unset, EventTempoRun]
        if isinstance(_tempo_run, Unset):
            tempo_run = UNSET
        else:
            tempo_run = EventTempoRun.from_dict(_tempo_run)

        _throw_in = d.pop("throw_in", UNSET)
        throw_in: Union[Unset, EventThrowIn]
        if isinstance(_throw_in, Unset):
            throw_in = UNSET
        else:
            throw_in = EventThrowIn.from_dict(_throw_in)

        _turn_ice_hockey = d.pop("turn_ice_hockey", UNSET)
        turn_ice_hockey: Union[Unset, EventTurnIceHockey]
        if isinstance(_turn_ice_hockey, Unset):
            turn_ice_hockey = UNSET
        else:
            turn_ice_hockey = EventTurnIceHockey.from_dict(_turn_ice_hockey)

        event_types = cls(
            acceleration=acceleration,
            ball_contact=ball_contact,
            ball_possession=ball_possession,
            ball_possession_lost=ball_possession_lost,
            ball_possession_recovery=ball_possession_recovery,
            cv_shot=cv_shot,
            change_of_direction=change_of_direction,
            change_of_orientation=change_of_orientation,
            change_of_pace=change_of_pace,
            corner_kick=corner_kick,
            counter_attack=counter_attack,
            detected_cross=detected_cross,
            cut=cut,
            deceleration=deceleration,
            defence=defence,
            detected_offside_soccer=detected_offside_soccer,
            detected_pass=detected_pass,
            detected_shot_basketball=detected_shot_basketball,
            detected_shot_fifa=detected_shot_fifa,
            detected_shot_handball=detected_shot_handball,
            detected_shot_ice_hockey=detected_shot_ice_hockey,
            detected_shot_intelligence_court=detected_shot_intelligence_court,
            detected_shot_soccer=detected_shot_soccer,
            dfl_corner_kick=dfl_corner_kick,
            dfl_cross=dfl_cross,
            dfl_free_kick=dfl_free_kick,
            dfl_goal_kick=dfl_goal_kick,
            dfl_kick_off=dfl_kick_off,
            dfl_pass=dfl_pass,
            dfl_penalty=dfl_penalty,
            dfl_shot_at_goal=dfl_shot_at_goal,
            dfl_sprint=dfl_sprint,
            dfl_tackling=dfl_tackling,
            dfl_throw_in=dfl_throw_in,
            down_on_pads=down_on_pads,
            dribbling_soccer=dribbling_soccer,
            dynamic_defence=dynamic_defence,
            exertion=exertion,
            full_court_transition=full_court_transition,
            goal_kick=goal_kick,
            goalkeeper_save_diving=goalkeeper_save_diving,
            goalkeeper_save_down_to_knees=goalkeeper_save_down_to_knees,
            goalkeeper_save_tilting=goalkeeper_save_tilting,
            group_counter_pressing=group_counter_pressing,
            group_empty_goal_handball=group_empty_goal_handball,
            heart_rate_recovery=heart_rate_recovery,
            impact=impact,
            jump_beach_volleyball=jump_beach_volleyball,
            jump=jump,
            mid_court_transition=mid_court_transition,
            noah_shot=noah_shot,
            offence=offence,
            pass_fifa=pass_fifa,
            pick_and_pop=pick_and_pop,
            pick_and_roll=pick_and_roll,
            pivot_rotation=pivot_rotation,
            play_by_player=play_by_player,
            play_by_team=play_by_team,
            player_counter_pressing=player_counter_pressing,
            rally_beach_volleyball=rally_beach_volleyball,
            rspct_shot=rspct_shot,
            shift=shift,
            skating_transition=skating_transition,
            speed_zone_entry=speed_zone_entry,
            speed_zone_entry_relative=speed_zone_entry_relative,
            sprint=sprint,
            tag=tag,
            tempo_run=tempo_run,
            throw_in=throw_in,
            turn_ice_hockey=turn_ice_hockey,
        )

        event_types.additional_properties = d
        return event_types

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
