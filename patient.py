import threading
import time

class Patient(threading.Thread):

    def __init__(self, id, hp, name, location, receptionists, chairs):
        self.id = id
        self.hp = hp
        self.name = name
        self.location = location
        self.receptionist = receptionists
        self.chairs = chairs

        self.doctors_needed = 0
        self.current_doctors_number = 0

        threading.Thread.__init__(self)

    # Thread method
    # 1) Patient should first choose queue to receptionist
    # 2) Patient should register himself
    def run(self):
        time.sleep(1)
        self.queue_selection()
        self.register()
        self.chair_selection()
        self.waiting_for_surgery()


    def queue_selection():
        # TODO
        pass

    def register():
        # TODO
        pass

    def chair_selection():
        # TODO
        pass

    def waiting_for_surgery():
        # TODO
        pass

