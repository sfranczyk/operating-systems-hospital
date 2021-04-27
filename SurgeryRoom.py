from patient import Patient
import threading
from Location import Location

class surgery_room(threading.Thread):
    def __init__(self):
        self.is_used = False
        self.surgery_stopped = False
        self.doctors_number = 0
        self.patient: Patient = None
        self.doctors = []
        self.lock = threading.Lock()

    def take_room(self, patient, doctors):
        self.surgery_stopped = True
        self.doctors = doctors
        self.patient = patient
        self.doctors_number = len(self.doctors)
        self.is_used = True

    def stop_surgery(self):
        self.surgery_stopped = True

    def start_surgery(self):
        self.surgery_stopped = False

    def complete_surgery(self):
        self.lock.acquire()
        try:
            self.doctors_number -= 1
            if self.doctors_number == 0:
                self.is_used = False
                self.patient = None
        finally:
            self.lock.release()
