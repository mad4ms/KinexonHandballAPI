from enum import Enum


class EventRspctShotMade(str, Enum):
    SUCCESSFUL = "successful"
    UNSUCCESSFUL = "unsuccessful"

    def __str__(self) -> str:
        return str(self.value)
