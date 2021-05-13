from SurgeryRoom import SurgeryRoom
from CoffeeMachine import CoffeeMachine
from Doctor import Doctor
from Statistics import Statistics
from Receptionist import Receptionist
from Location import Location
from Patient import Patient
from Chair import Chair


def main():

    r1 = Receptionist(1)
    r2 = Receptionist(id=2)
    ch1 = Chair(_id=1)
    ch2 = Chair(_id=2)
    statistics = Statistics()

    r_list = [r1, r2]
    ch_list = [ch1, ch2]

    p1 = Patient(id="aaa", hp=3, name="Patric", location=Location.RECEPTION,
                 receptionists=r_list, chairs=ch_list, statistics=statistics)
    # p2 = Patient(id="bbb", hp=90, name="Danil", location=Location.RECEPTION,
    #              receptionists=r_list, chairs=ch_list, statistics=statistics)
    # p3 = Patient(id="ccc", hp=30, name="Bernard", location=Location.RECEPTION,
    #              receptionists=r_list, chairs=ch_list, statistics=statistics)
    # p4 = Patient(id="ddd", hp=41, name="Stefan", location=Location.RECEPTION,
    #              receptionists=r_list, chairs=ch_list, statistics=statistics)
    # p5 = Patient(id="eee", hp=12, name="Carl", location=Location.RECEPTION,
    #              receptionists=r_list, chairs=ch_list, statistics=statistics)
    # p6 = Patient(id="fff", hp=92, name="Joe", location=Location.RECEPTION,
    #              receptionists=r_list, chairs=ch_list, statistics=statistics)
    # p7 = Patient(id="ggg", hp=55, name="Steven", location=Location.RECEPTION,
    #              receptionists=r_list, chairs=ch_list, statistics=statistics)

    p_list = [p1]

    coffee1 = CoffeeMachine()
    coffee2 = CoffeeMachine()
    surgeryRoom1 = SurgeryRoom()
    surgeryRoom2 = SurgeryRoom()

    coffee_list = [coffee1, coffee2]
    surgery_rooms = [surgeryRoom1, surgeryRoom2]

    d1 = Doctor(id="doctor_1", name="Dr Nowak", energy_points=40, chairs=ch_list,
                location=Location.CORRIDOR, coffee_machines=coffee_list, surgery_rooms=surgery_rooms)
    d2 = Doctor(id="doctor_2", name="Dr Kowalski", energy_points=80, chairs=ch_list,
                location=Location.CORRIDOR, coffee_machines=coffee_list, surgery_rooms=surgery_rooms)
    d3 = Doctor(id="doctor_3", name="Dr Wozniak", energy_points=55, chairs=ch_list,
                location=Location.CORRIDOR, coffee_machines=coffee_list, surgery_rooms=surgery_rooms)
    d4 = Doctor(id="doctor_4", name="Profesor Kowalczyk", energy_points=30, chairs=ch_list,
                location=Location.CORRIDOR, coffee_machines=coffee_list, surgery_rooms=surgery_rooms)
    d5 = Doctor(id="doctor_5", name="Dr Zelazna", energy_points=95, chairs=ch_list,
                location=Location.CORRIDOR, coffee_machines=coffee_list, surgery_rooms=surgery_rooms)

    doctor_list = [d1, d2, d3, d4, d5]

    # for doctor in doctor_list:
    #     doctor.start()

    for patient in p_list:
        patient.start()

    for patient in p_list:
        patient.join()

    # for doctor in doctor_list:
    #     doctor.join()


if __name__ == "__main__":
    main()
