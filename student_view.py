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
    def show_assignments(assignments):
        View.clear_terminal()
        table = PrettyTable(['Assaignments', 'Grades'])
        for row in assignments:
            title = row[0]
            grade = row[1]
            table.add_row([title, grade])
        table.align = 'l'
        print(table)

    @staticmethod
    def submit_assignment(assignment):
        print('Title: ' + assignment.title + '\n\n' + 'Description: ' + assignment.description + '\n\n')
        return input('Enter your answer below:\n\n')