class User:

    def __init__(self, login, password, name, surname, phone_number):

        self.login = login
        self.password = password
        self.name = name
        self.phone_number = phone_number
        self.surname = surname
        self.email = name.lower() + '.' + surname.lower() + '@codecool.com'

    def change_name(self, new_name):
        self.name = new_name

    def change_surname(self, new_surname):
        self.surname = new_surname

    def change_password(self, new_password):
        self.password = new_password

    def change_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

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
#
# ziomus = Mentor("ziomus", "ziomus", "Ziomus", "Ziomus", "r435234523")
# print(ziomus)
