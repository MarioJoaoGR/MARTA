
import pytest
from pymonet.box import Box

def test_valid_input():
    box = Box(5)
    assert box.value == 5
