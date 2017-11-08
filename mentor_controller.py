from user_models import Student
from view_mentor import ViewMentor
from student_container import StudentContainer

class MentorController:

    @staticmethod
    def create_student():

        login, password, name, surname, phone_number = ViewMentor.input_student_info()
        return Student(login, password, name, surname, phone_number)
    @staticmethod
    def add_student

container = StudentContainer()
MentorController.add_student()
print(container.student_list)