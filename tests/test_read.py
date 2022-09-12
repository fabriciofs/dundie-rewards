import pytest

from dundie.core import load, read
from tests.constants import PEOPLE_FILE


@pytest.mark.unit
@pytest.mark.high
def test_read_positive_without_query():
    load(PEOPLE_FILE)
    people = read()
    assert len(people) == 3
    assert people[1]["name"] == "Dwight Schrute"


@pytest.mark.unit
@pytest.mark.high
def test_read_positive_with_email_query():
    load(PEOPLE_FILE)
    people = read(email="schrute@dundermifflin.com")
    assert len(people) == 1
    assert people[0]["name"] == "Dwight Schrute"


@pytest.mark.unit
@pytest.mark.high
def test_read_positive_with_dept_query():
    load(PEOPLE_FILE)
    people = read(dept="Sales")
    assert len(people) == 2
    assert people[0]["name"] == "Jim Halpert"
