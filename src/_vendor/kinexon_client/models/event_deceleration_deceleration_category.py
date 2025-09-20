from enum import Enum


class EventDecelerationDecelerationCategory(str, Enum):
    CATEGORY1 = "category1"
    CATEGORY2 = "category2"
    CATEGORY3 = "category3"
    CATEGORY4 = "category4"
    CATEGORY5 = "category5"
    CATEGORY6 = "category6"
    CATEGORY7 = "category7"

    def __str__(self) -> str:
        return str(self.value)
