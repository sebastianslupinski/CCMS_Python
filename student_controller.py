from student_view import StudentView
from user_database import UserDataBase
from assignment_model import Assignment
from assignment_model import AssignmentsModel
from attendance_model import AttendanceModel
from user_controller import UserController


class StudentController(UserController):

    def __init__(self, student_container, user):
        self.student_container = student_container
        self.user = user
        self.assignment_model = AssignmentsModel(student_container)
        self.attendance_model = AttendanceModel(student_container)


    def start(self):

        user_controller_is_running = True
        self.notification = "Welcome {}!".format(self.user.name)
        while user_controller_is_running:

            StudentView.clear_terminal()
            StudentView.display_notification(self.notification, self.notification_visibility_time)
            self.notification = None
            user_choice = StudentView.display_student_menu()
            if user_choice == '1':
                self.display_grades()
            elif user_choice == '2':
                self.submit_assignment()
            elif user_choice == '3':
                self.show_attendance()
            elif user_choice == '9':
                return True
            elif user_choice == '0':
                return False

    def display_grades(self):
        assignment = self.preapre_data_for_grade_table(self.assignment_model.get_student_assignments(self.user))
        StudentView.show_assignments_grades(assignment)
        StudentView.getch()

    def get_attendance(self):
        for attendance in self.attendance_model.read_attendaces_from_file():
            if self.user.login == attendance.login:
                return attendance

    def preapre_data_for_grade_table(self, assaignemts):
        data = []
        for assignment in assaignemts:
            data.append([assignment.title, assignment.grade])
        return data

    def prepare_data_for_assignments_table(self, assignemts):
        data = []
        for assignment in assignemts:
            data.append([assignment.title, assignment.description, assignment.answer, assignment.grade])
        return data

    def submit_assignment(self):
        assignments = self.prepare_data_for_assignments_table(self.assignment_model.get_student_assignments(self.user))
        StudentView.show_assignmets(assignments)
        title = input('\nChoose assignment title: \n')
        assignment_data = (self.user.group, title, self.user.login)
        assignment = self.assignment_model.get_assignment(*assignment_data)
        if assignment:
            answer = StudentView.submit_assignment(assignment)
            self.assignment_model.add_student_answer(assignment, answer)
        else:
            self.notification = "Incorrect assignment title"

    def show_attendance(self):
        average = self.get_attendance()
        StudentView.show_attendance(average)