from enum import Enum


class EventTurnIceHockeyTurnCategory(str, Enum):
    SHARP_TURN = "sharp_turn"
    WIDE_TURN = "wide_turn"

    def __str__(self) -> str:
        return str(self.value)
