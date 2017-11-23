from user_models import Student
from mentor_view import ViewMentor
from user_controller import UserController
from assignment_model import Assignment
from assignment_model import AssignmentsModel
from attendance_controller import AttendanceController
from attendance_model import AttendanceModel
from attendance_model import Attendance


class MentorController(UserController):

    def __init__(self, student_container, user):
        self.student_container = student_container
        self.user = user
        self.assignment_model = AssignmentsModel(student_container)
        self.attendance_controller = AttendanceController(student_container)
        self.attendance_model = AttendanceModel(student_container)

    def start(self):

        user_controller_is_running = True
        self.notification = "Welcome {}!".format(self.user.name)
        while user_controller_is_running:

            ViewMentor.clear_terminal()
            ViewMentor.display_notification(self.notification, self.notification_visibility_time)
            self.notification = None
            user_choice = ViewMentor.display_mentor_menu()
            if user_choice == '1':
                self.add_student()
            elif user_choice == '2':
                student_list = self.student_container.get_student_list()
                self.show_student_list(student_list)
                ViewMentor.getch()
            elif user_choice == '3':
                self.delete_student()
            elif user_choice == '4':
                self.show_group()
            elif user_choice == '5':
                self.edit_student()
            elif user_choice == '6':
                self.create_assignment()
            elif user_choice == '7':
                self.grade_assignment()
            elif user_choice == '8':
                self.attendance_controller.check_attendance()
            elif user_choice == '9':
                return True
            elif user_choice == '0':
                return False

    def delete_student(self):
        student_list = self.student_container.get_student_list()
        self.show_user_list(student_list)
        user = self.student_container.pick_student_by_login(ViewMentor.get_user_input('Input login of student: '))
        if not user:
            ViewMentor.display_notification('Wrong login name')
        else:
            self.student_container.remove_student(user)
            self.notification = "Student removed!"

    def create_student(self):
        login = self.create_new_login()
        password, name, surname, phone_number = ViewMentor.input_student_info()
        group = ViewMentor.choose_group_to_add_student(self.prepare_classes())
        attendance = Attendance(login, 0, 0, group)
        self.attendance_controller.add_new_attendance(attendance)
        self.notification = "Student added!"
        return Student(login, password, name, surname, phone_number, group)

    def add_student(self):
        new_student = self.create_student()
        self.student_container.add_student(new_student)
        self.student_container.add_student_to_group(new_student, new_student.group)

        if new_student.group not in self.user.guided_groups:
            self.user.guided_groups.append(new_student.group)

    def manage_edit_options(self, edit_option, user):
        ViewMentor.clear_terminal()
        if edit_option == '1':
            user.change_attribute_value('name', ViewMentor.valid_data('Input new name: '))
            self.notification = "Name changed"
        elif edit_option == '2':
            user.change_attribute_value('surname', ViewMentor.valid_data('Input new surname: '))
            self.notification = "Surname changed"
        elif edit_option == '3':
            user.change_attribute_value('password', ViewMentor.valid_data('Input new password: '))
            self.notification = "Password changed"
        elif edit_option == '4':
            user.change_attribute_value('phone_number', ViewMentor.get_user_phone_number())
            self.notification = "Phone number changed"
        elif edit_option == '5':
            self.change_student_group(user)
            self.notification = "Group changed"

    def edit_student(self):
        student_list = self.student_container.get_student_list()
        if student_list:
            self.check_if_login_is_correct(student_list)
        else:
            self.notification = "No students here"

    def choose_edit_option(self, user, edit_option):
        edit_option_selected = False
        while not edit_option_selected:
            ViewMentor.display_notification(self.notification, self.notification_visibility_time)
            self.notification = None
            ViewMentor.clear_terminal()
            edit_option[0] = ViewMentor.select_edit_option()
            if edit_option[0] in ("1", "2", "3", "4", "5"):
                self.manage_edit_options(edit_option[0], user)
                self.student_container.save_edited_data()
            elif edit_option[0] == "0":
                break

    def check_if_login_is_correct(self, student_list):
        login_is_correct = False
        edit_option = [None]
        while not login_is_correct:
            if edit_option[0] == "0":
                break
            ViewMentor.clear_terminal()
            ViewMentor.display_notification(self.notification, self.notification_visibility_time)
            self.show_user_list(student_list)
            user = self.student_container.pick_student_by_login(ViewMentor.get_user_input('Input login of student: '))
            if not user:
                ViewMentor.display_notification('Wrong login name')
            else:
                self.choose_edit_option(user, edit_option)

    def prepare_classes(self):
        classes = sorted(list(self.user.guided_groups))
        return classes

    def show_group(self):
        group = ViewMentor.choose_group(self.prepare_classes())
        if group in self.prepare_classes():
            group_list = self.student_container.get_student_group(group)
            self.show_user_list(group_list)
            ViewMentor.getch()
        else:
            self.notification = "No such group"

    def create_assignment(self):
        ViewMentor.clear_terminal()
        group = ViewMentor.choose_group(self.prepare_classes())
        if group in self.prepare_classes():
            ViewMentor.clear_terminal()
            self.assignment_model.create_assignment(
                group, ViewMentor.get_user_input("Type assignment title:\n"),
                ViewMentor.get_user_input("Type assignment description:\n"))
            self.notification = "Assignmnent created!"
        else:
            self.notification = "No such group"

    def grade_assignment(self):
        group = ViewMentor.choose_group(self.prepare_classes())
        title = ViewMentor.choose_title(self.assignment_model.get_assignments_by_group(group))
        if title:
            login = ViewMentor.choose_login(self.assignment_model.get_assignments_by_title(group, title))
            grade = ViewMentor.show_assignment_for_grade(self.assignment_model.get_assignment(group, title, login))
            self.assignment_model.grade_assignment(self.assignment_model.get_assignment(group, title, login), grade)
            self.notification = "Assignment graded!"
        else:
            self.notification = 'No assignments here'

    def change_student_group(self, user):
        new_group = ViewMentor.choose_group_to_add_student(self.prepare_classes())
        self.student_container.remove_student_from_group(user)
        user.change_student_group(new_group)
        self.student_container.add_student_to_group(user, new_group)

    def prepare_student_table(self, users):
        data = []
        for user in users:
            average_grade = self.assignment_model.get_grade_average(user)
            if average_grade:
                data.append((str(user) + " " + str(average_grade)))
            else:
                data.append((str(user) + ' X'))
        return data

    def show_student_list(self, student_list):
        ViewMentor.clear_terminal()
        users = self.prepare_student_table(student_list)
        ViewMentor.display_student_table(users)
