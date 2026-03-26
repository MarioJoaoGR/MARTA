
import pytest
from pymonet.box import Box
from pymonet.either import Right

def test_valid_input():
    # Create a Box instance with a valid value
    box = Box(123)
    
    # Transform the Box to a Right either monad
    right_either = box.to_either()
    
    # Assert that the transformed object is an instance of Right and contains the original value
    assert isinstance(right_either, Right)
    assert right_either.value == 123
