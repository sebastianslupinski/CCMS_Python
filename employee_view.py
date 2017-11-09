
class EmployeeView():

    @classmethod
    def display_employee_menu(cls):
        employee_commands = ('Show Student list', 'Go back')
        cls.display_menu(employee_commands)
        return cls.get_user_input('Choose: ')

    @staticmethod
    def display_menu(options):
        for option in options:
            print(str(options.index(option) + 1) + "----->" + option)

    @staticmethod
    def get_user_input(message):
        return input(message)

    @staticmethod
    def display_all_students(students):
        print(students)
