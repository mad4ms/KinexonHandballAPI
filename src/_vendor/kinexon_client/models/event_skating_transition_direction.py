from enum import Enum


class EventSkatingTransitionDirection(str, Enum):
    LEFT = "left"
    RIGHT = "right"

    def __str__(self) -> str:
        return str(self.value)
