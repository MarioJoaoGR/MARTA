
# Module: pymonet.either
import pytest
from pymonet.either import Either, Left, Right
from pymonet.monad_try import Try

# Test initialization with Left and Right values
def test_init():
    left_value = Either(Left("error message"))
    assert not left_value.is_right(), "Expected is_right() to be False for a Left value"
    
    right_value = Either(Right(42))