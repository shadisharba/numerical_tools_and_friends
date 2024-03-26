import sys
import pytest
@pytest.mark.group1
def test_something():
    assert True

@pytest.mark.xfail
def test_fail():
    assert 1 == 2, "This should fail"

@pytest.mark.skip
def test_skip():
    raise Exception("This test should be skipped")

@pytest.mark.skipif(sys.version_info.major == 3, reason="requires Python 2.x :)")
def test_skipif():
    pass

@pytest.mark.parametrize("n", [2, 4, 6])
def test_even_number(n):
    assert not n % 2, f"{n} is not an even number"

@pytest.mark.parametrize(["n", "expected_output"], [(1, 3), (2, 6)])
def test_multiplication(n, expected_output):
    assert n * 3 == expected_output, "Check multiplication"