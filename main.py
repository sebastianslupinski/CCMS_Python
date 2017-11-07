from mentor_controller import MentorController
from manager_controller import ManagerController
from student_controller import StudentController
from employee_controller import EmployeeController


class RootController:

    def __init__(self):
        self.student = StudentController()
        self.mentor = MentorController()
        self.employee = EmployeeController()
        self.manager = ManagerController()

    def start():




