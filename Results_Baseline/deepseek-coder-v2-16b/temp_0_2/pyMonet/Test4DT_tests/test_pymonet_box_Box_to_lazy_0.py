
import pytest
from pymonet.box import Box

# Test cases for the Box class initialization and method behavior

def test_box_initialization():
    # Test creating a Box instance with an integer value
    box_int = Box(123)
    assert box_int.value == 123

    # Test creating a Box instance with a string value
    box_str = Box("Hello, World!")