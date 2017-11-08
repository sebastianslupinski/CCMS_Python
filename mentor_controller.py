from user_models import Student
from view_mentor import ViewMentor
from student_container import StudentContainer
from user_database import UserDataBase


class MentorController:

    @staticmethod
    def create_student():

        login, password, name, surname, phone_number = ViewMentor.input_student_info()
        return Student(login, password, name, surname, phone_number)

    @staticmethod
    def add_student(UserDataBase):

        new_student = MentorController.create_student()
        UserDataBase.student_container.add_student(new_student)

    @staticmethod
<<<<<<< HEAD
    def edit_student(UserDataBase):
        user = UserDataBase.pick_user_by_login(ViewMentor.get_user_input('Input login of student: '))
        edit_option = ViewMentor.select_edit_option()
        if edit_option == '1':
            user.change_attribute_value('name', ViewMentor.get_user_input('Input new name: '))
        elif edit_option == '2':
            user.change_attribute_value('surname', ViewMentor.get_user_input('Input new surname: '))
        elif edit_option == '3':
            user.change_attribute_value('password', ViewMentor.get_user_input('Input new password: '))
        elif edit_option == '4':
            user.change_attribute_value('phone_number', ViewMentor.get_user_input('Input new phone number: '))

u = UserDataBase()
print(MentorController.edit_student(u))
=======
    def show_students_list(UserDataBase):
        ViewMentor.display_all_students(UserDataBase)


u = UserDataBase()
MentorController.add_student(u)
MentorController.display_all_students(u)
>>>>>>> 65f48165346d54a65ecef61c34c688e3259948f0
