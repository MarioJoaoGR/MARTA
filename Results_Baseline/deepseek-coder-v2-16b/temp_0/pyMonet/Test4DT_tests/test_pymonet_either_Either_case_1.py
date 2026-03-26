
import pytest
from pymonet.either import Either, Left, Right

# Test initialization of Either with Left value
def test_left_init():
    left_value = Either(Left("error message"))
    assert not left_value.is_right()

# Test case for handling error when Either is Left
def test_case_with_left():
    def error_handler(value):
        return f"Handled {value}"
    
    left_value = Either(Left("error message"))
    result = left_value.case(error_handler, lambda x: None)