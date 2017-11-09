class StudentView:

    @staticmethod
    def get_user_input(message):
        return input(message)

    @staticmethod
    def custom_print(message):
        print(message)

    @staticmethod
    def display_menu(options):
        for option in options:
            print(str(options.index(option) + 1) + "----->" + option)

    @staticmethod
    def display_work():
        print(''' //
                 (")  Acces will be granted on 23.10.2017
                 UU\ 
                <><>''')

    @classmethod
    def display_student_menu(cls):
        student_commands = ('Display grades', 'Submit assignment','Go back')
        cls.display_menu(student_commands)
        return cls.get_user_input('Choose: ')

