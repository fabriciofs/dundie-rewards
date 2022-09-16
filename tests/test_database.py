import pytest

from dundie.database import EMPTY_DB, add_movement, add_person, commit, connect


@pytest.mark.unit
def test_database_schema():
    db = connect()
    assert db.keys() == EMPTY_DB.keys()


@pytest.mark.unit
def test_commit_to_database():
    db = connect()
    data = {
        "name": "Joe Doe",
        "role": "Salesman",
        "dept": "Sales",
    }
    db["people"]["joe@doe.com"] = data
    commit(db)
    db = connect()
    assert db["people"]["joe@doe.com"] == data


@pytest.mark.unit
def test_add_person_for_the_first_time():
    pk = "joe@doe.com"
    data = {
        "name": "Joe Doe",
        "role": "Salesman",
        "dept": "Sales",
    }
    db = connect()
    _, created = add_person(db, pk, data)
    commit(db)
    db = connect()
    assert created is True
    assert db["people"][pk] == data
    assert db["balance"][pk] == 500
    assert len(db["movement"][pk]) == 1
    assert db["movement"][pk][0]["value"] == 500


@pytest.mark.unit
def test_add_value_for_person():
    pk = "joe@doe.com"
    data = {
        "name": "Joe Doe",
        "role": "Salesman",
        "dept": "Sales",
    }
    db = connect()
    add_person(db, pk, data)
    commit(db)
    db = connect()
    add_movement(db, pk, 250)
    assert db["balance"][pk] == 750
    assert len(db["movement"][pk]) == 2