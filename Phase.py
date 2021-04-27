from enum import Enum

class Phase(Enum):
    START = 0
    QUEUE = 1
    REGISTRATION = 2
    CHAIR_SELECION = 3
    WAITING_FOR_SURGERY = 4
    SURGERY = 5
    DEAD = 6
    HEALED = 7
