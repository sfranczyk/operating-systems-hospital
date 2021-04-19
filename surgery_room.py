import threading
from Location import Location

class surgery_room(threading.Thread):
    def __init__(self, doctors, patient):
        self.patient_doctors = doctors
        self.patient = patient

    def release_doctors(self):
        for doctor in self.patient_doctors:
            doctor.choosen_patient = None
            doctor.location = Location.CORRIDOR

    def heal_patient(self):
        while self.patient.health_points < 100:
            for doctor in self.patient_doctors:
                if doctor.energy_points > 0:
                    self.patient.health_points += 1
                    doctor.energy_points -= 1
                else:
                    doctor.take_break()
        
        self.patient.doctors_needed = 0
        self.patient.current_doctors_number = 0
        
        self.release_doctors()