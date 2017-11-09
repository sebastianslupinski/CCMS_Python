from employee_view import EmployeeView


class EmployeeController:

    def __init__(self, student_container):
        self.student_container = student_container

    def start(self):
        while True:
            user_choice = EmployeeView.display_employee_menu()
            if user_choice == '1':
                self.show_students_list()
            elif user_choice == '2':
                break

    def show_students_list(self):

        students = self.prepare_student_list()
        EmployeeView.display_all_students(students)

    def prepare_student_list(self):

        students = ''
        counter = 1
        students_list = self.student_container.get_student_list()

        for student in students_list:
            students += (str(counter) + '.' + student.__str__()) + '\n'
            counter += 1

        return students
