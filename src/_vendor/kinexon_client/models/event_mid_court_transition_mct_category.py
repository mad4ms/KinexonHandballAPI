from enum import Enum


class EventMidCourtTransitionMctCategory(str, Enum):
    CATEGORY1 = "category1"
    CATEGORY2 = "category2"
    CATEGORY3 = "category3"

    def __str__(self) -> str:
        return str(self.value)
