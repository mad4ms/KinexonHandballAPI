from enum import Enum


class TimeEntityIdentifierQuickIdentifier(str, Enum):
    CURRENT = "current"
    LATEST = "latest"

    def __str__(self) -> str:
        return str(self.value)
