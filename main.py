from mentor_controller import MentorController
from manager_controller import ManagerController
from student_controller import StudentController
from employee_controller import EmployeeController
from view import View
from user_database import UserDataBase
from employee_container import EmployeeContainer
from mentor_container import MentorContainer
from student_container import StudentContainer


class RootController:

    def __init__(self):
        self.view = View()
        self.student_container = StudentContainer()
        self.mentor_container = MentorContainer()
        self.employee_container = EmployeeContainer()
        self.user_database = UserDataBase(self.student_container, self.mentor_container, self.employee_container)

    def login(self):

        login_procces = True

        while login_procces:

            self.view.greet_user()
            username = self.view.get_user_input("Type your username: \n")
            user = self.user_database.pick_user_by_login(username)
            if user:
                self.view.clear_terminal()
                password = self.view.get_pass("Type your password: \n")
                if user.password == password:
                    return user
            self.view.clear_terminal()

    def get_controler(self, user):
        user_rank = user.rank
        if user_rank == "manager":
            user = ManagerController(self.mentor_container, self.student_container, user)
        elif user_rank == "mentor":
            user = MentorController(self.student_container, user)
        elif user_rank == "student":
            user = StudentController(self.student_container, user)
        elif user_rank == "employee":
            user = EmployeeController(self.student_container, user)
        return user

    def start(self):

        program_running = True

        while program_running:
            
            self.view.clear_terminal()
            user = self.login()
            user_controller = self.get_controler(user)
            program_running = user_controller.start()
            if program_running is True:
                continue
            UserDataBase.write_to_csv()
            self.view.clear_terminal()


def main():
    s = RootController()
    s.start()

if __name__ == '__main__':
    main()
