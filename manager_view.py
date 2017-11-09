
class ViewManager:

    @staticmethod
    def get_user_input(message):
        return input(message)

    @classmethod
    def display_manager_menu(cls):
        manager_commands = ('Create new mentor', 'Edit existing mentor', 'Delete mentor', 'Show mentor list'
                            'Show student list', 'Go back')
        for option in manager_commands:
            print(str(manager_commands.index(option) + 1) + "----->" + option)
        chosen_option = cls.get_user_input('Choose: ')
        return chosen_option

    @staticmethod
    def input_mentor_info():

        login = input("Please enter mentor's login: ")
        password = input("Please enter password: ")
        name = input("Please enter mentor's name: ")
        surname = input("Please enter mentors's surname: ")
        phone_number = input("Please enter mentors's phone number: ")

        return login, password, name, surname, phone_number


    @classmethod
    def select_edit_option(cls):
        edit_commands = ('Change name', 'Change surname', 'Change password', 'Change phone number', 'Go back')
        for option in edit_commands:
            print(str(edit_commands.index(option) + 1) + "----->" + option)
        choosen_option = cls.get_user_input('Choose: ')
        return choosen_option
