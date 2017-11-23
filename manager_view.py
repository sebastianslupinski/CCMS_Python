from view import View
from prettytable import PrettyTable


class ViewManager(View):

    @classmethod
    def display_manager_menu(cls):
        manager_commands = ('Create new mentor', 'Edit existing mentor', 'Delete mentor', 'Show mentor list',
                            'Show employee list', 'Show student list')
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
        edit_commands = ('Change name', 'Change surname', 'Change password', 'Change phone number')
        for option in edit_commands:
            print(str(edit_commands.index(option) + 1) + "----->" + option)
        print("\n0----->Back\n")
        return cls.getch()

    @staticmethod
    def display_mentor_table(users):
        table = PrettyTable(['Login', 'Name', 'Surname', 'Email', 'Phone_number', 'Guided Classes'])
        for user in users:
            user = user.split(" ")
            user_login = user[0]
            user_name = user[1] 
            user_surname = user[2]
            user_email = user[3]
            user_phone_number = user[4]
            user_guided_classes = user[5]
            table.add_row([user_login, user_name, user_surname, user_email, user_phone_number, user_guided_classes])
        table.align = 'l'
        print(table)

    @staticmethod
    def display_employee_table(users):
        table = PrettyTable(['Login', 'Name', 'Surname', 'Email', 'Phone_number'])
        for user in users:
            user = user.split(" ")
            user_login = user[0]
            user_name = user[1] 
            user_surname = user[2]
            user_email = user[3]
            user_phone_number = user[4]
            table.add_row([user_login, user_name, user_surname, user_email, user_phone_number])
        table.align = 'l'
        print(table)


    @classmethod
    def display_groups(cls, classes):

        print("All avaible classes are: ")
        for group in classes:
            print("class name: ", group)
