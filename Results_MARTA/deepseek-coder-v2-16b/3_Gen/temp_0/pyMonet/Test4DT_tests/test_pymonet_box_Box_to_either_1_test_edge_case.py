
from pymonet.box import Box
from pymonet.either import Right
import pytest

def test_Box_to_either():
    # Create a Box instance with an integer value
    box = Box(123)
    
    # Transform the Box to a Right either monad
    result = box.to_either()
    
    # Check if the transformation is correct
    assert isinstance(result, Right)
    assert result.value == 123
