from mentor_controller import MentorController
from manager_controller import ManagerController
from student_controller import StudentController
from employee_controller import EmployeeController
from root_controller_view import RootControllerView
from user_database import UserDataBase
import getpass

class RootController:

    def __init__(self):
        self.user_database = UserDataBase()
        self.view = RootControllerView
        self.student = StudentController()
        self.mentor = MentorController()
        self.employee = EmployeeController()
        self.manager = ManagerController()

    def login(self):
        self.view.greet_user()
        while True:
            username = self.view.get_user_input("Type your username: \n")
            user = self.user_database.pick_user_by_login(username)
            if user:
                password = self.view.get_user_input("Type your password: \n")
                if user.password == password:
                    return user

    def get_controler(self, user):
        user_rank = user.rank
        if user_rank == "manager":
            user = self.manager
        elif user_rank == "mentor":
            user = self.mentor
        elif user_rank == "student":
            user = self.student
        elif user_rank == "employee":
            user = self.employee
        return user

    def start(self):
        user = self.login()
        user_controller = self.get_controler(user)
        user_controller.display_menu(user)
        


s = RootController()
s.start()





