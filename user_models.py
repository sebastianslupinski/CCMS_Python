class User:

    def __init__(self, login, password, name, surname, phone_number):

        self.login = login
        self.password = password
        self.name = name
        self.surname = phone_number
        self.email = name + '.' + surname + '@codecool.com'


class Manager(User):

    def __init__(self, login, password, name, surname, phone_number):

        super().__init__(name, login, password, name, surname, phone_number)
        self.email = name + '.' + surname + '@codecool.com'
        self.rank = "manager"


class Mentor(User):

    def __init__(self, login, password, name, surname, phone_number):

        super().__init__(login, password, name, surname, phone_number)
        self.email = name + '.' + surname + '@codecool.com'
        self.rank = "mentor"


class Employee(User):

    def __init__(self, login, password, name, surname, phone_number):

        super().__init__(login, password, name, surname, phone_number)
        self.email = name + '.' + surname + '@codecool.com'
        self.rank = "employee"


class Student(User):

    def __init__(self, login, password, name, surname, phone_number):
        super().__init__(login, password, name, surname, phone_number)
        self.email = name + '.' + surname + '@codecool.com'
        self.rank = "student"
