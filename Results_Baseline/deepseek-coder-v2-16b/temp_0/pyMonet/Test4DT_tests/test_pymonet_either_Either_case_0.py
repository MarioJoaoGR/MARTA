
import pytest
from pymonet.either import Either, Left, Right

# Test initialization of Either with Left value
def test_left_init():
    left_value = Either(Left("error message"))
    assert not left_value.is_right()