
import pytest
from pymonet.box import Box

# Test cases for the Box class
def test_create_box_with_integer():
    box = Box(123)  # Create a Box object with the value 123
    assert box.value == 123

def test_create_box_with_string():
    box_str = Box("Hello, World!")  # Create a Box object with the string "Hello, World!"