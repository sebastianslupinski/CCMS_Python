import csv

class Assignment:

    def __init__(self, title, login, description, answer, grade):
        self.title = title
        self.login = login
        self.description = description
        self.answer = answer
        self.grade = grade

class AssignmentContainer:

    @staticmethod
    def read_from_file(file_name):
        assignment_table = list(csv.reader(open(file_name, 'r', encoding="utf8"), delimiter=','))
        return assignment_table

    def create_assignment():
        pass

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








