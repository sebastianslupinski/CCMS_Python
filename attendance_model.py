import csv


class Attendance:

    def __init__(self, login, all_days, present_days, group):

        self.login = login
        self.present_days = int(all_days)
        self.all_days = int(present_days)
        self.group = group


    def set_presence(self):
        self.present_days += 1
        self.all_days += 1

    def set_absence(self):
        self.all_days += 1

    def get_presence_average(self):
        average = round(self.present_days/self.all_days, 2)
        return average


class AttendanceModel:

    def __init__(self, student_container):

        self.student_container = student_container
        self.attendance_container = []

    def save_attendances_to_file(self, file_name="attendance.csv", mode="w"):

        with open(file_name, mode) as file:
            for attendance in self.attendance_container:
                file.write(attendance.login + "|" +
                           str(attendance.present_days) + '|' +
                           str(attendance.all_days) + '|' +
                           attendance.group + "\n")


    def read_attendaces_from_file(self, file_name="attendance.csv"):
        attendance_table = list(csv.reader(open(file_name, 'r'), delimiter='|'))
        attendance_objects = []
        for item in attendance_table:
            attendance_objects.append(Attendance(*item))
        self.attendance_container = attendance_objects
        return attendance_objects

    def get_group_attendance(self, group):
        group_attendance = []
        for attendance in self.read_attendaces_from_file():
            if group == attendance.group:
                group_attendance.append(attendance)
        return group_attendance

    def get_group_data(self, group_attendance):
        student_data = []
        for attendance in group_attendance:
            login = attendance.login
            student = self.student_container.pick_student_by_login(login)
            student_data.append((student.name, student.surname))
            return student_data

    def get_student_data(self, student):
        login = student.login
        user = self.student_container.pick_student_by_login(login)
        return user.name, user.surname

    def check_attendance(self, group_attendance, check):
        for attendance in group_attendance:
            if check == 'y':
                attendance.set_presence()
            else:
                attendance.set_absence()
            self.save_attendances_to_file()
