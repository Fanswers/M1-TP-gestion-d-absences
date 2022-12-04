import database.users_table as users_table
import src.interface as interface

if __name__ == '__main__':
    # Connection a la database
    database = users_table.get_database()

    # Connection utilisateur
    not_connected = True
    while not_connected:
        not_connected, user = interface.connexion(database)

    # Affichage selon le role de l'utilisateur
    if user["role"] == "Administrateur":
        interface.admin_panel(database, user)
    else:
        interface.show_informations(user)
