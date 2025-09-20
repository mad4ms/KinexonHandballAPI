from enum import Enum


class EventDflTacklingSuccessful(str, Enum):
    DFL_TACKLING_LOST = "dfl_tackling_lost"
    DFL_TACKLING_WON = "dfl_tackling_won"

    def __str__(self) -> str:
        return str(self.value)
