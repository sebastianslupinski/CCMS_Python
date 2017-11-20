from view import View


class EmployeeView(View):

    @classmethod
    def display_employee_menu(cls):
        employee_commands = ('Show Student list', 'Go back')
        cls.display_menu(employee_commands)
        return cls.get_user_input('Choose: ')
