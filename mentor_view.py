import student_container
from user_database import UserDataBase
from view import View


class ViewMentor(View):

    @classmethod
    def display_mentor_menu(cls):
        mentor_commands = (
            'Add new student', 'Show all students', 'Remove student', 'Show group',
            'Edit student', 'Create new assignment', 'Grade assignment', 'Check attendance')
        cls.display_menu(mentor_commands)
        return cls.getch()

    @classmethod
    def input_student_info(cls):

        password = View.valid_data("Please enter password: ")
        name = View.valid_data("Please enter student's name: ")
        surname = View.valid_data("Please enter student's surname: ")
        phone_number = cls.get_user_phone_number()
        return password, name, surname, phone_number

    @classmethod
    def select_edit_option(cls):
        options = ('Change name', 'Change surname', 'Change password', 'Change phone number', 'Change student group')
        for option in options:
            print(str(options.index(option) + 1) + "----->" + option)
        print("\n0----->Back\n")
        return cls.getch()

    @classmethod
    def choose_group(cls, classes):

        cls.clear_terminal()
        cls.display_groups(classes)
        group_choice = ViewMentor.get_user_input('')
        return group_choice

    @classmethod
    def choose_group_to_add_student(cls, classes):

        cls.clear_terminal()
        cls.display_groups(classes)
        print("If you want to add new group, just type it's name: ")
        group_choice = ViewMentor.getch()
        return group_choice

    @classmethod
    def display_groups(cls, classes):

        print("Available classes are: ")
        for group in classes:

            print("class name: ", group)