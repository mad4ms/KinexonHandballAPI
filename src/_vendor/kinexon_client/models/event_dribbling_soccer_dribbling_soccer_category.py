from enum import Enum


class EventDribblingSoccerDribblingSoccerCategory(str, Enum):
    BALL_HOLDING = "ball_holding"
    OVERCOME_OPPONENT = "overcome_opponent"
    TEMPO = "tempo"

    def __str__(self) -> str:
        return str(self.value)
