import threading
import time

class doctor(threading.Thread):
    def __init__(self, energy_points):
        max_energy_points = 100
        self._energy_points = energy_points
        
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(1)