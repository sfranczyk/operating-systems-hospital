from ui import UserInterface
from SurgeryRoom import SurgeryRoom
from CoffeeMachine import CoffeeMachine
from Doctor import Doctor
from Statistics import Statistics
from Receptionist import Receptionist
from Location import Location
from Patient import Patient
from Chair import Chair


def main():

    interface = UserInterface()

    r1 = Receptionist(id=1)
    r2 = Receptionist(id=2)
    ch1 = Chair(_id=1)
    ch2 = Chair(_id=2)
    statistics = Statistics()

    r_list = [r1, r2]
    ch_list = [ch1, ch2]

    p1 = Patient(id=1, hp=85, name="Patric", location=Location.RECEPTION,
                 receptionists=r_list, chairs=ch_list, statistics=statistics, interface=interface)
    p2 = Patient(id=2, hp=93, name="Danil", location=Location.RECEPTION,
                 receptionists=r_list, chairs=ch_list, statistics=statistics, interface=interface)
    p3 = Patient(id=3, hp=30, name="Bernard", location=Location.RECEPTION,
                 receptionists=r_list, chairs=ch_list, statistics=statistics, interface=interface)
    p4 = Patient(id=4, hp=41, name="Stefan", location=Location.RECEPTION,
                 receptionists=r_list, chairs=ch_list, statistics=statistics, interface=interface)
    p5 = Patient(id=5, hp=12, name="Carl", location=Location.RECEPTION,
                 receptionists=r_list, chairs=ch_list, statistics=statistics, interface=interface)
    p6 = Patient(id=6, hp=92, name="Joe", location=Location.RECEPTION,
                 receptionists=r_list, chairs=ch_list, statistics=statistics, interface=interface)
    p7 = Patient(id=7, hp=55, name="Steven", location=Location.RECEPTION,
                 receptionists=r_list, chairs=ch_list, statistics=statistics, interface=interface)

    p_list = [p1, p2, p3, p4, p5, p6, p7]

    coffee1 = CoffeeMachine()
    coffee2 = CoffeeMachine()
    surgeryRoom1 = SurgeryRoom(id='1')
    surgeryRoom2 = SurgeryRoom(id='2')

    coffee_list = [coffee1, coffee2]
    surgery_rooms = [surgeryRoom1, surgeryRoom2]

    d1 = Doctor(id=1, name="Dr Nowak", energy_points=5, chairs=ch_list,
                location=Location.CORRIDOR, coffee_machines=coffee_list, surgery_rooms=surgery_rooms, interface=interface)
    d2 = Doctor(id=2, name="Dr Kowalski", energy_points=5, chairs=ch_list,
                location=Location.CORRIDOR, coffee_machines=coffee_list, surgery_rooms=surgery_rooms, interface=interface)
    d3 = Doctor(id=3, name="Dr Wozniak", energy_points=5, chairs=ch_list,
                location=Location.CORRIDOR, coffee_machines=coffee_list, surgery_rooms=surgery_rooms, interface=interface)
    d4 = Doctor(id=4, name="Profesor Kowalczyk", energy_points=5, chairs=ch_list,
                location=Location.CORRIDOR, coffee_machines=coffee_list, surgery_rooms=surgery_rooms, interface=interface)
    d5 = Doctor(id=5, name="Dr Zelazna", energy_points=5, chairs=ch_list,
                location=Location.CORRIDOR, coffee_machines=coffee_list, surgery_rooms=surgery_rooms, interface=interface)

    doctor_list = [d1, d2, d3, d4, d5]

    interface.displayText('Pacjent', 0, 0)
    interface.displayText('Punkty zycia', 35, 0)
    interface.displayText('Lokalizacja', 50, 0)

    interface.displayText('Lekarz', 100, 0)
    interface.displayText('Punkty energii', 130, 0)
    interface.displayText('Leczony pacjent', 155, 0)
    interface.displayText('Lokalizacja', 175, 0)
    interface.displayText('Sala', 195, 0)

    for doctor in doctor_list:
        doctor.start()

    for patient in p_list:
        patient.start()

    for patient in p_list:
        patient.join()

    for doctor in doctor_list:
        doctor.join()

if __name__ == "__main__":
    main()
