class Statistics:

    def __init__(self):        
        self.patients_total = 0
        self.patients_healed = 0
        self.patients_dead = 0
        self.patients_during_treatment = 0

    def new_patient(self):
        self.patients_total += 1
        self.patients_during_treatment += 1

    def patient_healed(self):
        self.patients_during_treatment -= 1
        self.patients_healed += 1

    def patient_died(self):
        self.patients_during_treatment -= 1
        self.patients_dead += 1

    def percentage_of_healed(self):
        if self.patients_total == 0:
            return 0        
        return self.patients_healed / self.patients_total * 100.0

    def percentage_of_dead(self):
        if self.patients_total == 0:
            return 0        
        return self.patients_dead / self.patients_total * 100.0

   