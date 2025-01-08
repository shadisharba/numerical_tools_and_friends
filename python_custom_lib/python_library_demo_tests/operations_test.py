import pytest
from python_library_demo import operations


def test_addition_of_two_positive_numbers():
    result = operations.add(5, 3)
    assert result == 8


def test_addition_of_two_negative_numbers():
    result = operations.add(-5, -3)
    assert result == -8


def test_addition_of_positive_and_negative_number():
    result = operations.add(5, -3)
    assert result == 2

def test_expected_error():
    # with pytest.raises(SystemExit) as wrapped_exception:
    with pytest.raises(TypeError) as wrapped_exception:
        assert 1 + "a", "This should raise an error"
    # assert wrapped_exception.type == SystemExit
    # assert wrapped_exception.value.code == 0

def division_of_two_positive_numbers():
    result = operations.divide(10, 2)
    assert result == 5


def division_of_two_negative_numbers():
    result = operations.divide(-10, -2)
    assert result == 5


def division_of_positive_and_negative_number():
    result = operations.divide(10, -2)
    assert result == -5


def division_by_zero_raises_exception():
    with pytest.raises(ZeroDivisionError):
        operations.divide(10, 0)
