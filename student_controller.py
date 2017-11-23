from student_view import StudentView
from user_database import UserDataBase
from assignment_model import Assignment
from assignment_model import AssignmentsModel
from user_controller import UserController

class StudentController(UserController):

    def __init__(self, student_container, user):
        self.student_container = student_container
        self.user = user
        self.assignment_model = AssignmentsModel(student_container)

    def start(self):

        user_controller_is_running = True
        self.notification = "Welcome {}!".format(self.user.name)
        while user_controller_is_running:

            StudentView.clear_terminal()
            StudentView.display_notification(self.notification, self.notification_visibility_time)
            self.notification = None
            user_choice = StudentView.display_student_menu()
            if user_choice == '1':
                assaignment = self.preapre_data_for_grade_table(self.assignment_model.get_student_assignments(self.user))
                StudentView.show_assignments_grades(assaignment)
                StudentView.getch()
            elif user_choice == '2':
                assignments = self.prepare_data_for_assignments_table(self.assignment_model.get_student_assignments(self.user))
                StudentView.show_assignmets(assignments)
                title = input('\nChoose assignment title:')
                assignment_data = (self.user.group, title, self.user.login)
                answer = StudentView.submit_assignment(self.assignment_model.get_assignment(*assignment_data))
                self.assignment_model.add_student_answer(self.assignment_model.get_assignment(*assignment_data), answer)
            elif user_choice == '9':
                return True
            elif user_choice == '0':
                return False

    def preapre_data_for_grade_table(self, assaignemts):
        data = []
        for assaignment in assaignemts:
            data.append([assaignment.title, assaignment.grade])
        return data

    def prepare_data_for_assignments_table(self, assignemts):
        data = []
        for assignment in assignemts:
            data.append([assignment.title, assignment.description, assignment.answer, assignment.grade])
        return data

    @staticmethod
    def submit_assignment():
        StudentView.display_work()
