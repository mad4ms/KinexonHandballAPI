from enum import Enum


class GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecatedType(str, Enum):
    PLAYER = "player"
    PLAYERS = "players"

    def __str__(self) -> str:
        return str(self.value)
