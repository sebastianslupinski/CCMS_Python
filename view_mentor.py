
import student_container
from user_database import UserDataBase


class ViewMentor:

    @classmethod
    def display_mentor_menu(cls):
        mentor_commands = ('Add new student', 'Show all students', 'Show group', 'Edit student', 'Go back')
        cls.display_menu(mentor_commands)
        return cls.get_user_input('Choose: ')

    @staticmethod
    def display_menu(options):
        for option in options:
            print(str(options.index(option) + 1) + "----->" + option)

    @staticmethod
    def input_student_info():

        login = input("Please enter student's login: ")
        password = input("Please enter password: ")
        name = input("Please enter student's name: ")
        surname = input("Please enter student's surname: ")
        phone_number = input("Please enter student's phone number: ")
        
        while True:

            group = input("Please enter a group 'a' or 'b': ")

            if group.lower() == 'a' or group.lower() == 'b':
                break
            else:
                print("There is no group like this")
                continue

        return login, password, name, surname, phone_number, group

    @staticmethod
    def get_user_input(message):
        return input(message)

    @classmethod
    def select_edit_option(cls):
        edit_commands = ('Change name', 'Change surname', 'Change password', 'Change phone number')
        for option in edit_commands:
            print(str(edit_commands.index(option) + 1) + "----->" + option)
        choosen_option = cls.get_user_input('Choose: ')
        return choosen_option

    @classmethod
    def choose_group(cls):
        while True:
            group_choice = input("Choose group to show (a or b)")
            if group_choice in ("a", "b"):
                return group_choice

    def display_all_students(students):

        print(students)

    def display_group(group):

        print(group)

    @staticmethod
    def custom_print(message):
        print(message)
