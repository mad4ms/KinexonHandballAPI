from enum import Enum


class EventDflThrowInDflThrowInCategory(str, Enum):
    FAULT_EXECUTION = "fault_execution"
    MISSED = "missed"
    SUCCESSFUL = "successful"

    def __str__(self) -> str:
        return str(self.value)
