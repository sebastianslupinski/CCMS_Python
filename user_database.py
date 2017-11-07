import csv
user_list = []

def read_from_csv(filename = 'user_data.csv'):
    with open(filename, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == 'manager':
                user_list.append(Manager(*row)) #zamienic Manager na dobrą nazwę
            elif row[0] == 'employee':
                user_list.append(Employee(*row)) #zamienic Employee na dobrą nazwę
            elif row[0] == 'mentor':
                user_list.append(Mentor(*row))  # zamienic Mentor na dobrą nazwę
            else: #Else czy elif ?
                user_list.append(Student(*row))  # zamienic Student na dobrą nazwę
read_from_csv()
