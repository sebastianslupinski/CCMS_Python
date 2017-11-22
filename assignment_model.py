import csv
from student_container import StudentContainer


class Assignment:

    def __init__(self, title, login, description, group, answer, grade):
        self.title = title
        self.login = login
        self.description = description
        self.group = group
        self.answer = ""
        self.grade = 0

    def __str__(self):
        return self.title + " " + self.login + " " + self.group + "\n\n" + self.description + "\n\n" + self.answer


class AssignmentsModel:

    def __init__(self, student_container):
        self.student_container = student_container
        self.assignment_list = []

    def read_from_file(self, file_name):
        assignment_table = list(csv.reader(open(file_name, 'r'), delimiter=','))
        assignment_objects = []
        for item in assignment_table:
            assignment_objects.append(Assignment(*item))
        self.assignment_list = assignment_objects
        return assignment_objects

    def create_assignment(self, group, title, description):
        group_assignment = []
        logins = self.get_group_logins(group)
        for login in logins:
            group_assignment.append(Assignment(title, login, description, group, "", None))
        assignment_list = self.read_from_file('assignment_data.csv')
        if not assignment_list:
            assignment_list = []
        assignment_list.extend(group_assignment)
        self.save_to_file(assignment_list)

    def save_to_file(self, assignments):
        with open('assignment_data.csv', 'w') as file:
            for assignment in assignments:
                file.write(
                    assignment.title + "," +
                    assignment.login + "," +
                    assignment.description + "," +
                    assignment.group + "," +
                    assignment.answer + "," +
                    str(assignment.grade) + "\n")

    def get_group_logins(self, group):
        logins = []
        for student in self.student_container.get_student_group(group):
            logins.append(student.login)
        return logins

    def get_assignments_by_title(self, group, title):
        titles = []
        for assignment in self.get_assignments_by_group(group):
            if assignment.title == title:
                titles.append(assignment)
        return titles

    def get_assignments_by_group(self, group):
        assignment_by_group = []
        for assignment in self.read_from_file('assignment_data.csv'):
            if group == assignment.group:
                assignment_by_group.append(assignment)
        return assignment_by_group

    def get_assignment(self, group, title, login):
        for assignment in self.read_from_file('assignment_data.csv'):
            if assignment.group == group and assignment.title == title and assignment.login == login:
                return assignment
    
    def grade_assignment(self, assignment, grade):
        for item in self.assignment_list:
            if assignment == item:
                assignment.grade = grade
                self.save_to_file(self.assignment_list)

