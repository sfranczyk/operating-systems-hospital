from CoffeeMachine import CoffeeMachine
from Patient import Patient
from SurgeryRoom import SurgeryRoom
from Location import Location
from datetime import datetime
import threading
import random
import time
from Phase import Phase


class Doctor(threading.Thread):
    max_energy_points = 100

    def __init__(self, id, name, energy_points, chairs, location, coffee_machines, surgery_rooms, interface):
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
        self.interface = interface

    def run(self):
        while(True):

            self.interface.displayText(self.name, 100, self.id, length=30)
            self.interface.displayText(str(self.energy_points), 130, self.id, length=25, color=2)
            if not self.choosen_patient == None:
                self.interface.displayText(self.choosen_patient.name, 155, self.id, length=45)             

            if self.location == Location.CORRIDOR:

                if self.choosen_patient == None:
                    self.choose_patient()
                else:
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
                    if self.choosen_patient != None:
                        self.choosen_patient.phase = Phase.SURGERY
                        self.choosen_patient.health_points += 1
                        self.energy_points -= 1
                                                                
            if self.location == Location.MEDICAL_ROOM:
                
                if not self.current_coffee_machine:
                    for machine in self.coffee_machines:
                        if(machine.try_take(self.id)):
                            self.current_coffee_machine = machine
                            break

                if self.current_coffee_machine and self.energy_points < self.max_energy_points:
                    self.energy_points += self.current_coffee_machine.drink_coffee()
                    self.choosen_patient.health_points -= 1

                if self.current_coffee_machine and self.energy_points >= self.max_energy_points:
                    self.current_coffee_machine.release()
                    self.current_coffee_machine = None
                    self.location = Location.SURGERY_ROOM

            time.sleep(random.uniform(1, 3))

    def choose_patient(self):
        most_valuable_patient = None
        max_points = 0

        for chair in self.chairs:
            if chair.sitting_patient != None:

                if chair.sitting_patient.current_doctors_number < chair.sitting_patient.doctors_needed:
                    actual_points = 2 * chair.sitting_patient.health_points
                    if actual_points > max_points:
                        max_points = actual_points
                        most_valuable_patient = chair.sitting_patient

        if most_valuable_patient != None:            
            most_valuable_patient.current_doctors_number += 1
            most_valuable_patient.doctors.append(self)
            self.choosen_patient = most_valuable_patient

    def start_surgery(self, patient):

        free_room: SurgeryRoom = None

        while not free_room:
            for surgery_room in self.surgery_rooms:
                if surgery_room.is_used == False:
                    free_room = surgery_room
                    break

        patient.phase = Phase.SURGERY
        self.surgery_room = free_room
        self.surgery_room.take_room(patient, patient.doctors)
