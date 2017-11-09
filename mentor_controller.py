from user_models import Student
from view_mentor import ViewMentor
from user_database import UserDataBase


class MentorController:

    def __init__(self, student_container):
        self.student_container = student_container

    def start(self):
        while True:
            user_choice = ViewMentor.display_mentor_menu()
            if user_choice == '1':
                self.add_student()
            elif user_choice == '2':
                self.show_students_list()
            elif user_choice == '3':
                self.delete_student()
            elif user_choice == '4':
                self.show_students_group(ViewMentor.choose_group())
            elif user_choice == '5':
                self.edit_student()
            elif user_choice == '6':
                break

    def delete_student(self):
        self.show_students_list()
        user = self.student_container.pick_student_by_login(ViewMentor.get_user_input('Input login of mentor: '))
        if not user:
            ViewMentor.custom_print('Wrong login name')
        else:
            self.student_container.remove_student(user)

    def create_student(self):
        login, password, name, surname, phone_number, group = ViewMentor.input_student_info()
        return Student(login, password, name, surname, phone_number, group)

    def add_student(self):
        new_student = self.create_student()
        self.student_container.add_student(new_student)
        self.student_container.add_student_to_group(new_student, new_student.group)

    def chose_edit_options(self, edit_option, user):
        if edit_option == '1':
            user.change_attribute_value('name', ViewMentor.get_user_input('Input new name: '))
        elif edit_option == '2':
            user.change_attribute_value('surname', ViewMentor.get_user_input('Input new surname: '))
        elif edit_option == '3':
            user.change_attribute_value('password', ViewMentor.get_user_input('Input new password: '))
        elif edit_option == '4':
            user.change_attribute_value('phone_number', ViewMentor.get_user_phone_number())

    def edit_student(self):
        user = self.student_container.pick_student_by_login(ViewMentor.get_user_input('Input login of student: '))
        if not user:
            ViewMentor.custom_print('Wrong login name')
        else:
            edit_option = ViewMentor.select_edit_option()
            self.chose_edit_options(edit_option, user)

    def show_students_list(self):
        students = self.prepare_student_list()
        ViewMentor.display_all_students(students)

    def prepare_student_list(self):
        students_list = self.student_container.get_student_list()
        return self.convert_list(students_list)

    def show_students_group(self, group):
        group_to_show = self.get_student_group(group)
        ViewMentor.display_group(group_to_show)

    def get_student_group(self, group):
        group_list = self.student_container.get_student_group(group)
        return self.convert_list(group_list)

    def convert_list(self, list):
        users = ''
        counter = 1
        for user in list:
            users += (str(counter) + '.' + user.__str__()) + '\n'
            counter += 1
        return users
