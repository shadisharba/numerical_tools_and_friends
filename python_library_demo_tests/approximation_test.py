import pytest


def test_something():
    assert 1.02354099 == pytest.approx(1.023540)  # 1e-6 by default
