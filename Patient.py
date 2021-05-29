import threading
import random
import time
from datetime import datetime

from Location import Location
import Receptionist
import Chair
import Statistics
from Phase import Phase
from threading import Lock


class Patient(threading.Thread):
    max_hp = 100

    def __init__(self, id, hp, name, location, receptionists, chairs, statistics, interface):
        super(Patient, self).__init__()
        self.id = id
        self.name = name
        self.health_points = hp
        self.location = location
        self.receptionists = receptionists
        self.chairs = chairs
        self.phase = Phase.START
        self.is_sitting = False
        self.points = self.max_hp - hp
        self.doctors = []    
        self.doctors_needed = 0
        self.current_doctors_number = 0
        self.current_receptionist = None
        self.time_to_start_waiting_for_the_surgery = None

        self.statistics: Statistics = statistics
        self.interface = interface

    # Thread method
    # 1) Patient should first choose queue to receptionist
    # 2) Patient should register himself
    # 3) Patient should choose the chair
    # 4) Patient should waiting to surgery

    def run(self):
        while(0 < self.health_points < Patient.max_hp):

            self.interface.displayText(self.name, 0, int(self.id), length=35)
            self.interface.displayText(str(self.health_points), 35, int(self.id), length=15, color=3)
            self.interface.displayText(str(self.phase.name), 50, int(self.id), length=50)
           
            for i in range(len(self.chairs)):
                if self.chairs[i].sitting_patient == None:
                    self.interface.displayText('Chair number: ' + str(i + 1) + ' is free', 0, 20 + i, length=25)
                else:
                    self.interface.displayText('Chair number: ' + str(i + 1) + ' is taken', 0, 20 + i, length=25)

            if self.phase == Phase.START:
                self.statistics.new_patient()

                time.sleep(random.uniform(1, 3))                
                self.queue_selection()
                self.phase = Phase.QUEUE

            if self.phase == Phase.QUEUE:
                                
                if self.current_receptionist.current_patient != self.id:                    
                    self.behavior_in_the_registration_queue()                    
                    time.sleep(random.uniform(1, 3))
                else:
                    self.current_receptionist.exit_registration(self.id)
                    self.phase = Phase.REGISTRATION                    

            if self.phase == Phase.REGISTRATION:                
               
                if self.points < 100:
                    self.points += 10
                    time.sleep(random.uniform(1, 3))
                else:
                    self.doctors_needed = self.current_receptionist.registration(
                        self.health_points)
                    
                    self.phase = Phase.CHAIR_SELECION

            if self.phase == Phase.CHAIR_SELECION:
                
                if not self.is_sitting:
                    self.chair_selection()
                    time.sleep(random.uniform(1, 3))
                else:
                    self.time_to_start_waiting_for_the_surgery = datetime.now()
                    self.current_receptionist.exit_registration(id)                    
                    self.phase = Phase.WAITING_FOR_SURGERY

            if self.phase == Phase.WAITING_FOR_SURGERY:
                
                self.waiting_for_surgery()
                time.sleep(random.uniform(1, 3))

            if self.phase == Phase.SURGERY:                
                time.sleep(random.uniform(1, 3))

            self.manage_patient_health_point()

        if self.health_points >= self.max_hp:
            for doctor in self.doctors:
                doctor.choosen_patient = None
                doctor.surgery_room.complete_surgery()
                doctor.location = Location.CORRIDOR

        if self.phase == Phase.HEALED or self.health_points >= self.max_hp:
            self.statistics.patient_healed()            

        if self.phase == Phase.DEAD or self.health_points <= 0:
            self.statistics.patient_died()            

        self.interface.displayText('Wszyscy pacjenci: ' + str(self.statistics.patients_total), 0, 12)
        self.interface.displayText('Wyleczeni: ' + str(self.statistics.patients_healed), 0, 13)
        self.interface.displayText('Zmarli: ' + str(self.statistics.patients_dead), 0, 14)
        
    def manage_patient_health_point(self):

        if self.health_points == Patient.max_hp:
            self.phase == Phase.HEALED

        if self.phase != Phase.DEAD and self.phase != Phase.HEALED and self.phase != Phase.SURGERY:
            self.health_points -= 1

        if self.health_points == 0:
            self.phase == Phase.DEAD

    
    def queue_selection(self):
        self.current_receptionist = min(
            self.receptionists, key=lambda r: r.get_length_queue())
        self.current_receptionist.join_queue(self.id)
    
    
    def behavior_in_the_registration_queue(self):
        self.number_of_queue_change = 0

        for receptionist in self.receptionists:
            if self.current_receptionist.get_position_in_queue(self.id) - self.number_of_queue_change > receptionist.get_length_queue():
                self.change_queue(receptionist)
                self.number_of_queue_change += 1
                break;

    def change_queue(self, new_queue):
        if self.current_receptionist:
            self.current_receptionist.exit_queue(self.id)

        self.current_receptionist = new_queue
        self.current_receptionist.join_queue(self.id)

    def chair_selection(self):
        for chair in self.chairs:
            if chair.sit_down(self):
                self.is_sitting = True
                break

    def waiting_for_surgery(self):
        # TODO waiting, can be as nervous moving of patient? xD
        pass
