from enum import Enum


class GetStatisticsByTypeByPlayerIdByTimeEntityTypeByTimeEntityIdentifierDeprecatedType(str, Enum):
    PLAYER = "player"
    PLAYERS = "players"

    def __str__(self) -> str:
        return str(self.value)
