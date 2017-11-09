from user_models import Mentor
from manager_view import ViewManager
from mentor_container import MentorContainer
from user_database import UserDataBase


class ManagerController:

    @staticmethod
    def create_mentor():

        login, password, name, surname, phone_number = ViewManager.input_mentor_info()
        return Mentor(login, password, name, surname, phone_number)

    @staticmethod
    def add_mentor(UserDataBase):

        new_mentor = ManagerController.create_mentor()
        UserDataBase.mentor_container.add_mentor(new_mentor)

    @staticmethod
    def edit_mentor(UserDataBase):
        user = UserDataBase.pick_user_by_login(ViewManager.get_user_input('Input login of mentor: '))
        edit_option = ViewManager.select_edit_option()
        while True:
            if edit_option == '1':
                user.change_attribute_value('name', ViewManager.get_user_input('Input new name: '))
            elif edit_option == '2':
                user.change_attribute_value('surname', ViewManager.get_user_input('Input new surname: '))
            elif edit_option == '3':
                user.change_attribute_value('password', ViewManager.get_user_input('Input new password: '))
            elif edit_option == '4':
                user.change_attribute_value('phone_number', ViewManager.get_user_input('Input new phone number: '))
            elif edit_option == '5':
                break

