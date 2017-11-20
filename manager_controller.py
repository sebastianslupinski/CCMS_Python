from user_models import Mentor
from manager_view import ViewManager
from view_mentor import ViewMentor
from user_controller import UserController


class ManagerController:

    def __init__(self, mentor_container, student_container):
        self.mentor_container = mentor_container
        self.student_container = student_container

    def start(self):
        while True:
            ViewMentor.clear_terminal()
            user_choice = ViewManager.display_manager_menu()
            if user_choice == '1':
                self.add_mentor()
            elif user_choice == '2':
                self.edit_mentor()
            elif user_choice == '3':
                self.delete_mentor()
            elif user_choice == '4':
                UserController.show_mentor_list(self.mentor_container.get_mentor_list())
            elif user_choice == '5':
                UserController.show_students_list(self.student_container.get_student_list())
            elif user_choice == '9':
                return False
            elif user_choice == '0':
                return True

    def delete_mentor(self):
        UserController.show_mentor_list(self.mentor_container.get_mentor_list())
        user = self.mentor_container.pick_mentor_by_login(ViewManager.get_user_input('Input login of mentor: '))
        if not user:
            ViewManager.custom_print('Wrong login name')
        else:
            self.mentor_container.remove_mentor(user)

    def create_mentor(self):
        login, password, name, surname, phone_number = ViewManager.input_mentor_info()
        return Mentor(login, password, name, surname, phone_number)

    def add_mentor(self):
        new_mentor = self.create_mentor()
        self.mentor_container.add_mentor(new_mentor)

    def chose_edit_options(self, edit_option, user):
        if edit_option == '1':
            user.change_attribute_value('name', ViewManager.get_user_input('Input new name: ').capitalize())
        elif edit_option == '2':
            user.change_attribute_value('surname', ViewManager.get_user_input('Input new surname: ').capitalize())
        elif edit_option == '3':
            user.change_attribute_value('password', ViewManager.get_user_input('Input new password: '))
        elif edit_option == '4':
            user.change_attribute_value('phone_number', ViewManager.get_user_phone_number())

    def edit_mentor(self):
        UserController.show_mentor_list(self.mentor_container.get_mentor_list())
        user = self.mentor_container.pick_mentor_by_login(ViewManager.get_user_input('Input login of mentor: '))
        if not user:
            ViewManager.custom_print('Wrong login name')
        else:
            edit_option = ViewManager.display_edit_option()
            self.chose_edit_options(edit_option, user)
