
# Module: pymonet.either
import pytest
from pymonet.either import Either, Left, Right

# Test cases for the __init__ method
def test_init_left():
    left_value = Either(Left("error message"))
    assert not left_value.is_right(), "Expected is_right() to be False when value is Left"
    assert left_value.value == Left("error message"), "Expected the value to be Left('error message')"

def test_init_right():
    right_value = Either(Right(42))