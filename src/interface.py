import database.users_table as users_table
from termcolor import colored


def connexion(dbname):
    print(colored("Veuillez vous connecter.", "blue"))
    print("Nom de compte:")
    name_account = input()
    print("Mot de passe:")
    password = input()
    connexion_value = users_table.connexion_database(dbname, name_account, password)

    # Check if connected
    if connexion_value :
        print(colored("Nom de compte ou mot de passe incorrect.", "red"))
    else:
        print(colored("Vous êtes connecté.", 'green'))
    return connexion_value
