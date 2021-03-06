from ui import UserInterface
from SurgeryRoom import SurgeryRoom
from CoffeeMachine import CoffeeMachine
from Doctor import Doctor
from Statistics import Statistics
from Receptionist import Receptionist
from Location import Location
from patient import Patient
from Chair import Chair
from patient_finished import Patient_Finished
import threading

def killer_run(p_list,doctor_list,patient_manager,interface):
    killer = 's'
    while not killer in ['Q', 'q']:
        killer  = interface.win.getkey()
    for patient in p_list:
        patient.kill = True

    for doctor in doctor_list:
        doctor.kill = True

    patient_manager.kill = True
    interface.kill = True

def main():

    r1 = Receptionist(id=1)
    r2 = Receptionist(id=2)
    ch1 = Chair(_id=1)
    ch2 = Chair(_id=2)
    statistics = Statistics()

    r_list = [r1, r2]
    ch_list = [ch1, ch2]

    p1 = Patient(id=1, hp=85, name="Patric",
                 receptionists=r_list, chairs=ch_list, statistics=statistics)
    p2 = Patient(id=2, hp=93, name="Danil",
                 receptionists=r_list, chairs=ch_list, statistics=statistics)
    p3 = Patient(id=3, hp=30, name="Bernard",
                 receptionists=r_list, chairs=ch_list, statistics=statistics)
    p4 = Patient(id=4, hp=41, name="Stefan", 
                 receptionists=r_list, chairs=ch_list, statistics=statistics)
    p5 = Patient(id=5, hp=12, name="Carl",
                 receptionists=r_list, chairs=ch_list, statistics=statistics)
    p6 = Patient(id=6, hp=92, name="Joe",
                 receptionists=r_list, chairs=ch_list, statistics=statistics)
    p7 = Patient(id=7, hp=55, name="Anna",
                 receptionists=r_list, chairs=ch_list, statistics=statistics)

    p_list = [p1, p2, p3, p4, p5, p6, p7]

    coffee1 = CoffeeMachine(id=1)
    coffee2 = CoffeeMachine(id=2)
    surgeryRoom1 = SurgeryRoom(id=1)
    surgeryRoom2 = SurgeryRoom(id=2)

    coffee_list = [coffee1, coffee2]
    surgery_rooms = [surgeryRoom1, surgeryRoom2]

    d1 = Doctor(id=1, name="Dr Nowacka", energy_points=35, chairs=ch_list,
                location=Location.CORRIDOR, coffee_machines=coffee_list, surgery_rooms=surgery_rooms)
    d2 = Doctor(id=2, name="Dr Kowalski", energy_points=15, chairs=ch_list,
                location=Location.CORRIDOR, coffee_machines=coffee_list, surgery_rooms=surgery_rooms)
    d3 = Doctor(id=3, name="Dr Wozniak", energy_points=5, chairs=ch_list,
                location=Location.CORRIDOR, coffee_machines=coffee_list, surgery_rooms=surgery_rooms)
    d4 = Doctor(id=4, name="Profesor Kowalczyk", energy_points=45, chairs=ch_list,
                location=Location.CORRIDOR, coffee_machines=coffee_list, surgery_rooms=surgery_rooms)
    d5 = Doctor(id=5, name="Dr Wojtasik", energy_points=65, chairs=ch_list,
                location=Location.CORRIDOR, coffee_machines=coffee_list, surgery_rooms=surgery_rooms)

    doctor_list = [d1, d2, d3, d4, d5]

    interface = UserInterface(chairs=ch_list, coffee_machines=coffee_list, doctors=doctor_list,
                              patients=p_list, receptionists=r_list, surgery_rooms=surgery_rooms)

    patient_manager = Patient_Finished(
        patients=p_list, receptionists=r_list, chairs=ch_list, statistics=statistics)

    for doctor in doctor_list:
        doctor.start()

    for patient in p_list:
        patient.start()

    patient_manager.start()
    interface.start()

    killer = threading.Thread(target=killer_run, args=(p_list,doctor_list,patient_manager,interface))
    killer.start()
    killer.join()

    
    for doctor in doctor_list:
        doctor.join()

    for patient in p_list:
        patient.join()

    patient_manager.join()
    interface.join()


if __name__ == "__main__":
    main()
