import csv


class Attendance:

    def __init__(self, login):

        self.login = login
        self.present_days = 0
        self.days = 0

    def set_presence(self):
        self.present_days += 1
        self.days += 1

    def set_absence(self):
        self.days += 1

    def get_presence_average(self):
        average = round(self.present_days/self.days, 2)
        return average


class AttendanceContainer:

    def __init__(self, student_container):

        self.student_container = student_container
        self.attendance_container = []

    def prepare_attendance(self):
        pass

    def save_attendances_to_file(self, file_name="attendance.csv", mode="w"):

        with open(file_name) as file:
            for attendance in self.attendance_container:
                file.write(attendance.login + "|" +
                           str(attendance.present_days) + '|' +
                           str(attendance.days) + "\n")

    def read_attendaces_from_file(self, file_name="attendance.csv"):
        attendance_table = list(csv.reader(open(file_name, 'r'), delimiter=','))
        attendance_obejcts = []
        for item in attendance_table:
            attendance_obejcts.append(Attendance(*item))
        self.attendance_container = attendance_obejcts
        return attendance_obejcts