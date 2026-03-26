
# Module: pymonet.either
import pytest
from pymonet.either import Either, Left, Right
try:
    from typing import Box  # Importing for type checking in later code
except ImportError:
    pass

# Test initialization of Either with Left and Right values
def test_either_initialization():
    left_value = Either(Left("error message"))
    assert isinstance(left_value, Either)
    assert left_value.is_left() is True
    
    right_value = Either(Right(42))
    assert isinstance(right_value, Either)
    assert right_value.is_right() is True

# Test handling either case using the `case` method
def test_either_case():
    def error_handler(value):
        return f"Error: {value}"
    
    def success_handler(value):
        return value * 2
    
    left_value = Either(Left("error message"))
    assert left_value.case(error_handler, success_handler) == "Error: error message"
    
    right_value = Either(Right(42))
    assert right_value.case(error_handler, success_handler) == 84

# Test applying a function contained within an `Either` structure
def test_either_ap():
    left_value = Left(42)
    right_value = Right("hello")
    
    def apply_function(e):
        if e.is_left():
            return Left(e.value + 1)
        else:
            return Right(e.value * 2)
    
    result1 = left_value.ap(apply_function)
    assert result1.is_left() is True
    
    result2 = right_value.ap(apply_function)
    assert result2.is_right() is True

# Test transforming the `Either` instance into a `Box`
def test_either_to_box():
    either = Either(123)  # Create an Either instance with the value 123
    box = either.to_box()  # Transform the Either to a Box
    assert isinstance(box, Box)
    assert box.value == 123
    
    either_str = Either("Hello, World!")  # Create an Either instance with the string "Hello, World!"
    box_str = either_str.to_box()  # Transform the Either to a Box
    assert isinstance(box_str, Box)
    assert box_str.value == "Hello, World!"

# Test transforming the `Either` instance into a `Try`
def test_either_to_try():
    left = Either(Left("error message"))
    right = Either(Right(42))
    assert left.to_try().is_success() is False
    assert right.to_try().is_success() is True

# Test transforming the `Either` instance into a `Lazy`
def test_either_to_lazy():
    either = Either(5)  # Create an Either instance with a value of 5
    lazy_either = either.to_lazy()  # Convert the Either to a Lazy monad
    assert lazy_either.fold() == 5

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Either___init___0
pyMonet/Test4DT_tests/test_pymonet_either_Either___init___0.py:14:11: E1101: Instance of 'Either' has no 'is_left' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_either_Either___init___0.py:74:11: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""