
import pytest
from pymonet.box import Box
from pymonet.lazy import Lazy

# Test cases for the Box class initialization and method behavior

def test_box_initialization():
    # Test creating a Box instance with an integer value
    box_int = Box(123)
    assert box_int.value == 123

    # Test creating a Box instance with a string value
    box_str = Box("Hello, World!")
    assert box_str.value == "Hello, World!"

def test_to_lazy():
    # Create a Box instance
    box = Box(42)
    
    # Call the to_lazy method and check the return type
    lazy_box = box.to_lazy()
    assert isinstance(lazy_box, Lazy)
    
    # Check that the value function returns the original value when folded