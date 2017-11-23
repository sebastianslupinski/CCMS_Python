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

        password = View.valid_data("Please enter password: ")
        name = View.valid_data("Please enter mentor's name: ")
        surname = View.valid_data("Please enter mentors's surname: ")
        phone_number = cls.get_user_phone_number()

        return password, name, surname, phone_number

    @classmethod
    def input_guided_groups(cls):

        groups = input("Please enter guided groups separated by ',': ")
        return groups.split(",")

    @classmethod
    def display_edit_option(cls):
        ViewManager.clear_terminal()
        edit_commands = ('Change name', 'Change surname', 'Change password', 'Change phone number', 'Go back')
        cls.display_menu(edit_commands)
        return cls.get_user_input('Choose: ')