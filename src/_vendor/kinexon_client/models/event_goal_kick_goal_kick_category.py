from enum import Enum


class EventGoalKickGoalKickCategory(str, Enum):
    LONG = "long"
    SHORT = "short"

    def __str__(self) -> str:
        return str(self.value)
