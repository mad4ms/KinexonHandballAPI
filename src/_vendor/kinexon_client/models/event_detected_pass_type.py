from enum import Enum


class EventDetectedPassType(str, Enum):
    ALMOST_FATAL = "almost_fatal"
    FATAL = "fatal"
    MISSED = "missed"
    SUCCESSFUL = "successful"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
