import database.users_table as users_table
from termcolor import colored
from database.users_table import create_user as database_create_user
from database.users_table import update_user as database_update_user


def connexion(dbname):
    print(colored("===== Veuillez vous connecter =====", "blue"))
    name_account = input("Nom de compte: ")
    password = input("Mot de passe: ")
    connexion_value, user = users_table.connexion_database(dbname, name_account, password)

    # Check if connected
    if connexion_value :
        print(colored("Nom de compte ou mot de passe incorrect.", "red"))
    else:
        print(colored("Vous êtes connecté.", 'green'))
    return connexion_value, user


def create_user():
    print("Remplissez les informations de l'utilisateurs :")

    name = input("1/6 - Prénom : ")
    last_name = input("2/6 - Nom : ")
    role = input("3/6 - Quel poste occupe l'utilisateur ? Enseignant, Etudiant ou Administrateur ? ")
    password = input("4/6 - Mot de passe : ")
    second_password = input("4/6 - Retapez votre mot de passe : ")
    while second_password != password:
        second_password = input("4/6 - Incorrect, retapez votre mot de passe : ")
    address = input("5/6 - Adresse : ")
    phone_number = input("6/6 - Téléphone : ")

    validate = input("Valider la création - Y/n ")
    if validate == "Y":
        database_create_user(name, last_name, role, password, address, phone_number)
        print("\nUtilisateur créé avec succès !")


def update_user():
    print("Quel utilisateur souhaitez vous modifier ?")
    uuid = input("1/6 - UUID de l'utilisateur : ")

    name = input("2/6 - Prénom : ")

    validate = input("Valider la modification - Y/n ")
    if validate == "Y":
        database_update_user(uuid, name)
        print("\nUtilisateur modifié avec succès !")


def show_informations(user):
    print(colored("===== VOS INFORMATIONS =====", "blue"))
    print("Nom: ", user["last_name"])
    print("Prenom: ", user["name"])
    print("Role: ", user["role"])
    print("Password: ", "*******")
    print("Adresse: ", user["address"])
    print("Telephone: ", user["phone_number"])


def show_all_users(dbname):
    users = users_table.show_all_users_database(dbname)
    for user in users:
        print("ID", user["_id"], "   ---   ", "Nom:", user["last_name"], "   ---   ", "Prénom:", user["name"], "   ---   ", "Role:", user["role"])


def admin_panel(dbname, user):
    is_exit = False
    while not is_exit:
        print(colored("===== INTERFACE ADMINISTRATEUR =====", "blue"))
        print("Voir les utilisateurs: 1")
        print("Ajouter un utilisateur: 2")
        print("Modifier un utilisateur: 3")
        print("Supprimer un utilisateur: 4")
        print("Quitter: 5")
        choice = input()
        match choice:
            case "1":
                show_all_users(dbname)
            case "2":
                create_user()
            case "3":
                update_user()
            case "4":
                print(choice)
            case "5":
                print(colored("Deconnexion...", "red"))
                break
            case _:
                print(colored("Ce n'est pas une entrée valide.", "red"))

