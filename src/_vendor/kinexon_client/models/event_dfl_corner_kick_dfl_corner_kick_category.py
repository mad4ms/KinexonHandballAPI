from enum import Enum


class EventDflCornerKickDflCornerKickCategory(str, Enum):
    MISSED_PLAY = "missed_play"
    MISSED_SHOT = "missed_shot"
    SUCCESSFUL_PLAY = "successful_play"
    SUCCESSFUL_SHOT = "successful_shot"

    def __str__(self) -> str:
        return str(self.value)
