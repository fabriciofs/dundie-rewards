from subprocess import CalledProcessError, check_output

import pytest


@pytest.mark.integration
@pytest.mark.medium
def test_load_positive_call_load_command():
    out = (
        check_output(["dundie", "load", "tests/assets/people.csv"])
        .decode("utf-8")
        .split("\n")
    )
    assert len(out) == 2


@pytest.mark.integration
@pytest.mark.medium
def test_load_negative_call_load_command_with_wrong_params():
    with pytest.raises(CalledProcessError):
        out = (
            check_output(["dundie", "loady", "tests/assets/people.csv"])
            .decode("utf-8")
            .split("\n")
        )
        assert len(out) == 2
