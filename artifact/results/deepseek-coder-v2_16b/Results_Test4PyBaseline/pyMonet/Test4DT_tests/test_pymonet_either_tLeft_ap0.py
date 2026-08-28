# Module: pymonet.either
import pytest
from pymonet.either import Left

# Test case for creating a Left instance with an integer value
def test_left_creation():
    left_value = Left(10)
    assert left_value.value == 10

# Test case for using the `ap` method to apply a monadic function
def test_left_ap():
    left_instance = Left(10)
    result = left_instance.ap(Left("error"))
    assert result.value == 10

# Test case for handling different scenarios using the `case` method
def handle_error(value):
    return "Error handling {}".format(value)

def handle_success(value):
    return "Successfully handled {}".format(value)

def test_left_case():
    left_instance = Left("error message")
    result = left_instance.case(handle_error, handle_success)
    assert result == "Error handling error message"

# Test case for converting an Either to a Box monad (not applicable here as it's not defined in the provided function)
# def test_left_to_box():
#     either_instance = Left(15)
#     box = either_instance.to_box()
#     assert box.value == 15

# Test case for converting an Either to a Try monad (not applicable here as it's not defined in the provided function)
# def test_left_to_try():
#     try_from_either = either_instance.to_try()
#     assert try_from_either.is_success == True

# Test case for converting an Either to a Lazy monad (not applicable here as it's not defined in the provided function)
# def test_left_to_lazy():
#     lazy = either_instance.to_lazy()
#     assert lazy() == 15
