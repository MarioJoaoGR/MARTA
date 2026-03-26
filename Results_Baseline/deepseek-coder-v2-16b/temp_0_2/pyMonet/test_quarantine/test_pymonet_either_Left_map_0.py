
# Module: pymonet.either
import pytest
from pymonet.either import Left, Right

# Test initialization of Left and Right instances
def test_left_initialization():
    left_value = Left("error message")  # Creating a Left instance with an error message
    assert isinstance(left_value, Left)
    assert left_value.value == "error message"

    right_value = Right(42)  # Creating a Right instance with the value 42
    assert isinstance(right_value, Right)
    assert right_value.value == 42

# Test map method of Left class
def test_left_map():
    left_instance = Left("error message")
    mapped_left = left_instance.map(lambda x: f"Processed {x}")
    assert isinstance(mapped_left, Left)
    assert mapped_left.value == "error message"

# Test is_right method of Either class
def test_either_is_right():
    left_value = Left("error message")
    right_value = Right(42)
    
    assert not left_value.is_right()  # Output: False
    assert right_value.is_right()  # Output: True

# Test case method of Either class
def test_either_case():
    def error_handler(value):
        return f"Error: {value}"
    
    def success_handler(value):
        return value * 2
    
    left_value = Left("error message")
    right_value = Right(42)
    
    assert left_value.case(error_handler, success_handler) == "Error: error message"
    assert right_value.case(error_handler, success_handler) == 84

# Test ap method of Either class
def test_either_ap():
    applicative = Right("hello")
    
    left_value = Left(lambda x: x * 2)
    result1 = left_value.ap(applicative)
    assert isinstance(result1, Left)
    assert result1.value == "error message"

    right_value = Right("hello")
    result2 = right_value.ap(applicative)
    assert isinstance(result2, Right)
    assert result2.value == "hello"

# Test to_box method of Either class
def test_either_to_box():
    either = Right(123)  # Create an Either instance with the value 123
    box = either.to_box()  # Transform the Either to a Box
    assert box.value == 123

    either_str = Right("Hello, World!")  # Create an Either instance with the string "Hello, World!"
    box_str = either_str.to_box()  # Transform the Either to a Box
    assert box_str.value == "Hello, World!"

# Test to_try method of Either class
def test_either_to_try():
    left = Right(Left("error message"))
    assert not left.to_try().is_success()  # Output: False, since it's Left

    right = Right(Right(42))
    assert right.to_try().is_success()  # Output: True, since it's Right and the value is resolved successfully

# Test to_lazy method of Either class
def test_either_to_lazy():
    either = Right(5)  # Create an Either instance with a value of 5
    lazy_either = either.to_lazy()  # Convert the Either to a Lazy monad
    assert lazy_either.fold() == 5  # The function stored in Lazy will be called, returning the original value

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Left_map_0
pyMonet/Test4DT_tests/test_pymonet_either_Left_map_0.py:81:11: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""