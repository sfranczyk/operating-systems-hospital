from threading import Lock

class CoffeeMachine:
    
    _energy_points = 10
    
    def __init__(self, id):
        self.lock = Lock()
        self.id = id
        self.doctor_id = None
        self.doctor_name = None

    def try_take(self, id, name):
        if(self.lock.acquire(False)):
            self.doctor_id = id
            self.doctor_name = name
            return True
        return False


    def drink_coffee(self):
        return CoffeeMachine._energy_points

    def release(self):
        self.doctor_id = None
        self.doctor_name = None
        self.lock.release()