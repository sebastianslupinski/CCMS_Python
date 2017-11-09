from mentor_controller import MentorController
from manager_controller import ManagerController
from student_controller import StudentController
from employee_controller import EmployeeController
from root_controller_view import RootControllerView
from user_database import UserDataBase
from employee_container import EmployeeContainer
from mentor_container import MentorContainer
from student_container import StudentContainer

class RootController:

    def __init__(self):
        self.view = RootControllerView
        self.student_container = StudentContainer()
        self.mentor_container = MentorContainer()
        self.employee_container = EmployeeContainer()                
        self.manager = ManagerController(self.mentor_container, self.student_container)
        self.mentor = MentorController(self.student_container)
        self.student = StudentController()
        self.employee = EmployeeController(self.student_container)
        self.user_database = UserDataBase(self.student_container, self.mentor_container, self.employee_container)

    def login(self):
        self.view.greet_user()
        while True:
            username = self.view.get_user_input("Type your username: \n")
            user = self.user_database.pick_user_by_login(username)
            if user:
                password = self.view.get_pass("Type your password: \n")
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
        user_controller.start()
        


s = RootController()
s.start()





