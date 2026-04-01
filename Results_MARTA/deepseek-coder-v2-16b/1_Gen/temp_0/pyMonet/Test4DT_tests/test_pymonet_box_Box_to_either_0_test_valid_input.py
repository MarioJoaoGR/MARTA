
import pytest
from pymonet.box import Box
from pymonet.either import Right

def test_valid_input():
    box = Box(42)
    assert isinstance(box.to_either(), Right)
    assert box.to_either().value == 42
