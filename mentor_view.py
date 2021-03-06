import student_container
from user_database import UserDataBase
from view import View
from prettytable import PrettyTable
import string


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
        group_choice = ViewMentor.get_user_input('\n')
        return group_choice

    @classmethod
    def choose_group_to_add_student(cls, classes):

        cls.clear_terminal()
        cls.display_groups(classes)
        print("If you want to add new group, just type it's name: ")
        group_choice = input("")
        return group_choice

    @classmethod
    def display_groups(cls, classes):

        print("Groups you guide are: ")
        for group in classes:
            print("class name: ", group)

    @staticmethod
    def choose_title(assignment_by_group):
        if assignment_by_group:
            titles = set()
            for assignment in assignment_by_group:
                titles.add(assignment.title)

            title_not_choosen = True
            while title_not_choosen:
                ViewMentor.clear_terminal()
                for title in titles:
                    print(title)
                choose = input("\nChoose title:\n")
                if choose in titles:
                    return choose

    @staticmethod
    def choose_login(assignment_by_title):
        login_not_choosen = True
        while login_not_choosen:
            ViewMentor.clear_terminal()
            logins = []
            for assignment in assignment_by_title:
                logins.append(assignment.login)
                print(assignment.login)
            choose = input("\nChoose login:\n")
            if choose in logins:
                return choose

    @staticmethod
    def show_assignment_for_grade(assignment):
        assignment_not_graded = True
        while assignment_not_graded:
            View.clear_terminal()
            print(assignment)
            grade = input("\nGrade assignment:\n")
            if grade in ("1", "2", "3", "4", "5"):
                return grade
    @staticmethod
    def display_student_table(users):
        table = PrettyTable(['Login', 'Name', 'Surname', 'Email', 'Phone_number', 'Grade', 'Attendance'])
        for user in users:
            user = user.split(" ")
            user_login = user[0]
            user_name = user[1]
            user_surname = user[2]
            user_email = user[3]
            user_phone_number = user[4]
            user_grade = user[5]
            user_attendance = user[6]
            table.add_row([user_login, user_name, user_surname, user_email, user_phone_number, user_grade, user_attendance])
        table.align = 'l'
        print(table)

    @staticmethod
    def show_attendance(attendance):
        View.clear_terminal()
        print('Your attendance is {}%'.format(attendance.get_presence_average() * 100))
        View.getch()