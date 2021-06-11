from threading import Lock


class Chair:
    def __init__(self, _id):
        self.id = _id
        self.sitting_patient = None
        self.place_taken = Lock()
        pass

    def sit_down(self, patient):
        if self.place_taken.acquire(False):
            self.sitting_patient = patient
            return True
        else:
            return False

    def release_chair(self):
        self.sitting_patient = None
        if self.place_taken.locked:
            self.place_taken.release()
