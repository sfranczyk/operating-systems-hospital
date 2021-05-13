from CoffeeMachine import CoffeeMachine
from Patient import Patient
from SurgeryRoom import SurgeryRoom
from Location import Location
from datetime import datetime
import threading
import random
import time


class Doctor(threading.Thread):
    max_energy_points = 100

    def __init__(self, id, name, energy_points, chairs, location, coffee_machines, surgery_rooms):
        super(Doctor, self).__init__()
        self.id = id
        self.name = name
        self.energy_points = energy_points
        self.chairs = chairs
        self.choosen_patient: Patient = None
        self.location = location
        self.surgery_room: SurgeryRoom = None
        self.surgery_rooms = surgery_rooms
        self.coffee_machines = coffee_machines
        self.current_coffee_machine: CoffeeMachine = None

    def run(self):
        while(True):

            if self.location == Location.CORRIDOR:
                print(f'{self.name} jestem na korytarzu')
                if self.choosen_patient == None:
                    print(f'{self.name} szukam pacjenta')
                    self.choose_patient()
                else:
                    print(
                        f'{self.name}, moj pacjent {self.choosen_patient.name} ma {self.choosen_patient.current_doctors_number} lekarzy')
                    if self.choosen_patient.current_doctors_number >= self.choosen_patient.doctors_needed:
                        self.start_surgery(self.choosen_patient)

                if self.surgery_room:
                    self.location = Location.SURGERY_ROOM

            if self.location == Location.SURGERY_ROOM:

                if not self.surgery_room.is_used:
                    self.choosen_patient = None
                    self.location = Location.CORRIDOR

                elif self.energy_points == 0:
                    self.location = Location.MEDICAL_ROOM
                    self.surgery_room.stop_surgery()

                elif self.surgery_room.surgery_stopped:
                    all_in_surgery_room = True
                    for doctor in self.surgery_room.doctors:
                        if doctor.location != Location.SURGERY_ROOM:
                            all_in_surgery_room = False
                            break
                    if all_in_surgery_room:
                        self.surgery_room.start_surgery()

                else:
                    self.choosen_patient.health_points += 1
                    self.energy_points -= 1

                if self.choosen_patient.health_points >= Patient.max_hp:
                    self.surgery_room.complete_surgery()

            if self.location == Location.MEDICAL_ROOM:
                if not self.current_coffee_machine:
                    for machine in self.coffee_machines:
                        if(machine.try_take(self.id)):
                            self.current_coffee_machine = machine
                            break

                if self.current_coffee_machine and self.energy_points < self.max_energy_points:
                    self.energy_points += self.current_coffee_machine.drink_coffee()

                if self.current_coffee_machine and self.energy_points >= self.max_energy_points:
                    self.current_coffee_machine.release()
                    self.current_coffee_machine = None
                    self.location = Location.SURGERY_ROOM

            time.sleep(random.uniform(2, 5))

    def choose_patient(self):
        most_valuable_patient = None
        max_points = 0

        for chair in self.chairs:
            if chair.sitting_patient != None:
                print('na krzesle siedzi pacjent')
                if chair.sitting_patient.current_doctors < chair.sitting_patient.doctors_needed:
                    actual_points = 2 * chair.sitting_patient.health_points + 0.5 * \
                        (datetime.now() -
                         chair.sitting_patient.time_to_start_waiting_for_the_surgery)
                    if actual_points > max_points:
                        max_points = actual_points
                        most_valuable_patient = chair.sitting_patient
            else:
                print('na krzesle nie ma pacjenta')


        if most_valuable_patient != None:
            print(f'znaleziono {most_valuable_patient.name}')
            most_valuable_patient.current_doctors += 1
            most_valuable_patient.doctors.append(self)
            self.choosen_patient = most_valuable_patient
        else:
            print('nie znaleziono pacjenta')

    def start_surgery(self, patient):

        free_room: SurgeryRoom = None

        while not free_room:
            for surgery_room in self.surgery_rooms:
                if surgery_room.is_used == False:
                    free_room = surgery_room
                    break

        self.surgery_room = free_room

        self.surgery_room.take_room(patient, patient.doctors)
