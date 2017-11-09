import csv
import user_models
from student_container import StudentContainer
from mentor_container import MentorContainer
from employee_container import EmployeesContainer


class UserDataBase:

    def __init__(self):
        self.user_list = []
        self.student_container = StudentContainer()
        self.mentor_container = MentorContainer()
        self.employee_container = EmployeesContainer()
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

    def write_to_csv(self, filename='user_data.csv', mode='w'):
        with open(filename, mode) as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.user_list)

    def pick_user_by_login(self, login):
        for user in self.user_list:
            if user.login == login:
                return user

