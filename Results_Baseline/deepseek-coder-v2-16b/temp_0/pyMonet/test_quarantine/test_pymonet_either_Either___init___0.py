
# Module: pymonet.either
import pytest
from pymonet.either import Either, Left, Right
from typing import Callable

# Test initialization with a Left value
def test_left_init():
    left_value = Either(Left("error message"))
    assert isinstance(left_value, Either)
    assert left_value.is_left() is True
    assert left_value.is_right() is False
    assert left_value.value == "error message"

# Test initialization with a Right value
def test_right_init():
    right_value = Either(Right(42))
    assert isinstance(right_value, Either)
    assert right_value.is_left() is False
    assert right_value.is_right() is True
    assert right_value.value == 42

# Test case method with a Left value
def test_case_method_with_left():
    either = Either(Left("error message"))
    def error_handler(value):
        return f"Error: {value}"
    def success_handler(value):
        return f"Success: {value}"
    result = either.case(error_handler, success_handler)
    assert result == "Error: error message"

# Test case method with a Right value
def test_case_method_with_right():
    right_either = Either(Right("Hello"))
    def error_handler(value):
        return f"Error: {value}"
    def success_handler(value):
        return f"Success: {value}"
    result = right_either.case(error_handler, success_handler)
    assert result == "Success: Hello"

# Test to_box method with a Left value
def test_to_box_with_left():
    left_value = Either(Left("error message"))
    transformed_left = left_value.to_box()
    assert isinstance(transformed_left, Box)
    assert transformed_left.value == "error message"

# Test to_box method with a Right value
def test_to_box_with_right():
    right_value = Either(Right(42))
    transformed_right = right_value.to_box()
    assert isinstance(transformed_right, Box)
    assert transformed_right.value == 42

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Either___init___0
pyMonet/Test4DT_tests/test_pymonet_either_Either___init___0.py:11:11: E1101: Instance of 'Either' has no 'is_left' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_either_Either___init___0.py:19:11: E1101: Instance of 'Either' has no 'is_left' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_either_Either___init___0.py:47:40: E0602: Undefined variable 'Box' (undefined-variable)
pyMonet/Test4DT_tests/test_pymonet_either_Either___init___0.py:54:41: E0602: Undefined variable 'Box' (undefined-variable)


"""