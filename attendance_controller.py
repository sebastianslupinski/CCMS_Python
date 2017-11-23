from user_controller import UserController
from attendance_model import AttendanceModel
from attendance_view import AttendanceView


class AttendanceController(UserController):

    def __init__(self, student_container):
        self.student_container = student_container
        self.attendance_model = AttendanceModel(student_container)

    def check_attendance(self):
        choose_group = AttendanceView.choose_group(self.student_container.list_of_classes)
        group_attendance = self.attendance_model.get_group_attendance(choose_group)
        student_attendance = AttendanceView.display_student_to_check(self.attendance_model.get_student_data(group_attendance))
        self.attendance_model.check_attendance(group_attendance, student_attendance)