from view import View
from prettytable import PrettyTable


class StudentView(View):

    @staticmethod
    def display_work():
        print(''' //
                 (")  Acces will be granted on 23.10.2017
                 UU\ 
                <><>''')

    @classmethod
    def display_student_menu(cls):
        student_commands = ('Display grades', 'Submit assignment')
        cls.display_menu(student_commands)
        return cls.get_user_input('Choose: ')

    @staticmethod
    def show_assignments_grades(assignments):
        View.clear_terminal()
        table = PrettyTable(['Assignments', 'Grades'])
        for row in assignments:
            title = row[0]
            grade = row[1]
            table.add_row([title, grade])
        table.align = 'l'
        print(table)

    @staticmethod
    def show_assignmets(assignments):
        View.clear_terminal()
        table = PrettyTable(['Title', 'Description', 'Answer', 'Grade'])
        for row in assignments:
            title = row[0]
            description = row[1]
            answer = row[2]
            grade = row[3]
            table.add_row([title, description, answer, grade])
        table.align = 'l'
        print(table)

    @staticmethod
    def submit_assignment(assignment):
        print('Title: ' + assignment.title + '\n\n' + 'Description: ' + assignment.description + '\n\n')
        return input('Enter your answer below:\n\n')