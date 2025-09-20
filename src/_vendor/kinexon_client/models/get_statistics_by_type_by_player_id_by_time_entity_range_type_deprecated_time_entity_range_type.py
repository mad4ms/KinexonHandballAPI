from enum import Enum


class GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedTimeEntityRangeType(str, Enum):
    PHASES = "phases"
    SESSIONS = "sessions"

    def __str__(self) -> str:
        return str(self.value)
