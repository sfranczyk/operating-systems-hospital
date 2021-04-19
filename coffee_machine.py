import threading
from Location import Location

class coffee_machine(threading.Thread):
    
    def __init__(self, is_free, doctor):
        self.is_free = is_free
        self.doctor = doctor

        threading.Thread.__init__(self)

    def run(self):
        if not self.is_free and self.doctor:
            while self.doctor.energy_points < self.doctor.max_energy_points:
                self.doctor.energy_points += 1

            self.is_free = True
            self.doctor = None
            

    