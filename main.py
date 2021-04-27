from Receptionist import Receptionist
from Location import Location
from Patient import Patient
from Chair import Chair

def main():
    print("Helicopter")
    r1 = Receptionist(1)
    r2 = Receptionist(id=2)
    r_list = [r1, r2]
    ch1 = Chair(_id=1)
    ch2 = Chair(_id=2)
    ch_list = [ch1, ch2]

    p1 = Patient(id = "aaa", hp=10, name="Patric", location = Location.RECEPTION, receptionists= r_list, chairs=ch_list)
    p2 = Patient(id = "bbb", hp=100, name="Danil", location = Location.RECEPTION, receptionists= r_list, chairs=ch_list)
    p3 = Patient(id = "ccc", hp=30, name="Bernard", location = Location.RECEPTION, receptionists= r_list, chairs=ch_list)
    p4 = Patient(id = "ddd", hp=41, name="Stefan", location = Location.RECEPTION, receptionists= r_list, chairs=ch_list)
    p5 = Patient(id = "eee", hp=12, name="Carl", location = Location.RECEPTION, receptionists= r_list, chairs=ch_list)
    p6 = Patient(id = "fff", hp=92, name="Joe", location = Location.RECEPTION, receptionists= r_list, chairs=ch_list)
    p7 = Patient(id = "ggg", hp=55, name="Steven", location = Location.RECEPTION, receptionists= r_list, chairs=ch_list)
    
    p_list = [p1, p2, p3, p4, p5, p6, p7]
    for p in p_list:
        p.start()

    for p in p_list:
        p.join()











if __name__ == "__main__":
    main()