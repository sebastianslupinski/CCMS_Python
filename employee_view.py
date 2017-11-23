from view import View


class EmployeeView(View):

    @classmethod
    def display_employee_menu(cls):
        employee_commands = ('Show Student list', 'Look pretty', 'Do you wanna play a game ?')
        cls.display_menu(employee_commands)
        return cls.getch()
