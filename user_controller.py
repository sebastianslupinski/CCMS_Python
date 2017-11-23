from view import View
from user_database import UserDataBase
from user_models import User


class UserController():

    notification = None
    notification_visibility_time = 1.2

    @classmethod
    def show_user_list(cls, user_list):
        View.clear_terminal()
        users = cls.prepare_user_table(user_list)
        View.display_user_table(users)

    @classmethod
    def create_new_login(cls):

        login_is_valid = False

        while login_is_valid is False:
            View.clear_terminal()
            View.display_notification(cls.notification)
            cls.notification = None
            login = View.validate_login()

            if isinstance(UserDataBase.pick_user_by_login(login), User):
                cls.notification = "Please select another username"
                continue
            else:
                return login
    
    @staticmethod
    def prepare_user_table(users):
        data = []
        for user in users:
            data.append(str(user))
        return data
