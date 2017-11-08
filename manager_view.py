# import mentor_container
# import user_database

class ViewMentor:

    @staticmethod
    def display_menu():
        print("")

    @staticmethod
    def input_student_info():

        login = input("Please enter mentor's login: ")
        password = input("Please enter password: ")
        name = input("Please enter mentor's name: ")
        surname = input("Please enter mentors's surname: ")
        phone_number = input("Please enter mentors's phone number: ")

        return login, password, name, surname, phone_number

    @staticmethod
    def get_user_input(message):
        return input(message)
