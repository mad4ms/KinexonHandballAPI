from enum import Enum


class EventDetectedCrossDetectedCrossCategory(str, Enum):
    MISSED = "missed"
    SUCCESSFUL = "successful"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
