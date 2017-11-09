import getpass


class RootControllerView:

    @staticmethod
    def greet_user():
        print("Welcome to CcMS")

    @staticmethod
    def get_user_input(message):
        return input(message)

    @staticmethod
    def custom_print(message):
        print(message)

    @staticmethod
    def get_pass(message):
        return getpass.getpass(message)