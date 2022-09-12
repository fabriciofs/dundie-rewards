import pytest

from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


@pytest.mark.unit
@pytest.mark.parametrize(
    "address", ["test@email.com", "joe@doe.com", "a@b.c.br"]
)
def test_positive_check_valid_email(address):
    """Ensure email is valid."""
    assert check_valid_email(address) is True
    assert check_valid_email(address) is True


@pytest.mark.unit
@pytest.mark.parametrize(
    "address", ["test@email", "joe@com", "joecom", "@email.com"]
)
def test_negative_check_valid_email(address):
    """Ensure email is valid."""
    assert check_valid_email(address) is False
    assert check_valid_email(address) is False
    assert check_valid_email(address) is False


@pytest.mark.unit
def test_generate_simple_password():
    """Teste generation of random simple passwords."""
    passwords = []
    for _ in range(100):
        passwords.append(generate_simple_password(8))

    assert len(set(passwords)) == 100
