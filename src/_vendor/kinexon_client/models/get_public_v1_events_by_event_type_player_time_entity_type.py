from enum import Enum


class GetPublicV1EventsByEventTypePlayerTimeEntityType(str, Enum):
    PHASE = "phase"
    SESSION = "session"

    def __str__(self) -> str:
        return str(self.value)
