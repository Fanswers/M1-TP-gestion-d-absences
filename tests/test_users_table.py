import pytest
import database.users_table as users
import mongomock


@pytest.fixture
def client_mock():
    yield mongomock.MongoClient()


@pytest.fixture
def mock_db(client_mock):
    obj = {'last_name': 'Admin', 'password': 'Admin'}
    client_mock.db['users'].insert_one(obj)
    yield client_mock.db


@pytest.mark.parametrize(
    "test_input_name, test_input_password, expected_output",
    [("Admin", "Admin", 0),
     ("Admon", "Admin", 1),
     ("Admin", "Admon", 1),
     ("Admon", "Admon", 1),
     ("", "", 1)],
    ids=[
        'good identifiers',
        'wrong name',
        'wrong password',
        'both wrong',
        'no identifiers',
    ]
)
def test_connexion_database(mock_db, test_input_name, test_input_password, expected_output):
    test_value, test_user = users.connexion_database(mock_db, test_input_name, test_input_password)
    assert test_value == expected_output

