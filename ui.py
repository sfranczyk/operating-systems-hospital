import curses
import threading


class UserInterface(threading.Thread):

    def __init__(self, patients, doctors, chairs, surgery_rooms, coffee_machines, receptionists):
        super(UserInterface, self).__init__()
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.start_color()

        self.begin_x = 0
        self.begin_y = 0
        self.height = 200
        self.width = 200

        self.patients = patients
        self.doctors = doctors
        self.chairs = chairs
        self.surgery_rooms = surgery_rooms
        self.coffee_machines = coffee_machines
        self.receptionists = receptionists

        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)

        self.win = curses.newwin(
            self.height, self.width, self.begin_y, self.begin_x)

        self.kill = False

    def run(self):
        self.displayHeaders()

        while not self.kill:
            for patient in self.patients:
                self.patientInfo(patient)
                self.statisticsInfo(patient)
            for doctor in self.doctors:
                self.doctorInfo(doctor)
            for chair in self.chairs:
                self.chairInfo(chair)
            for surgery_room in self.surgery_rooms:
                self.surgeryRoomInfo(surgery_room)
            for coffee_machine in self.coffee_machines:
                self.coffeMachineInfo(coffee_machine)
            for receptionist in self.receptionists:
                self.receptionistInfo(receptionist)

        self.terminate()

    def patientInfo(self, patient):
        self.displayText(patient.name, 0, int(patient.id), length=35)
        self.displayText(str(patient.health_points), 35, int(patient.id), length=15, color=3)
        self.displayText(str(patient.phase.name), 50, int(patient.id), length=50)
        if patient.phase.name == 'QUEUE':
            self.displayText(str(patient.current_receptionist.id), 60, int(patient.id), length=15)
        self.displayText(str(patient.doctors_needed), 75, int(patient.id), length=20)

    def doctorInfo(self, doctor):
        self.displayText(doctor.name, 100, doctor.id, length=30)
        self.displayText(str(doctor.energy_points), 130, doctor.id, length=25, color=2)
        if not doctor.choosen_patient == None:
            self.displayText(doctor.choosen_patient.name, 155, doctor.id, length=20)
        else:
            self.displayText("Free", 155, doctor.id, length=20)
        self.displayText(str(doctor.location.name), 175, doctor.id, length=20)
        if not doctor.surgery_room == None:
            self.displayText(str(doctor.surgery_room.id), 195, doctor.id, length=5)

    def chairInfo(self, chair):       
        self.displayText("Chair number: " + str(chair.id) + " is: ", 0, 10 + chair.id)

        if chair.sitting_patient == None:
            self.displayText("free", 20, 10 + chair.id)
        else:
            self.displayText("taken by: " + chair.sitting_patient.name, 20, 10 + chair.id, color=3)

    def surgeryRoomInfo(self, surgery_room):
        self.displayText("Surgery room number: " + str(surgery_room.id) + " is: ", 0, 14 + surgery_room.id)

        if surgery_room.is_used:
            self.displayText(" occupied by: " + surgery_room.patient.name, 25, 14 + surgery_room.id, color=3)
        else:
            self.displayText(" free", 25, 14 + surgery_room.id)

    def coffeMachineInfo(self, coffee_machine):
        self.displayText("Coffee machine number: " + str(coffee_machine.id) + " is ", 0, 17 + coffee_machine.id)

        if coffee_machine.doctor_id == None:
            self.displayText(" free", 28, 17 + coffee_machine.id)
        else:
            self.displayText(" taken by: " + str(coffee_machine.doctor_name), 28, 17 + coffee_machine.id, color=3)

    def receptionistInfo(self, receptionist):
        self.displayText("Receptionist number: " + str(receptionist.id) + " is ", 0, 20 + receptionist.id)

        if receptionist.current_patient == None or receptionist.current_patient_name == None:
            self.displayText(" free", 25, 20 + receptionist.id)
        else:
            self.displayText(" taken by: " + receptionist.current_patient_name, 25, 20 + receptionist.id, color=3)

    def statisticsInfo(self, patient):
        if patient != None and patient.statistics != None:
            self.displayText("All patients: ", 0, 24)
            self.displayText(str(patient.statistics.patients_total), 19, 24, color=3)
            self.displayText("Healed patients: ", 0, 25)
            self.displayText(str(patient.statistics.patients_healed), 19, 25, color=3)
            self.displayText("Dead patients: ", 0, 26)
            self.displayText(str(patient.statistics.patients_dead), 19, 26, color=3)

    def terminate(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def clearTerminal(self):
        self.win.clear()

    def displayText(self, text, x, y, length=30, color=1):
        spaces = " " * length

        self.win.addstr(y, x, spaces)
        self.win.addstr(y, x, text, curses.color_pair(color))
        self.win.refresh()

    def displayHeaders(self):
        self.displayText('Patient name', 0, 0, color=4)
        self.displayText('Health points', 35, 0, color=4)
        self.displayText('Location', 50, 0, color=4)
        self.displayText('Needed doctors', 75, 0, color=4)
        self.displayText('Doctor', 100, 0, color=4)
        self.displayText('Energy points', 130, 0, color=4)
        self.displayText('Current patient', 155, 0, color=4)
        self.displayText('Location', 175, 0, color=4)
        self.displayText('Surgery Room', 195, 0, color=4)
