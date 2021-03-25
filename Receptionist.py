from threading import Lock
class Receptionist:
    def __init__(self, id):
        self.id = id
        self.current_patient = ""

        self.lock = Lock()
        self.patients_list = []


    def get_length_queue(self):
        return len(self.patients_list)


    def join_queue(self, id):
        self.lock.acquire()
        try:
            if not self.current_patient:
                self.current_patient = id  
            else:
                self.patients_list.append(id)
        finally:
            self.lock.release()

        print(f"I am receptinist {self.id}, patient {id}, and I have patient {self.current_patient}")
        for p in self.patients_list:
            print(p)
        
        print("asa", id, " ", self.current_patient)


    def exit_queue(self, id):
        self.lock.acquire()
        try:
            self.patients_list.remove(id)
        except ValueError:
            pass
        finally:
            self.lock.release()


    # registration return number of needed doctors
    def registration(self, patient):
        # TODO method of calculating the number of doctors
        return 1


    def exit_registration(self, id):
        self.lock.acquire()
        try:
            if (id == self.current_patient):
                if not self.patients_list:
                    self.current_patient = ""  
                else:
                    self.current_patient = self.patients_list.pop(0)
            else:
                try:
                    self.patients_list.remove(id)
                except ValueError:
                    pass
        finally:
            self.lock.release()
