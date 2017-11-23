import student_container
from user_database import UserDataBase
from view import View

import string

class AttendanceView(View):

    @classmethod
    def choose_group(cls, classes):
        cls.clear_terminal()
        cls.display_groups(classes)
        group_choice = cls.get_user_input('\n')
        return group_choice

    @classmethod
    def display_groups(cls, classes):
        print("Available classes are: ")
        for group in classes:
            print("class name: ", group)

    @classmethod
    def display_student_to_check(cls, student_data):
        student_not_checked = True
        while student_not_checked:
            View.clear_terminal()
            for student in student_data:
                check = cls.get_user_input("Is {} present? y/n".format(student)).lower()
                if check in ('y', 'n'):
                    return check


