class EmployeeContainer:

    def __init__(self):
        self.employee_list = []


    def add_employee(self, user):
        self.employee_list.append(user)

    def edit_employee(self):
        pass

    def remove_employee(self, index):
        self.employee_list.pop(index)