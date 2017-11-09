from user_models import Mentor
from manager_view import ViewManager
from view_mentor import ViewMentor
from mentor_container import MentorContainer
from user_database import UserDataBase


class ManagerController:

    def __init__(self, mentor_container, student_container):
        self.mentor_container = mentor_container
        self.student_container = student_container


    def start(self):
        ViewManager.display_manager_menu()
        user_choice = ViewManager.get_user_input('Choose option:')

        while True:
            if user_choice == '1':
                self.add_mentor(self.mentor_container)
            elif user_choice == '2':
                self.edit_mentor(self.mentor_container)
            elif user_choice == '3':
                self.mentor_container.remove_mentor() #do rozwinięcia
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
    def validate_phone_number(user):
        user.change_attribute_value('phone_number', int(ViewManager.get_user_input('Input new phone number: ')))
        if len(ViewManager.get_user_input) > 9:
            print('Phone number too long!')

    @staticmethod
    def edit_mentor(database):
        user = database.pick_mentor_by_login(ViewManager.get_user_input('Input login of mentor: '))
        if not user:
            ViewManager.custom_print('Wrong login name')
        else:
            edit_option = ViewManager.select_edit_option()
            if edit_option == '1':
                user.change_attribute_value('name', ViewManager.get_user_input('Input new name: ').capitalize())
            elif edit_option == '2':
                user.change_attribute_value('surname', ViewManager.get_user_input('Input new surname: ').capitalize())
            elif edit_option == '3':
                user.change_attribute_value('password', ViewManager.get_user_input('Input new password: '))
            elif edit_option == '4':
                try:
                    ManagerController.validate_phone_number(user)
                except ValueError:
                    print('Enter numbers only!')
            elif edit_option == '5':
                pass

    def show_students_list(self, student_container):
        students = self.get_student_list(student_container)
        ViewMentor.display_all_students(students)

    def get_student_list(self, student_container):
        students = ''
        counter = 1
        students_list = student_container.get_student_list()

        for student in students_list:
            students += (str(counter) + '.' + student.__str__()) + '\n'
            counter += 1

        return students

    def show_mentor_list(self, mentor_container):
        mentors = self.get_mentor_list(mentor_container)
        ViewManager.display_all_mentors(mentors)

    def get_mentor_list(self, mentor_container):
        mentors = ''
        counter = 1
        mentor_list = mentor_container.get_mentor_list()

        for mentor in mentor_list:
            mentors += (str(counter) + '.' + mentor.__str__()) + '\n'
            counter += 1

        return mentors

u = UserDataBase()
manager = ManagerController(u.mentor_container, u.student_container)
manager.show_mentor_list(u.mentor_container)
manager.edit_mentor(u.mentor_container)
manager.show_mentor_list(u.mentor_container)