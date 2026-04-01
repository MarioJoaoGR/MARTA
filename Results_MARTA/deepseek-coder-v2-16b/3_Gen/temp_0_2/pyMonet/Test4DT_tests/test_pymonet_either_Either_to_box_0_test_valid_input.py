
import pytest
from pymonet.either import Either, Left, Right
from pymonet.box import Box

def test_valid_input():
    # Test with a valid integer value
    either = Either(10)
    box = either.to_box()
    assert isinstance(box, Box)
    assert box.value == 10

    # Test with a valid string value
    either_str = Either("Hello, World!")
    box_str = either_str.to_box()
    assert isinstance(box_str, Box)
    assert box_str.value == "Hello, World!"
