import csv
import pickle
from student_container import StudentContainer


class Assignment:

    def __init__(self, title, login, description, answer, grade):
        self.title = title
        self.login = login
        self.description = description
        self.answer = ""
        self.grade = 0


class AssignmentsModel:

    def __init__(self, student_container):
        self.student_container = student_container

    def read_from_file(self, file_name):
        assignments = []
        while True:
            with open(file_name, "rb") as file:
                try:
                    assignments.append(pickle.load(file))
                except EOFError:
                    break
        return assignments

    def create_assignment(self, group, title, description):
        group_assignment = []
        logins = self.get_group_logins(group)
        for login in logins:
            group_assignment.append(Assignment(title, login, description, "", None))
        assignment_list = self.read_from_file('assignment_data.csv')
        if not assignment_list:
            assignment_list = []
        assignment_list.extend(group_assignment)
        self.save_to_file(assignment_list)

    def save_to_file(self, assignments):
        with open('assignment_data.csv', 'wb') as file:
            for assignment in assignments:
                pickle.dump(assignment, file)

    def get_group_logins(self, group):
        logins = []
        for student in self.student_container.get_student_group(group):
            logins.append(student.login)
        return logins

    def get_assignments_by_login(self, login):
        personal_asssignments = []
        for assignment in self.get_assignment_list():
            if login == assignment.login:
                personal_asssignments.append(assignment)
        return personal_asssignments

    def get_assignments_by_title(self, title, login):
        assignments_with_title = []
        for assignment in self.get_assignments_by_login(login):
            if title == assignment.title:
                assignments_with_title.append(assignment)
        return assignments_with_title
    







