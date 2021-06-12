from Location import Location
import threading
from Phase import Phase
import random
from patient import Patient
from Location import Location


class Patient_Finished(threading.Thread):

    def __init__(self, patients, receptionists, chairs, statistics):
        super(Patient_Finished, self).__init__()

        self.patients = patients
        self.receptionists = receptionists
        self.chairs = chairs
        self.statistisc = statistics
        self.kill = False

    def get_name(self):

        names = ['Steve', 'Cornel', 'Alex', 'Yanna',
                 'Max', 'Stefanie', 'Oleg', 'Olga', 'Wojtek', 'Karolina', 'Kornelia', 'Michal', 'Bogdan', 'Dominika', 'Michalina']

        return names[random.randint(0, len(names) - 1)]

    def create_new_patient(self, id):

        health_points = random.randint(5, 99)
        patient_name = self.get_name()

        patient = Patient(
            id=id,
            hp=health_points,
            name=patient_name,
            receptionists=self.receptionists,
            chairs=self.chairs,
            statistics=self.statistisc
        )

        self.patients.append(patient)

        return patient

    def run(self):
        while not self.kill:

            for patient in self.patients:
                if patient.phase in [Phase.DEAD, Phase.HEALED]:

                    if patient.current_receptionist.get_position_in_queue(patient.id) == 0:
                        patient.current_receptionist.exit_registration(
                            patient.id)

                    if patient.current_chair:
                        patient.current_chair.release_chair()
                        patient.current_chair = None

                    id_for_new_patient = patient.id
                    self.patients.remove(patient)
                    new_patient = self.create_new_patient(id_for_new_patient)

                    new_patient.start()
