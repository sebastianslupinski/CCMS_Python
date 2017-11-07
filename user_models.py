class User:

    def __init__(self, login, password, name, surname, phone_number):

        self.login = login
        self.password = password
        self.name = name
        self.phone_number = phone_number
        self.surname = surname
        self.email = name + '.' + surname + '@codecool.com'

    def __str__(self):

        full_info = []

        full_info.append("{} {} | {} | {}".format(self.name, self.surname, self.email, self.phone_number))

        return " ".join(full_info)


class Manager(User):

    def __init__(self, login, password, name, surname, phone_number):

        super().__init__(name, login, password, surname, phone_number)
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

    def __init__(self, login, password, name, surname, phone_number):
        super().__init__(login, password, name, surname, phone_number)
        self.rank = "student"
