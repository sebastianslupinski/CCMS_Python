import csv
import user_models


class UserDataBase:

    user_list = []

    def __init__(self, student_container, mentor_container, employee_container):
        self.student_container = student_container
        self.mentor_container = mentor_container
        self.employee_container = employee_container
        self.read_from_csv()

    def read_from_csv(self, filename='user_data.csv'):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                rank = row[0]
                group = row[-1]
                if rank == 'manager':
                    self.user_list.append(user_models.Manager(*row[1:]))
                elif rank == 'employee':
                    new_user = user_models.Employee(*row[1:])
                    self.user_list.append(new_user)
                    self.employee_container.employee_list.append(new_user)
                elif rank == 'mentor':
                    new_user = user_models.Mentor(*row[1:])
                    self.user_list.append(new_user)
                    self.mentor_container.mentor_list.append(new_user)
                elif rank == 'student':
                    new_user = user_models.Student(*row[1:])
                    self.user_list.append(new_user)
                    self.student_container.student_list.append(new_user)
                    if group == 'a' or group == 'b':
                        self.student_container.add_student_to_group(new_user, group)

    @classmethod
    def write_to_csv(cls, filename='user_data.csv', mode='w'):
        with open(filename, mode) as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(cls.user_list)

    def pick_user_by_login(self, login):
        for user in self.user_list:
            if user.login == login:
                return user

    @classmethod
    def add_user_to_db(cls, user):
        cls.user_list.append(user)

    def validate_login(self, login):
        for user in self.user_list:
            if user.login == login:
                return False
        return True

    @classmethod
    def remove_user_from_db(cls, user):
        cls.user_list.remove(user)

    @classmethod
    def prepare_user_list(cls):
        prepared_users_list = []
        for user in cls.user_list:
            user_data = [user.rank, user.login, user.password, user.name, user.surname, user.phone_number]
            if user.rank == "student":
                user_data.append(user.group)
            prepared_users_list.append(user_data)
        return prepared_users_list

    @classmethod
    def write_to_csv(cls, filename='user_data.csv', mode='w'):
        user_list = cls.prepare_user_list()
        with open(filename, mode, newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(user_list)
