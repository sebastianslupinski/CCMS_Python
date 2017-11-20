from view import View


class UserController():

    @classmethod
    def show_user_list(cls, user_list):
        View.clear_terminal()
        users = cls.convert_list(user_list)
        View.display_user_table(users)
        View.getch()

    @classmethod
    def convert_list(cls, list):
        users = ''
        counter = 1
        for user in list:
            users += (str(counter) + '.' + user.__str__()) + '\n'
            counter += 1
        return users
