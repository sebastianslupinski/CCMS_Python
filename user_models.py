class User:

    def __init__(self, login, password, name, surname, phone_number):

        self.login = login
        self.password = password
        self.name = name
        self.phone_number = phone_number
        self.surname = surname
        self.email = name.lower() + '.' + surname.lower() + '@codecool.com'

    def change_attribute_value(self, atribute_type, new_atribute):
        if atribute_type == 'name':
            self.name = new_atribute

        elif atribute_type == 'surname':
            self.surname = new_atribute

        elif atribute_type == 'phone_number':
            self.phone_number = new_atribute

        elif atribute_type == 'password':
            self.password = new_atribute

    def __str__(self):

        full_info = []

        full_info.append("{} | {} {} | {} | {}".format(self.login, self.name, self.surname, self.email, self.phone_number))

        return " ".join(full_info)


class Manager(User):

    def __init__(self, login, password, name, surname, phone_number):

        super().__init__(login, password, name, surname, phone_number)
        self.rank = "manager"


class Mentor(User):

    def __init__(self, login, password, name, surname, phone_number):

        super().__init__(login, password, name, surname, phone_number)
        self.rank = "mentor"


class Employee(User):

    def __init__(self, login, password, name, surname, phone_number):

        super().__init__(login, password, name, surname, phone_number)
        self.rank = "employee"


class Student(User):

    def __init__(self, login, password, name, surname, phone_number, group):
        super().__init__(login, password, name, surname, phone_number)
        self.rank = "student"
        self.group = group
