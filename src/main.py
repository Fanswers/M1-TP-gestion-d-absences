import database.users_table as users_table
import interface
from termcolor import colored


if __name__ == '__main__':
    database = users_table.get_database()

    not_connected = True
    while not_connected:
        not_connected = interface.connexion(database)

