from student_view import StudentView


class StudentController:

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
    def submit_assignment():
        StudentView.display_work()

    @staticmethod
    def view_grades():
        StudentView.display_work()
