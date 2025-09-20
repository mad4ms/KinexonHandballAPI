from enum import Enum


class EventGoalkeeperSaveDownToKneesGoalkeeperSaveDownToKneesCategory(str, Enum):
    FORWARD = "forward"
    LEFT = "left"
    RIGHT = "right"

    def __str__(self) -> str:
        return str(self.value)
