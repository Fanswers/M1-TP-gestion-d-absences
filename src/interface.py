from database.users_table import create_user as database_create_user


def create_user():
    print("Remplissez les informations de l'utilisateurs :")

    name = input("1/6 - Prénom :")
    last_name = input("2/6 - Nom :")
    role = input("3/6 - Quel poste occupe l'utilisateur ? Enseignant, Etudiant ou Administrateur ?")
    password = input("4/6 - Mot de passe :")
    second_password = input("4/6 - Retapez votre mot de passe :")
    while second_password != password:
        second_password = input("4/6 - Incorrect, retapez votre mot de passe :")
    address = input("5/6 - Adresse :")
    phone_number = input("5/6 - Téléphone :")

    validate = input("Valider la création - Y/n")
    if validate == "Y":
        database_create_user(name, last_name, role, password, address, phone_number)
