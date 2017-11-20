from employee_view import EmployeeView
from user_controller import UserController


class EmployeeController:

    def __init__(self, student_container):
        self.student_container = student_container

    def start(self):
        while True:
            user_choice = EmployeeView.display_employee_menu()
            if user_choice == '1':
                student_list = self.student_container.get_student_list()
                UserController.show_user_list(student_list)
            elif user_choice == '2':
                break
