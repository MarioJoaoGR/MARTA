
# Module: pymonet.either
import pytest
from pymonet.either import Either, Left, Right

# Test initialization with Left value
def test_left_initialization():
    left_value = Either(Left("error message"))
    assert not left_value.is_right()
    assert isinstance(left_value.value, Left)
    assert left_value.value.value == "error message"

# Test initialization with Right value
def test_right_initialization():
    right_value = Either(Right(42))
    assert right_value.is_right()
    assert isinstance(right_value.value, Right)
    assert right_value.value.value == 42

# Test equality between two Left instances
def test_left_equality():
    left1 = Either(Left("error message"))
    left2 = Either(Left("error message"))
    assert left1 == left2

# Test equality between a Left and a Right instance
def test_inequality_between_left_and_right():
    left = Either(Left("error message"))
    right = Either(Right(42))
    assert not (left == right)

# Test inequality between two different Left instances with different values
def test_inequality_between_two_different_lefts():
    left1 = Either(Left("first error"))
    left2 = Either(Left("second error"))
    assert left1 != left2

# Test equality between two Right instances
def test_right_equality():
    right1 = Either(Right(42))
    right2 = Either(Right(42))
    assert right1 == right2

# Test inequality between two different Right instances with different values
def test_inequality_between_two_different_rights():
    right1 = Either(Right(42))
    right2 = Either(Right(84))
    assert not (right1 == right2)

# Test equality between a Left and a Right instance
def test_inequality_between_left_and_right():
    left = Either(Left("error message"))
    right = Either(Right(42))
    assert not (left == right)

# Test inequality with an unrelated object
def test_inequality_with_unrelated_object():
    left = Either(Left("error message"))
    unrelated_obj = "I am a string"
    assert not (left == unrelated_obj)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Either___eq___0
pyMonet/Test4DT_tests/test_pymonet_either_Either___eq___0.py:51:0: E0102: function already defined line 27 (function-redefined)


"""