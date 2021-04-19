import threading
import time
from datetime import datetime
from threading import Lock
from Location import Location
from doctor import doctor


class patient_selection(threading.Thread):
    doctors_lock = Lock()

    def __init__(self, doctors, chairs, surgery_rooms):
        self.chairs = chairs
        self.doctors = doctors
        self.surgery_rooms = surgery_rooms

    def choose_patient(self):
        most_valuable_patient = None
        most_valuable_patient_chair = None

        for doctor in self.doctors:
            if doctor.location == Location.CORRIDOR:
                max_points = 0
                for chair in self.chairs:
                    if chair.sitting_patient.current_doctors < chair.sitting_patient.doctors_needed:
                        actual_points = 2 * chair.sitting_patient.health_points + 0.5 * \
                            (datetime.now() -
                             chair.sitting_patient.time_to_start_waiting_for_the_surgery)
                        if actual_points > max_points:
                            max_points = actual_points
                            most_valuable_patient = chair.sitting_patient
                            most_valuable_patient_chair = chair

                most_valuable_patient.current_doctors += 1
                doctor.choosen_patient = most_valuable_patient

                if most_valuable_patient.current_doctors == most_valuable_patient.doctors_needed:
                    self.start_surgery(most_valuable_patient_chair)


    def start_surgery(self, chair):

        free_room = None
        while not free_room:
            for surgery_room in self.surgery_rooms:
                if surgery_room.is_used == False:
                    free_room = surgery_room
                    break

        patient = chair.take_surgery()
        patient.location = Location.SURGERY_ROOM

        for doctor in self.doctors:
            if doctor.choosen_patient == patient:
                doctor.surgery_room = free_room
            # if doctor.choosen_patient == patient:
            #     doctor.location = Location.SURGERY_ROOM
        
        free_room.take_room()
