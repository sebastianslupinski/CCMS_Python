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
                group = ViewMentor.choose_group(self.prepare_classes())
                if group in self.prepare_classes():
                    group_list = self.student_container.get_student_group(group)
                    self.show_user_list(group_list)
                    ViewMentor.getch()
            elif user_choice == '5':
                self.edit_student()
            elif user_choice == '6':
                self.assignment_model.create_assignment(
                    ViewMentor.get_user_input("For which class do you want to create an assignment:\n"),
                    ViewMentor.get_user_input("Type assignment title:\n"),
                    ViewMentor.get_user_input("Type assignment description:\n"))
            elif user_choice == '7':
                # self.assignment_model.get_assignments_by_group(ViewMentor.choose_group(self.student_container.groups))
                ViewMentor.custom_print(self.assignment_model.get_assignments_by_group(ViewMentor.choose_group(self.student_container.groups)))
                ViewMentor.getch()
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
            self.notification = "Student removed"

    def create_student(self):
        login = self.create_new_login()
        password, name, surname, phone_number = ViewMentor.input_student_info()
        group = ViewMentor.choose_group_to_add_student(self.prepare_classes())
        return Student(login, password, name, surname, phone_number, group)

    def add_student(self):
        new_student = self.create_student()
        self.student_container.add_student(new_student)
        self.student_container.add_student_to_group(new_student, new_student.group)

    def chose_edit_options(self, edit_option, user):
        ViewMentor.clear_terminal()
        if edit_option == '1':
            user.change_attribute_value('name', ViewMentor.valid_data('Input new name: '))
            ViewMentor.display_notification("Name changed", self.notification_visibility_time)
        elif edit_option == '2':
            user.change_attribute_value('surname', ViewMentor.valid_data('Input new surname: '))
            ViewMentor.display_notification("Surname changed", self.notification_visibility_time)
        elif edit_option == '3':
            user.change_attribute_value('password', ViewMentor.valid_data('Input new password: '))
            ViewMentor.display_notification("Password changed", self.notification_visibility_time)
        elif edit_option == '4':
            user.change_attribute_value('phone_number', ViewMentor.get_user_phone_number())
            ViewMentor.display_notification("Phone number changed", self.notification_visibility_time)
        elif edit_option == '5':
            new_group = ViewMentor.choose_group_to_add_student(self.prepare_classes())
            user.change_student_group(new_group)
        
    def edit_student(self):
        student_list = self.student_container.get_student_list()
        self.show_user_list(student_list)
        user = self.student_container.pick_student_by_login(ViewMentor.get_user_input('Input login of student: '))
        if not user:
            ViewMentor.custom_print('Wrong login name')
            ViewMentor.getch()
        else:
            ViewMentor.clear_terminal()
            edit_option = ViewMentor.select_edit_option()
            self.chose_edit_options(edit_option, user)
            self.student_container.save_edited_data()
        

    def prepare_classes(self):
        classes = sorted(list(self.student_container.list_of_classes.keys()))
        return classes
