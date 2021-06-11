from threading import Lock
import random

class Receptionist:

    def __init__(self, id):
        self.id = id
        self.current_patient = None
        self.current_patient_name = None

        self.lock = Lock()
        self.patients_list = []


    def get_position_in_queue(self, id):
        try:
            return self.patients_list.index(id)
        except IndexError:            
            return -1
        except ValueError:
            return -1


    def get_length_queue(self):
        return len(self.patients_list)


    def join_queue(self, id):
        self.lock.acquire()
        try:
            if not self.current_patient:
                self.current_patient = id                
            self.patients_list.append(id)
        finally:
            self.lock.release()


    def exit_queue(self, id):
        self.lock.acquire()
        try:
            self.patients_list.remove(id)
        except ValueError:
            pass
        finally:
            self.lock.release()


    def registration(self, patient_hp):
       number_of_needed_doctors = int(1 + 1 / patient_hp * 30 + random.uniform(0, 1))
       
       return number_of_needed_doctors if number_of_needed_doctors < 5 else 5


    def exit_registration(self, id):
        self.lock.acquire()
        try:

            self.current_patient = None
            self.current_patient_name = None
            self.patients_list.remove(id)

            if len(self.patients_list) > 0:
                self.current_patient = self.patients_list[0]

            # if (id == self.current_patient):
            #     if not self.patients_list:
            #         self.current_patient = None  
            #     else:
            #         self.patients_list.pop(0)
            #         if len(self.patients_list) > 0:
            #             self.current_patient = self.patients_list[0]
            # else:
            #     try:
            #         self.patients_list.remove(id)
            #     except ValueError:
            #         pass
        finally:
            self.lock.release()
