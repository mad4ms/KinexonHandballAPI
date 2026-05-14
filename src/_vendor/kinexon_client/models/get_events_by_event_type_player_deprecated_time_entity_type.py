from enum import Enum


class GetEventsByEventTypePlayerDeprecatedTimeEntityType(str, Enum):
    PHASE = "phase"
    SESSION = "session"

    def __str__(self) -> str:
        return str(self.value)
