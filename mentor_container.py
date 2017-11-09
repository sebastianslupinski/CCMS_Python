class MentorContainer:

    def __init__(self):
        self.mentor_list = []

    def add_mentor(self, user):
        self.mentor_list.append(user)

    def edit_mentor(self):
        pass

    def remove_mentor(self, index):
        self.mentor_list.pop(index)

    def get_mentor_list(self):
        return self.mentor_list

    def pick_mentor_by_login(self, login):
        for mentor in self.mentor_list:
            if mentor.login == login:
                return mentor
