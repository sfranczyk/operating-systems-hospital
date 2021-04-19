import threading
import time
from datetime import datetime
from threading import Lock

class doctor(threading.Thread):
    max_energy_points = 100   

    def __init__(self, energy_points, chairs, location):
        self.energy_points = energy_points
        self.chairs = chairs
        self.choosen_patient = None
        self.location = location

        threading.Thread.__init__(self)

    def run(self):
        time.sleep(1)

    def take_break(self):
        pass

