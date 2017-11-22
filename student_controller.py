from student_view import StudentView
from user_database import UserDataBase
from assignment_model import Assignment
from assignment_model import AssignmentsModel


class StudentController:

    def __init__(self, student_container, user):
        self.student_container = student_container
        self.user = user
        self.assignment_model = AssignmentsModel(student_container)

    def start(self):

        user_controller_is_running = True

        while user_controller_is_running:

            user_choice = StudentView.display_student_menu()
            if user_choice == '1':
                self.view_grades()
            elif user_choice == '2':
                self.submit_assignment()
            elif user_choice == '9':
                return True
            elif user_choice == '0':
                return False

    @staticmethod
    def view_grades():
        StudentView.display_work()

    @staticmethod
    def submit_assignment():
        StudentView.display_work()

