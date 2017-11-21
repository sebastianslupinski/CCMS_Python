import student_container
from user_database import UserDataBase
from view import View


class ViewMentor(View):

    @classmethod
    def display_mentor_menu(cls):
        mentor_commands = ('Add new student', 'Show all students', 'Remove student', 'Show group', 'Edit student')
        cls.display_menu(mentor_commands)
        return cls.getch()

    @classmethod
    def input_student_info(cls):

        password = View.valid_data("Please enter password: ")
        name = View.valid_data("Please enter student's name: ")
        surname = View.valid_data("Please enter student's surname: ")
        phone_number = cls.get_user_phone_number()

        while True:

            group = input("Please enter a group 'a' or 'b': ")

            if group.lower() == 'a' or group.lower() == 'b':
                break
            else:
                print("There is no group like this")
                continue

        return password, name, surname, phone_number, group

    @classmethod
    def select_edit_option(cls):
        edit_commands = ('Change name', 'Change surname', 'Change password', 'Change phone number')
        cls.display_menu(edit_commands)
        return cls.getch()

    @classmethod
    def choose_group(cls):
        while True:
            cls.clear_terminal()
            print("Choose group to show (a or b)")
            group_choice = ViewMentor.getch()
            if group_choice in ("a", "b"):
                return group_choice
