from enum import Enum


class EventDflFreeKickDflFreeKickCategory(str, Enum):
    MISSED = "missed"
    SUCCESSFUL = "successful"

    def __str__(self) -> str:
        return str(self.value)
