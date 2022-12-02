import pymongo
from urllib.parse import quote_plus


def get_database():
    password = quote_plus("u^qEiHIOw7Ax378Ux3#fci%VcvD6aq")

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    client = pymongo.MongoClient(
        f"mongodb+srv://alarrode:{password}@cluster0.0qgkquq.mongodb.net/?retryWrites=true&w=majority")

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

