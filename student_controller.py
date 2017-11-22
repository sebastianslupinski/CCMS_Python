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
                StudentView.show_assignments(self.assignment_model.get_student_assignments(self.user))
                StudentView.getch()
            elif user_choice == '2':
                StudentView.show_assignments(self.assignment_model.get_student_assignments(self.user))
                title = input('\nChoose assignment title:')
                assignment_data = (self.user.group, title, self.user.login)
                answer = StudentView.submit_assignment(self.assignment_model.get_assignment(*assignment_data))
                self.assignment_model.add_student_answer(self.assignment_model.get_assignment(*assignment_data), answer)
            elif user_choice == '9':
                return True
            elif user_choice == '0':
                return False




    @staticmethod
    def submit_assignment():
        StudentView.display_work()

