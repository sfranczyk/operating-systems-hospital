import threading
import random
import time
import datetime

import Location
import Receptionist
import Chair

class Patient(threading.Thread):
    max_hp = 1000

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

        # self.behavior_in_the_registration_queue()

        # self.register()

        # self.chair_selection()

        # self.waiting_for_surgery()


    def queue_selection(self):
        self.current_receptionist = min(self.receptionists, key=lambda r: r.get_length_queue()) # IDK, maybe it's better recording
        self.current_receptionist.join_queue(self.id)

        # reception_with_the_shortest_queue = (self.receptionists[0], self.receptionists[0].get_length_queue())
        # for rec in self.receptionists[1:]:
        #     if reception_with_the_shortest_queue[1] > rec.get_length_queue():
        #         reception_with_the_shortest_queue = (rec, rec.get_length_queue())
        # self.current_receptionist = reception_with_the_shortest_queue[0]
        # self.current_receptionist.join_queue(self.id)



    def behavior_in_the_registration_queue(self):
        while(self.current_receptionist.current_patient != self.id):
            # TODO maybe patient should compare queue legth of other receptionist
            print("Im waiting!!!")
            time.sleep(1)
        pass


    def register(self):
        # TODO Here we should add some bar increase

        self.doctors_needed = self.current_receptionist.registration(self)
        pass


    def chair_selection(self):
        # TODO selection of the chair

        self.time_to_start_waiting_for_the_surgery = datetime.now()
        self.current_receptionist.exit_registration(id)
        self.location = Location.CORRIDOR
        pass

    def waiting_for_surgery():
        # TODO waiting, can be as nervous moving of patient? xD
        pass

