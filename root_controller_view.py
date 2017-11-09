import getpass
import os


class RootControllerView:

    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

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