from enum import Enum


class EventPlayerCounterPressingPlayerCounterPressingCategory(str, Enum):
    CLOSE_PRESSURE = "close_pressure"
    RUNNING_TO_PRESSURE = "running_to_pressure"

    def __str__(self) -> str:
        return str(self.value)
