from enum import Enum


class EventDetectedShotIntelligenceCourtDetectedShotIntelligenceCourtCategory(str, Enum):
    BLOCKED = "blocked"
    GOAL = "goal"
    MISSED = "missed"

    def __str__(self) -> str:
        return str(self.value)
