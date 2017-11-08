class ViewMentor:

    @staticmethod
    def display_menu():

        print("")

    @staticmethod
    def input_student_info():

        login = input("Please enter student's login: ")
        password = input("Please enter password: ")
        name = input("Please enter student's name: ")
        surname = input("Please enter student's surname: ")
        phone_number = input("Please enter student's phone number")

        return login, password, name, surname, phone_number

    