import pytest

from dundie.core import add, load, read
from tests.constants import PEOPLE_FILE


@pytest.mark.unit
@pytest.mark.high
def test_add_positive_without_query():
    load(PEOPLE_FILE)
    add(500)
    people = read()
    assert people[0]["balance"] == 1000
    assert people[1]["balance"] == 600
    assert people[2]["balance"] == 600


@pytest.mark.unit
@pytest.mark.high
def test_add_positive_with_email_query():
    load(PEOPLE_FILE)
    add(500, email="schrute@dundermifflin.com")
    people = read()
    assert people[0]["balance"] == 500
    assert people[1]["balance"] == 600
    assert people[2]["balance"] == 100


@pytest.mark.unit
@pytest.mark.high
def test_add_positive_with_dept_query():
    load(PEOPLE_FILE)
    add(500, dept="Sales")
    people = read()
    assert people[0]["balance"] == 1000
    assert people[1]["balance"] == 600
    assert people[2]["balance"] == 100
