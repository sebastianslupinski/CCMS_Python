from employee_view import EmployeeView
from user_controller import UserController


class EmployeeController(UserController):

    def __init__(self, student_container, user):
        self.student_container = student_container
        self.user = user

    def start(self):

        user_controller_is_running = True
        self.notification = "Welcome {}!".format(self.user.name)
        while user_controller_is_running:

            EmployeeView.clear_terminal()
            EmployeeView.display_notification(self.notification, self.notification_visibility_time)
            self.notification = None
            user_choice = EmployeeView.display_employee_menu()
            if user_choice == '1':
                student_list = self.student_container.get_student_list()
                self.show_user_list(student_list)
                EmployeeView.getch()
            elif user_choice == '2':
                self.notification = "{}, you look pretty!".format(self.user.name)
            elif user_choice == '9':
                return True
            elif user_choice == '0':
                return False
