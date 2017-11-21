from view import View
from user_database import UserDataBase
from user_models import User


class UserController():

    @classmethod
    def show_user_list(cls,user_list):
        View.clear_terminal()
        users = cls.convert_list(user_list)
        View.display_user_table(users)
        View.getch()

    @staticmethod
    def convert_list(list):
        users = ''
        counter = 1
        for user in list:
            users += (str(counter) + '.' + user.__str__()) + '\n'
            counter += 1
        return users

    # @classmethod
    # def check_if_login_in_database(cls, login):

    #     if UserDataBase.pick_user_by_login(login) is True:
    #         return True
    #     else:
    #         return False

    @classmethod
    def create_new_login(cls):

        login_is_valid = False

        while login_is_valid is False:

            login = View.validate_login()

            if isinstance(UserDataBase.pick_user_by_login(login), User):
                continue
            else:
                return login