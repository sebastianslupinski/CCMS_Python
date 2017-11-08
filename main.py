from mentor_controller import MentorController
from manager_controller import ManagerController
from student_controller import StudentController
from employee_controller import EmployeeController
from root_controller_view import RootControllerView
from user_database import UserDataBase
import getpass

class RootController:

    def login(self):
        self.view.greet_user()
        while True:
            username = self.view.get_user_input("Type your username: \n")
            user = self.user_database.pick_user_by_login(username)
            if user:
                password = self.view.get_user_input("Type your password: \n")
                if user.password == password:
                    return user


    def __init__(self):
        self.user_database = UserDataBase()
        self.view = RootControllerView
        self.student = StudentController()
        self.mentor = MentorController()
        self.employee = EmployeeController()
        self.manager = ManagerController()

    def start(self):
        user_rank = self.login().rank
        if user_rank == "manager":
            user = self.manager
        user.display_menu()
        


s = RootController()
s.start()





