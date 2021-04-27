class Statistics:

    patients_total = 0
    patients_healed = 0
    patients_dead = 0
    patients_during_treatment = 0

    def new_patient(self):
        Statistics.patients_total += 1
        Statistics.patients_during_treatment += 1

    def patient_healed(self):
        Statistics.patients_during_treatment -= 1
        Statistics.patients_healed += 1

    def patient_died(self):
        Statistics.patients_during_treatment -= 1
        Statistics.patients_dead += 1

    def percentage_of_healed(self):
        return Statistics.patient_healed / Statistics.patients_total

    def percentage_of_dead(self):
        return Statistics.patient_died / Statistics.patients_total