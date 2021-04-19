from enum import Enum
class Location(Enum):

    RECEPTION    = 1    # RECEPCJA
    CORRIDOR     = 2    # KORYTARZ, POKÓJ OCZEKIWAŃ, waitingRoom
    SURGERY_ROOM = 3    # Sala operacyjna
    MEDICAL_ROOM = 4    # Pokój lekarski