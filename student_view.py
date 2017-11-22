from view import View


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
        print('Your assignments: \n')
        for assignment in assignments:
            print('Title: ' + assignment.title + '\n' + 'Grade: ' + str(assignment.grade) + '\n')

    @staticmethod
    def submit_assignment(assignment):
        print('Title: ' + assignment.title + '\n\n' + 'Description: ' + assignment.description + '\n\n')
        return input('Enter your answer below:\n\n')