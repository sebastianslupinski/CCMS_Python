from user_models import Student


class StudentContainer:

    def __init__(self):
        self.student_list = []

    def add_student(self, user):
        self.student_list.append(user)

    def edit_student(self):
        pass

    def remove_student(self, index):
        self.item_list.pop(index)

    def get_student_list(self):

        students = ''
        counter = 0

        for student in self.student_list:
            students += (str(counter) + '.' + student.__str__()) + '\n'
            counter += 1
        

        return students
