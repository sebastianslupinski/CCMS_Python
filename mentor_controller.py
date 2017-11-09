from user_models import Student
from view_mentor import ViewMentor
from student_container import StudentContainer
from user_database import UserDataBase


class MentorController:

    def __init__(self, student_container):
        self.student_container = student_container

    @staticmethod
    def create_student():

        login, password, name, surname, phone_number = ViewMentor.input_student_info()
        return Student(login, password, name, surname, phone_number)

    @staticmethod
    def add_student(UserDataBase):

        new_student = MentorController.create_student()
        UserDataBase.student_container.add_student(new_student)

    @staticmethod
    def edit_student(UserDataBase):
        user = UserDataBase.pick_user_by_login(ViewMentor.get_user_input('Input login of student: '))
        if not user:
            ViewMentor.custom_print('Wrong login name')
        else:
            edit_option = ViewMentor.select_edit_option()
            if edit_option == '1':
                user.change_attribute_value('name', ViewMentor.get_user_input('Input new name: '))
            elif edit_option == '2':
                user.change_attribute_value('surname', ViewMentor.get_user_input('Input new surname: '))
            elif edit_option == '3':
                user.change_attribute_value('password', ViewMentor.get_user_input('Input new password: '))
            elif edit_option == '4':
                user.change_attribute_value('phone_number', ViewMentor.get_user_input('Input new phone number: '))

    def show_students_list(self, UserDataBase):
        students = self.get_student_list(UserDataBase)
        ViewMentor.display_all_students(students)

    def get_student_list(self, UserDataBase):
        students = ''
        counter = 1
        students_list = UserDataBase.student_container.get_student_list()

        for student in students_list:
            students += (str(counter) + '.' + student.__str__()) + '\n'
            counter += 1

        return students

