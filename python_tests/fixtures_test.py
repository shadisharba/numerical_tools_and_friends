import pytest


# fixtures can be used to standardize input across multiple unit tests.
@pytest.fixture
def input_dict():
    return {"a": 1}


def test_fixture(input_dict):
    assert input_dict["a"] == 1, f"Check fixture {input_dict}"
