import threading
from threading import Lock

class medical_room(threading.Thread):
    machine_lock = Lock()
   
    def __init__(self, coffee_machines):
        self.coffee_machines = coffee_machines
        self.search = True

    def take_coffee_machine(self, doctor):
        while self.search:
            for machine in self.coffee_machines:
                if machine.is_free:
                    try:
                        self.search = False
                        self.machine_lock.acquire()
                        machine.is_free = False
                        machine.doctor = doctor
                    finally:
                        self.machine_lock.release()
