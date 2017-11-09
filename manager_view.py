
class ViewManager:

    @staticmethod
    def get_user_input(message):
        return input(message)

    @classmethod
    def display_manager_menu(cls):
        manager_commands = ('Create new mentor', 'Edit existing mentor', 'Delete mentor', 'Show mentor list',
                            'Show student list', 'Go back')
        cls.display_menu(manager_commands)
        return cls.get_user_input('Choose: ')

    @classmethod
    def input_mentor_info(cls):

        login = input("Please enter mentor's login: ")
        password = input("Please enter password: ")
        name = input("Please enter mentor's name: ")
        surname = input("Please enter mentors's surname: ")
        phone_number = cls.get_user_phone_number()

        return login, password, name, surname, phone_number

    @staticmethod
    def display_menu(options):
        for option in options:
            print(str(options.index(option) + 1) + "----->" + option)

    @classmethod
    def display_edit_option(cls):
        edit_commands = ('Change name', 'Change surname', 'Change password', 'Change phone number', 'Go back')
        cls.display_menu(edit_commands)
        return cls.get_user_input('Choose: ')

    @classmethod
    def get_user_phone_number(cls):
        while True:
            phone_number = cls.get_user_input('Please enter mentors phone number: ')
            if len(phone_number) == 9:
                try:
                    return int(phone_number)
                except ValueError:
                    print('Not a number input!')
            else:
                print('Invalid or too short input!')


    @staticmethod
    def display_all_mentors(mentors):
        print(mentors)

    @staticmethod
    def custom_print(message):
        print(message)