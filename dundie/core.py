import os
from csv import reader

from dundie.database import add_movement, add_person, commit, connect
from dundie.utils.log import get_logger

log = get_logger()


def load(filepath):
    try:
        csv_data = reader(open(filepath))
    except FileNotFoundError as e:
        log.error(str(e))
        raise e

    db = connect()
    people = []
    headers = ["name", "dept", "role", "email"]
    for line in csv_data:
        person_data = dict(zip(headers, [item.strip() for item in line]))
        pk = person_data.pop("email")
        person, created = add_person(db, pk, person_data)
        return_data = person.copy()
        return_data["created"] = created
        return_data["email"] = pk
        people.append(return_data)
    commit(db)
    return people


def read(**query):
    db = connect()
    return_data = []
    for pk, data in db["people"].items():
        if (query_dept := query.get("dept")) and query_dept != data["dept"]:
            continue
        if (query_email := query.get("email")) and query_email != pk:
            continue
        return_data.append(
            {
                **data,
                "email": pk,
                "balance": db["balance"][pk],
                "last_movement": db["movement"][pk][-1]["date"],
            }
        )
    return return_data


def add(value, **query):
    people = read(**query)
    if not people:
        raise RuntimeError("Not Found")

    user = os.getenv("USER")
    db = connect()
    for person in people:
        add_movement(db, person["email"], value, user)
    commit(db)
