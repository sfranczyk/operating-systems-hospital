from CoffeeMachine import CoffeeMachine
from Patient import Patient
from SurgeryRoom import SurgeryRoom
from Location import Location
import threading


class Doctor(threading.Thread):
    max_energy_points = 100

    def __init__(self, id, name, energy_points, chairs, location, coffee_machines):
        super(Doctor, self).__init__()
        self.id = id
        self.name = name
        self.energy_points = energy_points
        self.chairs = chairs
        self.choosen_patient: Patient = None
        self.location = location
        self.surgery_room: SurgeryRoom = None
        self.coffee_machines = coffee_machines
        self.current_coffee_machine: CoffeeMachine = None

    def run(self):
        while(True):
            if self.location == Location.CORRIDOR:
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
                