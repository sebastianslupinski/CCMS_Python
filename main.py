from mentor_controller import MentorController
from manager_controller import ManagerController
from student_controller import StudentController
from employee_controller import EmployeeController
from view import DisplayRootController
import getpass

class RootController:

    def login():
        pass

    def __init__(self):
        self.student = StudentController()
        self.mentor = MentorController()
        self.employee = EmployeeController()
        self.manager = ManagerController()

    def start():
        self.login()





