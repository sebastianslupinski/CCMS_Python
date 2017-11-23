from user_database import UserDataBase


class MentorContainer:

    def __init__(self):
        self.mentor_list = []

    def add_mentor(self, user):
        self.mentor_list.append(user)
        UserDataBase.add_user_to_db(user)

    def remove_mentor(self, user):
        self.mentor_list.remove(user)
        UserDataBase.remove_user_from_db(user)

    def get_mentor_list(self):
        return self.mentor_list

    def pick_mentor_by_login(self, login):
        for mentor in self.mentor_list:
            if mentor.login == login:
                return mentor

    @staticmethod
    def save_edited_data():
        UserDataBase.write_to_csv()
