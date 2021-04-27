from threading import Lock

class CoffeeMachine:
    
    _energy_points = 1
    
    def __init__(self):
        self.lock = Lock()
        self.doctor_id = None

    def try_take(self, id):
        if(self.lock.acquire(False)):
            self.doctor_id = id
            return True
        return False


    def drink_coffee():
        return CoffeeMachine._energy_points

    def release(self):
        self.doctor_id = None
        self.lock.release()