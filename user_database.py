import csv
import user_models


class UserDataBase:

    def __init__(self):
        self.user_list = []
        self.mentor_list = []
        self.student_list = []
        self.employee_list = []
        self.read_from_csv()

    def read_from_csv(self, filename='user_data.csv'):
        with open(filename, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                rank = row[0]
                if rank == 'manager':
                    self.user_list.append(user_models.Manager(*row[1:]))
                elif rank == 'employee':
                    self.user_list.append(user_models.Employee(*row[1:]))
                    self.employee_list.append(user_models.Employee(*row[1:]))
                elif rank == 'mentor':
                    self.user_list.append(user_models.Mentor(*row[1:]))
                    self.mentor_list.append(user_models.Mentor(*row[1:]))
                elif rank == 'student':
                    self.user_list.append(user_models.Student(*row[1:]))
                    self.student_list.append(user_models.Mentor(*row[1:]))
