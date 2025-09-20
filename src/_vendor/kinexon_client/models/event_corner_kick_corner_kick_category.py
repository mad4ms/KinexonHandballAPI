from enum import Enum


class EventCornerKickCornerKickCategory(str, Enum):
    CROSS_BOX = "cross_box"
    CROSS_LONG = "cross_long"
    CROSS_MEDIUM = "cross_medium"
    CROSS_SHORT = "cross_short"
    SHORT = "short"

    def __str__(self) -> str:
        return str(self.value)
