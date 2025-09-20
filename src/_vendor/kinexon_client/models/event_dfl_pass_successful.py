from enum import Enum


class EventDflPassSuccessful(str, Enum):
    DFL_PASS_MISSED = "dfl_pass_missed"
    DFL_PASS_SUCCESSFUL = "dfl_pass_successful"

    def __str__(self) -> str:
        return str(self.value)
