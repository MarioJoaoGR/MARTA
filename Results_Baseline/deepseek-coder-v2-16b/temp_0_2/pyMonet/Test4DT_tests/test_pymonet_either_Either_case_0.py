
# Module: pymonet.either
# test_either.py
from pymonet.either import Either, Left, Right
import pytest

@pytest.fixture
def left_value():
    return Either(Left("error message"))

@pytest.fixture
def right_value():
    return Either(Right(42))

def test_left_instance(left_value):
    assert isinstance(left_value, Either)