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

        

    def take_surgery(self):
        patient = self.sitting_patient = None
        self.sitting_patient = None
        self.place_taken.release()
        return patient
