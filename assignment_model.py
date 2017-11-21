import csv
from student_container import StudentContainer


class Assignment:

    def __init__(self, title, login, description, answer, grade):
        self.title = title
        self.login = login
        self.description = description
        self.answer = ""
        self.grade = 0


class AssignmentsModel:

    @staticmethod
    def read_from_file(file_name):
        assignment_table = list(csv.reader(open(file_name, 'r', encoding="utf8"), delimiter=','))
        return assignment_table

    @classmethod
    def create_assignment(cls, group, title, description):
        group_assignment = []
        logins = cls.get_group_logins(group)
        for login in logins:
            group_assignment.append(Assignment(title, login, description, "", None))
        assignment_list = cls.get_assignment_list()
        if not assignment_list:
            assignment_list = []
        assignment_list.extend(group_assignment)
        cls.save_to_file(assignment_list)

    @staticmethod
    def save_to_file(assignments):
        with open('assignment_data.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(assignments.title)

    @staticmethod
    def get_group_logins(group):
        logins = []
        for student in StudentContainer().get_student_group(group):
            logins.append(student.login)
        return logins

    @classmethod
    def get_assignment_list(cls):
        assignment_list = []
        for assignment in cls.read_from_file('assignment_data.csv'):
            assignment_list.append(Assignment(*assignment))
        return assignment_list

    @classmethod
    def get_assignments_by_login(cls, login):
        personal_asssignments = []
        for assignment in cls.get_assignment_list():
            if login == assignment.login:
                personal_asssignments.append(assignment)
        return personal_asssignments

    @classmethod
    def get_assignments_by_title(cls, title, login):
        assignments_with_title = []
        for assignment in cls.get_assignments_by_login(login):
            if title == assignment.title:
                assignments_with_title.append(assignment)
        return assignments_with_title








