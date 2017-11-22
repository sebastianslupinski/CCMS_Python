from user_models import Student
from user_database import UserDataBase


class StudentContainer:

    def __init__(self):
        self.student_list = []
        self.list_of_classes = {}

    def add_student(self, user):
        self.student_list.append(user)
        UserDataBase.add_user_to_db(user)

    def add_student_to_group(self, user, group):
        if group in self.list_of_classes.keys():
            for key in self.list_of_classes:
                if key == group:
                    self.list_of_classes[key].append(user)
        else:
            self.list_of_classes[group] = [user]

    def edit_student(self):
        pass

    def remove_student(self, user):
        self.student_list.remove(user)
        UserDataBase.remove_user_from_db(user)

    def get_student_list(self):
        return self.student_list

    def get_student_group(self, group):
        return self.list_of_classes[group]

    def pick_student_by_login(self, login):
        for user in self.student_list:
            if user.login == login:
                return user

    @staticmethod
    def save_edited_data():
        UserDataBase.write_to_csv()
