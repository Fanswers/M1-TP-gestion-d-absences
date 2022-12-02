import pymongo
from urllib.parse import quote_plus
import uuid


def get_database():
    password = quote_plus("u^qEiHIOw7Ax378Ux3#fci%VcvD6aq")

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    client = pymongo.MongoClient(
        f"mongodb+srv://alarrode:{password}@cluster0.0qgkquq.mongodb.net/?retryWrites=true&w=majority", uuidRepresentation='standard')

    db = client["test_unitaires"]

    return db


def find_one(dbname):

    users_col = dbname["users"]

    x = users_col.find_one()

    print(x)


def connexion_database(dbname, name_account, password):
    collection = dbname['users']
    cursor = collection.find({})
    for document in cursor:
        if name_account == document["name"] and password == document["password"]:
            return False
    return True



def create_user(name, last_name, role, password, address, phone_number):
    dbname = get_database()

    users_col = dbname["users"]

    user_item = {
        "_id": uuid.uuid4(),
        "name": name,
        "last_name": last_name,
        "role": role,
        "password": password,
        "address": address,
        "phone_number": phone_number
    }

    users_col.insert_one(user_item)

    print("\nUtilisateur créé avec succès !")
