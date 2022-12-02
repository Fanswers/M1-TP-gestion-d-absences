import database.users_table as users_table
import interface
from termcolor import colored


from database.users_table import find_one
import interface as interface

if __name__ == '__main__':
    database = users_table.get_database()

    not_connected = True
    while not_connected:
        not_connected = interface.connexion(database)

    interface.create_user()
