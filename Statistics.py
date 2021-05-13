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
        return Statistics.patients_healed / Statistics.patients_total * 100.0

    def percentage_of_dead(self):
        return Statistics.patients_dead / Statistics.patients_total * 100.0

    def print_actual_statistics(self):
        dead_percentage = self.percentage_of_dead()
        healed_percentage = self.percentage_of_healed()

        print(f'Do szpitala przybylo {self.patients_total} pacjentow, umarlo {dead_percentage}% z nich, zostalo uleczonych {healed_percentage}% z nich, w trakcie leczenia pozostaje {self.patients_during_treatment} pacjentow')
