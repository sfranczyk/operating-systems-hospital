import threading
import random
import time
from datetime import datetime

from Location import Location
import Receptionist
import Chair

class Patient(threading.Thread):
    max_hp = 100

    def __init__(self, id, hp, name, location, receptionists, chairs):
        super(Patient, self).__init__()
        self.id = id
        self.hp = hp
        self.name = name
        self.location = location
        self.receptionists = receptionists
        self.chairs = chairs

        self.doctors_needed = 0
        self.current_doctors_number = 0

        self.current_receptionist = None
        self.time_to_start_waiting_for_the_surgery = None

        print(f"Created patient {self.name}, and he has such an ID: {self.id}")

    # Thread method
    # 1) Patient should first choose queue to receptionist
    # 2) Patient should register himself
    # 3) Patient should choose the chair
    # 4) Patient should waiting to surgery
    def run(self):
        time.sleep(random.uniform(0.02, 2))
        print(f"Hello, I am {self.name}, and I have such an ID: {self.id}")

        self.queue_selection()

        #self.behavior_in_the_registration_queue()

        self.register()

        # self.chair_selection()

        # self.waiting_for_surgery()


    def queue_selection(self):
        self.current_receptionist = min(self.receptionists, key=lambda r: r.get_length_queue()) # IDK, maybe it's better recording
        self.current_receptionist.join_queue(self.id)
    

    def behavior_in_the_registration_queue(self):
        number_of_queue_change = 0

        while(self.current_receptionist.current_patient != self.id):
            for receptionist in self.receptionists:
                if self.current_receptionist.get_position_in_queue(self.id) - number_of_queue_change > receptionist.get_length_queue():                                  
                    self.change_queue(receptionist)
                    number_of_queue_change += 1

            print(f"Im {self.id} waiting!!! in receptionist number: {self.current_receptionist.id}, {actual_position}, {self.current_receptionist.get_length_queue()}")
            time.sleep(1) #TODO Increase time range


    def change_queue(self, new_queue):
        if self.current_receptionist:
            self.current_receptionist.exit_queue(self.id)

        self.current_receptionist = new_queue
        new_queue.join_queue(self.id)
        


    def register(self):        
        self.doctors_needed = self.current_receptionist.registration(self.hp)

        print(f"Id pacjenta: {self.id} hp: {self.hp} liczba lekarzy: {self.doctors_needed}")


    def chair_selection(self):
        # TODO selection of the chair

        self.time_to_start_waiting_for_the_surgery = datetime.now()
        self.current_receptionist.exit_registration(id)
        self.location = Location.CORRIDOR
        pass


    def waiting_for_surgery(self):
        # TODO waiting, can be as nervous moving of patient? xD
        pass

