import getpass
import os
import time


class View:

    @classmethod
    def get_user_input(cls, message=""):
        if message:
            return input(message)
        return cls.getch()

    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def display_notification(notification, wait=None):
        if notification:
            View.clear_terminal()
            print(notification)
            if wait:
                time.sleep(wait)
                View.clear_terminal()
            else:
                print("Press any key...\n")
                View.getch()
                View.clear_terminal()

    @staticmethod
    def getch():
        # import sys, tty, termios
        # fd = sys.stdin.fileno()
        # old_settings = termios.tcgetattr(fd)
        # try:
        #     tty.setraw(sys.stdin.fileno())
        #     ch = sys.stdin.read(1)
        # finally:
        #     termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        # return ch
        return input("")

    @staticmethod
    def greet_user():
        print("Welcome to CcMS")

    @staticmethod
    def custom_print(message):
        print(message)

    @staticmethod
    def get_pass(message):
        return getpass.getpass(message)

    @staticmethod
    def display_user_table(users):
        print(users)

    @staticmethod
    def display_menu(options):
        for option in options:
            print(str(options.index(option) + 1) + "----->" + option)
        print("\n9----->Log out\n0----->Quit")

    @classmethod
    def get_user_phone_number(cls):
        phone_number_valid = False
        while not phone_number_valid:
            phone_number = cls.get_user_input("Please enter user's phone number: ")
            if cls.validate_phone_number(phone_number) is True:
                phone_number_valid = True
            else:
                cls.display_notification('Invalid or too short input!')
        return phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        MAX_LEN_PHONE_NUMBER = 9
        if len(phone_number) == MAX_LEN_PHONE_NUMBER:
            for number in phone_number:
                if not number.isdigit():
                    return False
            return True

    @staticmethod
    def valid_data(message):

        MIN_DATA_LENGHT = 3
        data_validation = False
        while data_validation is False:

            user_input = input(message)

            if " " in user_input or "," in user_input:
                continue
            elif len(user_input) < MIN_LOGIN_LENGHT:
                continue
            else:
                data_validation = True

        return user_input

    @classmethod
    def validate_login(cls):
        cls.clear_terminal()
        print("You are creating new user, remember you can't use ',' or spaces and phone number must be 9-digits")
        return cls.valid_data("Please enter new user login: ")