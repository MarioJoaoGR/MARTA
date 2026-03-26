
# Module: pymonet.either
import pytest
from pymonet.either import Either, Left, Right

# Test cases for the Either class initialization
def test_either_initialization():
    left_value = Either(Left("error message"))
    right_value = Either(Right(42))
    
    assert isinstance(left_value, Either)
    assert isinstance(right_value, Either)
    assert not left_value.is_right()