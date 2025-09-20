from enum import Enum


class EventDflPenaltySuccessful(str, Enum):
    DFL_PENALTY_MISSED = "dfl_penalty_missed"
    DFL_PENALTY_SUCCESSFUL = "dfl_penalty_successful"

    def __str__(self) -> str:
        return str(self.value)
