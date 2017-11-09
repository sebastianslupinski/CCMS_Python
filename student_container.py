from user_models import Student


class StudentContainer:

    def __init__(self):
        self.student_list = []
        self.group_a = []
        self.group_b = []

    def add_student(self, user):
        self.student_list.append(user)

    def add_student_to_group(self, user, group):
        if group == 'a':
            self.group_a.append(user)
        elif group == 'b':
            self.group_b.append(user)

    def edit_student(self):
        pass

    def remove_student(self, index):
        self.student_list.pop(index)

    def get_student_list(self):

        return self.student_list

    def get_student_group(self, group):

        if group == 'a':
            return self.group_a
        
        elif group == 'b':
            return self.group_b
