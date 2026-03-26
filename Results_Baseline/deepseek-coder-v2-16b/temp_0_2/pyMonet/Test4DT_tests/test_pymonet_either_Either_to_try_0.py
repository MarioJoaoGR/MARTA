
# Module: pymonet.either
import pytest
from pymonet.either import Either, Left, Right
from pymonet.monad_try import Try

# Test cases for the Either class and its methods

def test_create_left():
    left_value = Either(Left("error message"))
    assert not left_value.is_right(), "Expected Left to return False"

def test_create_right():
    right_value = Either(Right(42))