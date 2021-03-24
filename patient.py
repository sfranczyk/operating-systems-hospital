import threading
import time



class patient(threading.Thread):
    def __init__(self, health_points):
        max_health_points = 100
        self._health_points = health_points
        
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(1)

