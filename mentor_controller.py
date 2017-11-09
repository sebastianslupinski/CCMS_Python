from user_models import Student
from view_mentor import ViewMentor
from student_container import StudentContainer
from user_database import UserDataBase


class MentorController:

    @staticmethod
    def create_student():

        login, password, name, surname, phone_number, group = ViewMentor.input_student_info()
        return Student(login, password, name, surname, phone_number, group)

    @staticmethod
    def add_student(UserDataBase):

        new_student = MentorController.create_student()
        UserDataBase.student_container.add_student(new_student)
        UserDataBase.student_container.add_student_to_group(new_student, new_student.group)


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

    @classmethod
    def show_students_list(cls, UserDataBase):
        students = cls.get_student_list(UserDataBase)
        ViewMentor.display_all_students(students)

    @staticmethod
    def get_student_list(UserDataBase):
        students = ''
        counter = 1
        students_list = UserDataBase.student_container.get_student_list()

        for student in students_list:
            students += (str(counter) + '.' + student.__str__()) + '\n'
            counter += 1

        return students

    @classmethod
    def show_students_group(cls, UserDataBase, group):
        group_to_show = cls.get_student_group(UserDataBase, group)
        ViewMentor.display_group(group_to_show)

    @staticmethod
    def get_student_group(UserDataBase, group):

        studends_in_group = ''
        counter = 0
        group_list = UserDataBase.student_container.get_student_group(group)

        for student in group_list:
            group += (str(counter) + '.' + student.__str__()) + '\n'
            counter += 1

        return group

# u = UserDataBase()
# MentorController.show_students_list(u)
# MentorController.add_student(u)
# MentorController.show_students_group(u, 'a')
