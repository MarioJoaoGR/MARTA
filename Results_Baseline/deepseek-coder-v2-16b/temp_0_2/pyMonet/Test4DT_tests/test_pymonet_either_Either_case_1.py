
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

# Test case for the 'case' method when Either is Left
def test_left_case(left_value):
    result = left_value.case(lambda x: "error", lambda x: "success")
    assert result == "error"

# Corrected test case for the 'case' method when Either is Right
def test_right_case(right_value):
    result = right_value.case(lambda x: "error", lambda x: "success")