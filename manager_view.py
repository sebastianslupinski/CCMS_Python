from view import View


class ViewManager(View):

    @classmethod
    def display_manager_menu(cls):
        manager_commands = ('Create new mentor', 'Edit existing mentor', 'Delete mentor', 'Show mentor list',
                            'Show student list')
        cls.display_menu(manager_commands)
        return cls.getch()

    @classmethod
    def input_mentor_info(cls):

        print("You are creating new user, remember you can't use ',' or spaces and phone number must be 9-digits")

        login = View.valid_data("Please enter mentor's login: ")
        password = View.valid_data("Please enter password: ")
        name = View.valid_data("Please enter mentor's name: ")
        surname = View.valid_data("Please enter mentors's surname: ")
        phone_number = cls.get_user_phone_number()

        return login, password, name, surname, phone_number

    @classmethod
    def display_edit_option(cls):
        edit_commands = ('Change name', 'Change surname', 'Change password', 'Change phone number', 'Go back')
        cls.display_menu(edit_commands)
        return cls.get_user_input('Choose: ')
