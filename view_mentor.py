
import student_container
from user_database import UserDataBase

class ViewMentor:

    @staticmethod
    def display_menu():
        print("")

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

    def display_all_students(students):

        print(students)

    def display_group(group):

        print(group)

    @staticmethod
    def custom_print(message):
        print(message)