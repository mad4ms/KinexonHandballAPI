from enum import Enum


class EventDflCrossDflCrossCategory(str, Enum):
    MISSED = "missed"
    SUCCESSFUL = "successful"

    def __str__(self) -> str:
        return str(self.value)
