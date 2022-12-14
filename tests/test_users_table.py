import pytest
import database.users_table as users
import mongomock
from contextlib import nullcontext as does_not_raise


@pytest.fixture
def client_mock():
    yield mongomock.MongoClient()


@pytest.fixture
def mock_db(client_mock):
    obj = {'_id': 1, 'last_name': 'Admin', 'password': 'Admin'}
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
def test_connexion_user(mock_db, test_input_name, test_input_password, expected_output):
    test_value, test_user = users.connexion_database(mock_db, test_input_name, test_input_password)
    assert test_value == expected_output


@pytest.mark.parametrize(
    "expected_output",
    [{'_id': 1,
        'last_name': 'Admin',
        'password': 'Admin'}],
    ids=[
        'good users'
    ]
)
def test_show_all_users_database_good(mock_db, expected_output):
    test_recup = users.show_all_users_database(mock_db)
    assert test_recup == [expected_output]


@pytest.mark.parametrize(
    "expected_output",
    [{'_id': 2,
        'last_name': 'Admin',
        'password': 'Admin'},
     {'_id': 1,
      'last_name': 'Admon',
      'password': 'Admin'},
     {'_id': 1,
      'last_name': 'Admin',
      'password': 'Admon'},
     {'_id': 2,
      'last_name': 'Admon',
      'password': 'Admon'},
     {'_id': "",
      'last_name': '',
      'password': ''}
     ],
    ids=[
        'bad id',
        'bad last_name',
        'bad password',
        'bad all',
        'empty'
    ]
)
def test_show_all_users_database_bad(mock_db, expected_output):
    test_recup = users.show_all_users_database(mock_db)
    assert test_recup != [expected_output]


@pytest.mark.parametrize(
    "user_info, expectation",
    [({"uuid": "30352e23-e61b-42d9-bf4b-7d7986af8b22",
       "name": "Admin"}, does_not_raise()),
    ({"uuid": "3033-e61b-42d9-bf4b-7d7986af8b22",
       "name": "Admin"}, pytest.raises(ValueError))
     ],
    ids=[
        'good uuid',
        'wrong id'
    ]
)
def test_update_user(mock_db, user_info, expectation):
    with expectation:
        users.update_user(mock_db, user_info["uuid"], user_info["name"], "Admin", "Administrateur", "Admin", "Admin", "00 00 00 00 00")
