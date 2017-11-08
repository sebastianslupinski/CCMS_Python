class MentorContainer:

    def __init__(self):
        self.mentor_list = []

    def add_mentor(self, user):
        self.mentor_list.append(user)

    def edit_mentor(self):
        pass

    def remove_mentor(self, index):
        self.mentor_list.pop(index)