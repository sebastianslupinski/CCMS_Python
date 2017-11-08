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
    def show_students_list(UserDataBase):
        ViewMentor.display_all_students(UserDataBase)


u = UserDataBase()
MentorController.add_student(u)
MentorController.display_all_students(u)