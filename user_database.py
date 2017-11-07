import csv
import user_models
user_list = []

def read_from_csv(filename = 'user_data.csv'):
    with open(filename, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            rank = row[0]
            if rank == 'manager':
                user_list.append(user_models.Manager(*row[1:])) #zamienic Manager na dobrą nazwę
            elif rank == 'employee':
                user_list.append(user_models.Employee(*row[1:])) #zamienic Employee na dobrą nazwę
            elif rank == 'mentor':
                user_list.append(user_models.Mentor(*row[1:]))  # zamienic Mentor na dobrą nazwę
            elif rank == 'student':
                user_list.append(user_models.Student(*row[1:]))  # zamienic Student na dobrą nazwę
read_from_csv()
