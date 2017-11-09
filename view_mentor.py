import student_container
from user_database import UserDataBase
from root_controller_view import RootControllerView


class ViewMentor(RootControllerView):

    @classmethod
    def display_mentor_menu(cls):
        mentor_commands = ('Add new student', 'Show all students', 'Remove student', 'Show group', 'Edit student')
        cls.display_menu(mentor_commands)
        return cls.getch()

    @classmethod
    def get_user_phone_number(cls):
        while True:
            phone_number = cls.get_user_input('Please enter mentors phone number: ')
            if len(phone_number) == 9:
                try:
                    return int(phone_number)
                except ValueError:
                    print('Not a number input!')
            else:
                print('Invalid or too short input!')

    @staticmethod
    def display_menu(options):
        for option in options:
            print(str(options.index(option) + 1) + "----->" + option)
        print("\n9----->Log out\n0----->Quit")

    @classmethod
    def input_student_info(cls):

        login = input("Please enter student's login: ")
        password = input("Please enter password: ")
        name = input("Please enter student's name: ")
        surname = input("Please enter student's surname: ")
        phone_number = cls.get_user_phone_number()
        
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
        cls.display_menu(edit_commands)
        return cls.get_user_input('Choose: ')

    @classmethod
    def choose_group(cls):
        while True:
            cls.clear_terminal()
            print("Choose group to show (a or b)")
            group_choice = ViewMentor.getch()
            if group_choice in ("a", "b"):
                return group_choice

    @staticmethod
    def display_all_students(students):
        print(students)

    @staticmethod
    def display_group(group):
        print(group)

    @staticmethod
    def custom_print(message):
        print(message)
