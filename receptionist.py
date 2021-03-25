from threading import Lock, current_thread
class Receptionist:
    def __init__(self, id):
        self.id = id
        self.queue_length = 0
        self.current_patient = ""

        self.lock = Lock()
        patients_list = []

    def get_length_queue(self):
        return self.queue_length

    def join_queue(self, id):
        self.lock.acquire()
        self.queue_length += 1
        if not self.patients_list:
            self.current_patient = id
        else:
            self.patients_list.append(id)
        self.lock.release()

    def exit_registration(self, id):
        self.lock.acquire()
        self.current_patient = "" if not self.patients_list else self.current_patient = self.patients_list.pop(0)
        self.lock.release()