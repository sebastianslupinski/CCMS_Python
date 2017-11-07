
import getpass

class User:

    def __init__(self, rank, login, password):
        self.rank = rank
        self.login = login
        self.password = password

user_list = []


def get_user_by_login(login):
    for user in user_list:
        if user.login == login:
            return user

def login():
    while True:
        username = input("Type username\n")
        user = get_user_by_login(username)
        if user:
            password = getpass.getpass("Type password\n")
            if user.password == password:
                return True




def read_csv():
    with open("user_data.csv.txt") as file:
        for line in file:
            data = line.split(",")
            user_list.append(User(data[0], data[1], data[2]))

# read_csv()
# login()
hu = User(*[2,3,4])
print(hu)