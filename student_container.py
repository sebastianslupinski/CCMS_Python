from user_models import Student

class StudentContainer:

    def __init__(self):
        self.student_list = []

    def add_student(self,user):
        self.student_list.append(user)

    def edit_student(self):
        pass

    def remove_student(self, index):
        self.student_list.pop(index)