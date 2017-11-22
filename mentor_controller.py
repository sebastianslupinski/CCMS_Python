from user_models import Student
from mentor_view import ViewMentor
from user_controller import UserController
from assignment_model import Assignment
from assignment_model import AssignmentsModel


class MentorController(UserController):

    def __init__(self, student_container):
        self.student_container = student_container
        self.assignment_model = AssignmentsModel(student_container)

    def start(self):

        user_controller_is_running = True

        while user_controller_is_running:

            ViewMentor.clear_terminal()
            ViewMentor.display_notification(self.notification, self.notification_visibility_time)
            self.notification = None
            user_choice = ViewMentor.display_mentor_menu()
            if user_choice == '1':
                self.add_student()
            elif user_choice == '2':
                student_list = self.student_container.get_student_list()
                self.show_user_list(student_list)
                ViewMentor.getch()
            elif user_choice == '3':
                self.delete_student()
            elif user_choice == '4':
                group_list = self.student_container.get_student_group(ViewMentor.choose_group(self.student_container.groups))
                self.show_user_list(group_list)
                ViewMentor.getch()
            elif user_choice == '5':
                self.edit_student()
            elif user_choice == '6':
                ViewMentor.clear_terminal()
                self.assignment_model.create_assignment(
                    ViewMentor.choose_group(self.student_container.groups),
                    ViewMentor.get_user_input("Type assignment title:\n"),
                    ViewMentor.get_user_input("Type assignment description:\n"))
                self.notification = "Assignmnent created!"
            elif user_choice == '7':
                group = ViewMentor.choose_group(self.student_container.groups)
                title = ViewMentor.choose_title(self.assignment_model.get_assignments_by_group(group))
                login = ViewMentor.choose_login(self.assignment_model.get_assignments_by_title(group, title))
                grade = ViewMentor.show_assignment_for_grade(self.assignment_model.get_assignment(group, title, login))
                self.assignment_model.grade_assignment(self.assignment_model.get_assignment(group, title, login), grade)
                self.notification = "Assignment graded!"
            elif user_choice == '8':
                self.check_attendance()                        
            elif user_choice == '9':
                return True
            elif user_choice == '0':
                return False

    def delete_student(self):
        student_list = self.student_container.get_student_list()
        self.show_user_list(student_list)
        user = self.student_container.pick_student_by_login(ViewMentor.get_user_input('Input login of student: '))
        if not user:
            ViewMentor.display_notification('Wrong login name')
        else:
            self.student_container.remove_student(user)
            self.notification = "Student removed!"

    def create_student(self):
        login = self.create_new_login()
        password, name, surname, phone_number, group = ViewMentor.input_student_info()
        self.notification = "Student added!"
        return Student(login, password, name, surname, phone_number, group)

    def add_student(self):
        new_student = self.create_student()
        self.student_container.add_student(new_student)
        self.student_container.add_student_to_group(new_student, new_student.group)

    def chose_edit_options(self, edit_option, user):
        ViewMentor.clear_terminal()
        if edit_option == '1':
            user.change_attribute_value('name', ViewMentor.get_user_input('Input new name: '))
            ViewMentor.display_notification("Name changed", self.notification_visibility_time)
        elif edit_option == '2':
            user.change_attribute_value('surname', ViewMentor.get_user_input('Input new surname: '))
            ViewMentor.display_notification("Surname changed", self.notification_visibility_time)
        elif edit_option == '3':
            user.change_attribute_value('password', ViewMentor.get_user_input('Input new password: '))
            ViewMentor.display_notification("Password changed", self.notification_visibility_time)
        elif edit_option == '4':
            user.change_attribute_value('phone_number', ViewMentor.get_user_phone_number())
            ViewMentor.display_notification("Phone number changed", self.notification_visibility_time)

    def edit_student(self):
        student_list = self.student_container.get_student_list()
        self.show_user_list(student_list)
        user = self.student_container.pick_student_by_login(ViewMentor.get_user_input('Input login of student: '))
        if not user:
            ViewMentor.custom_print('Wrong login name')
            ViewMentor.getch()
        else:
            edit_option = None
            while edit_option != "0":
                ViewMentor.clear_terminal()
                edit_option = ViewMentor.select_edit_option()
                self.chose_edit_options(edit_option, user)
