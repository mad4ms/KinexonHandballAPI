from enum import Enum


class EventJumpBeachVolleyballJumpBeachVolleyballCategory(str, Enum):
    ATTACK = "attack"
    BLOCK = "block"
    FAKE_ATTACK = "fake_attack"
    OTHER = "other"
    PASS = "pass"
    RUNNING_SERVE = "running_serve"
    SERVE = "serve"

    def __str__(self) -> str:
        return str(self.value)
