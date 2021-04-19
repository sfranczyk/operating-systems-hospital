from patient import Patient
from surgery_room import surgery_room
from Location import Location
import threading
import time
from datetime import datetime
from threading import Lock

class doctor(threading.Thread):
    max_energy_points = 100   

    def __init__(self, energy_points, chairs, location):
        self.energy_points = energy_points
        self.chairs = chairs
        self.choosen_patient : Patient = None
        self.location = location
        self.surgery_room : surgery_room = None

        threading.Thread.__init__(self)

    def run(self):
        while(True):
            if self.location == Location.CORRIDOR:
                if self.surgery_room:
                    self.location = Location.SURGERY_ROOM
            if self.location == Location.SURGERY_ROOM:
                # end surgery
                if not self.surgery_room.is_used:
                    doctor.choosen_patient = None
                    doctor.location = Location.CORRIDOR
                # surgery
                elif self.energy_points == 0:
                    self.surgery_room.stop_surgery();
                    doctor.location = Location.MEDICAL_ROOM
                else:
                    self.choosen_patient.health_points += 1
                    self.energy_points -= 1
                if self.choosen_patient.health_points >= Patient.max_hp:
                    self.surgery_room.complete_surgery()

            if self.location == Location.MEDICAL_ROOM:
                # TODO
                pass


