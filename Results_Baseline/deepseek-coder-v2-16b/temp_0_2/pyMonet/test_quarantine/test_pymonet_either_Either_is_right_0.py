
# Module: pymonet.either
import pytest
from pymonet.either import Either, Left, Right
try:
    from pymonet.monad import Box  # Importing here to avoid circular import issues
except ImportError:
    pass

# Test creating a Left instance
def test_left_instance():
    left_value = Either(Left("error message"))
    assert not left_value.is_right(), "Expected is_right() to return False for Left"
    assert isinstance(left_value.value, Left), "Expected value to be of type Left"
    assert left_value.value.value == "error message", "Expected the error message to be 'error message'"

# Test creating a Right instance
def test_right_instance():
    right_value = Either(Right(42))
    assert right_value.is_right(), "Expected is_right() to return True for Right"
    assert isinstance(right_value.value, Right), "Expected value to be of type Right"
    assert right_value.value.value == 42, "Expected the value to be 42"

# Test checking if an Either instance is right
def test_is_right():
    left = Either(Left("error message"))
    right = Either(Right(42))
    
    assert not left.is_right(), "Expected is_right() to return False for Left"
    assert right.is_right(), "Expected is_right() to return True for Right"

# Test handling either case using the `case` method
def test_case_method():
    def error_handler(value):
        return f"Error: {value}"
    
    def success_handler(value):
        return value * 2
    
    left = Either(Left("error message"))
    right = Either(Right(42))
    
    assert left.case(error_handler, success_handler) == "Error: error message", "Expected error handler to be called"
    assert right.case(error_handler, success_handler) == 84, "Expected success handler to be called"

# Test applying a function contained within an Either structure
def test_ap():
    left_value = Left(42)
    right_value = Right("hello")
    
    result1 = left_value.ap(right_value)
    assert isinstance(result1, Left), "Expected the result to be a Left"
    assert result1.value == 42, "Expected the value inside Left to remain unchanged"
    
    result2 = right_value.ap(left_value)
    assert isinstance(result2, Right), "Expected the result to be a Right"
    assert result2.value == "hello", "Expected the string 'hello' to remain unchanged"

# Test transforming the Either instance into a Box monad
def test_to_box():
    either = Either(123)
    box = either.to_box()
    assert isinstance(box, Box), "Expected the result to be a Box"
    assert box.value == 123, "Expected the value inside Box to be 123"
    
    either_str = Either("Hello, World!")
    box_str = either_str.to_box()
    assert isinstance(box_str, Box), "Expected the result to be a Box"
    assert box_str.value == "Hello, World!", "Expected the value inside Box to be 'Hello, World!'"

# Test transforming the Either instance into a Try monad
def test_to_try():
    left = Either(Left("error message"))
    right = Either(Right(42))
    
    assert not left.to_try().is_success(), "Expected to_try() on Left to return a failed Try"
    assert right.to_try().is_success(), "Expected to_try() on Right to return a successful Try"

# Test transforming the Either instance into a Lazy monad
def test_to_lazy():
    either = Either(5)
    lazy_either = either.to_lazy()
    assert lazy_either.fold() == 5, "Expected the function stored in Lazy to be called and return the original value"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Either_is_right_0
pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0.py:83:11: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""