from user_models import Mentor
from manager_view import ViewManager
from mentor_container import MentorContainer
from user_database import UserDataBase


class ManagerController:


    @classmethod
    def manager_menu(cls):
        ViewManager.display_manager_menu()
        user_choice = ViewManager.get_user_input()

        while True:
            if user_choice == '1':
                cls.add_mentor(UserDataBase)
            elif user_choice == '2':
                cls.edit_mentor(UserDataBase)
            elif user_choice == '3':
                MentorContainer.remove_mentor() #do rozwinięcia
            elif user_choice == '4':
                '''show mentor list'''
                pass
            elif user_choice == '5':
                '''show student list'''
                pass
            elif user_choice == '6':
                break



    @staticmethod
    def create_mentor():
        login, password, name, surname, phone_number = ViewManager.input_mentor_info()

        return Mentor(login, password, name, surname, phone_number)

    @staticmethod
    def add_mentor(database):
        new_mentor = ManagerController.create_mentor()
        database.mentor_container.add_mentor(new_mentor)

    @staticmethod
    def edit_mentor(database):
        user = database.pick_user_by_login(ViewManager.get_user_input('Input login of mentor: '))
        edit_option = ViewManager.select_edit_option()
        while True:
            if edit_option == '1':
                user.change_attribute_value('name', ViewManager.get_user_input('Input new name: ').capitalize())
            elif edit_option == '2':
                user.change_attribute_value('surname', ViewManager.get_user_input('Input new surname: ').capitalize())
            elif edit_option == '3':
                user.change_attribute_value('password', ViewManager.get_user_input('Input new password: '))
            elif edit_option == '4':
                try:
                    user.change_attribute_value('phone_number', int(ViewManager.get_user_input('Input new phone number: ')))
                    if len(ViewManager.get_user_input) > 9:
                        print('Phone number too long!')
                    continue
                except ValueError:
                    print('Enter numbers only!')
                    continue
            elif edit_option == '5':
                break

