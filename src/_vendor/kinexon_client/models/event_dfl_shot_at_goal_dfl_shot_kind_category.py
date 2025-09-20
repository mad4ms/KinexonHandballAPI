from enum import Enum


class EventDflShotAtGoalDflShotKindCategory(str, Enum):
    SHOT_AT_GOAL_BLOCKED = "shot_at_goal_blocked"
    SHOT_AT_GOAL_OTHER = "shot_at_goal_other"
    SHOT_AT_GOAL_SAVED = "shot_at_goal_saved"
    SHOT_AT_GOAL_SUCCESSFUL = "shot_at_goal_successful"
    SHOT_AT_GOAL_WIDE = "shot_at_goal_wide"

    def __str__(self) -> str:
        return str(self.value)
