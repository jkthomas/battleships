from enum import Enum


class AIState(Enum):
    Searching = 0
    Hit = 1
    HitTop = 2
    HitBottom = 3
    HitLeft = 4
    HitRight = 5