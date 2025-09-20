from enum import Enum


class GetPublicV1StatisticsByTypeByPlayerIdByTimeEntityTypeByTimeEntityIdentifierType(str, Enum):
    PLAYER = "player"
    PLAYERS = "players"

    def __str__(self) -> str:
        return str(self.value)
