from user_models import Mentor
from manager_view import ViewManager
from user_controller import UserController


class ManagerController(UserController):

    def __init__(self, mentor_container, employee_container, student_container, user):
        self.user = user
        self.mentor_container = mentor_container
        self.student_container = student_container
        self.employee_container = employee_container

    def start(self):

        user_controller_is_running = True
        self.notification = "Welcome {}!".format(self.user.name)
        while user_controller_is_running:

            ViewManager.clear_terminal()
            ViewManager.display_notification(self.notification, self.notification_visibility_time)
            self.notification = None
            user_choice = ViewManager.display_manager_menu()
            if user_choice == '1':
                self.add_mentor()
            elif user_choice == '2':
                self.edit_mentor()
            elif user_choice == '3':
                self.delete_mentor()
            elif user_choice == '4':
                mentor_list = self.mentor_container.get_mentor_list()
                self.show_mentor_list(mentor_list)
                ViewManager.getch()
            elif user_choice == '5':
                employee_list = self.employee_container.get_employee_list()
                self.show_employee_list(employee_list)
                ViewManager.getch()
            elif user_choice == '6':
                student_list = self.student_container.get_student_list()
                self.show_user_list(student_list)
                ViewManager.getch() 
            elif user_choice == '9':
                return True
            elif user_choice == '0':
                return False

    def delete_mentor(self):
        mentor_list = self.mentor_container.get_mentor_list()
        self.show_user_list(mentor_list)
        user = self.mentor_container.pick_mentor_by_login(ViewManager.get_user_input('Input login of mentor to delete: '))
        if not user:
            ViewManager.custom_print('Wrong login name')
        else:
            self.mentor_container.remove_mentor(user)
            self.notification = "Mentor deleted"

    def create_guided_groups(self):

        choosing_group = True

        while choosing_group:
            ViewManager.display_groups(self.student_container.list_of_classes.keys())
            groups = ViewManager.input_guided_groups()

            for group in groups:
                if group not in self.student_container.list_of_classes.keys() or len(group) < 1:
                    print("There is no group or groups like this")
                    choosing_group = True
                else:
                    choosing_group = False

        return groups

    def create_mentor(self):
        login = self.create_new_login()
        password, name, surname, phone_number = ViewManager.input_mentor_info()
        guided_groups = self.create_guided_groups()
        self.notification = "Mentor added!"
        return Mentor(login, password, name, surname, phone_number, guided_groups)

    def add_mentor(self):
        new_mentor = self.create_mentor()
        self.mentor_container.add_mentor(new_mentor)

    def chose_edit_options(self, edit_option, user):
        ViewManager.clear_terminal()
        if edit_option == '1':
            user.change_attribute_value('name', ViewManager.get_user_input('Input new name: ').capitalize())
            self.notification = "Name changed"
        elif edit_option == '2':
            user.change_attribute_value('surname', ViewManager.get_user_input('Input new surname: ').capitalize())
            self.notification = "Surname changed"
        elif edit_option == '3':
            user.change_attribute_value('password', ViewManager.get_user_input('Input new password: '))
            self.notification = "Password changed"
        elif edit_option == '4':
            user.change_attribute_value('phone_number', ViewManager.get_user_phone_number())
            self.notification = "Phone number changed"

    def edit_mentor(self):
        mentor_list = self.mentor_container.get_mentor_list()
        if mentor_list:
            self.show_user_list(mentor_list)
            user = self.mentor_container.pick_mentor_by_login(ViewManager.get_user_input('Input login of mentor: '))
            if not user:
                ViewManager.display_notification('Wrong login name')
            else:
                edit_option_selected = False
                while not edit_option_selected:
                    ViewManager.display_notification(self.notification, self.notification_visibility_time)
                    self.notification = None
                    edit_option = ViewManager.display_edit_option()
                    if edit_option == "0":
                        break
                    self.chose_edit_options(edit_option, user)
                    self.mentor_container.save_edited_data()
                    
        else:
            self.notification = "No mentors here"

    def show_mentor_list(self, mentor_list):
        ViewManager.clear_terminal()
        users = self.prepare_user_table(mentor_list)
        ViewManager.display_mentor_table(users)

    def show_employee_list(self, employee_list):
        ViewManager.clear_terminal()
        users = self.prepare_user_table(employee_list)
        ViewManager.display_employee_table(users)
