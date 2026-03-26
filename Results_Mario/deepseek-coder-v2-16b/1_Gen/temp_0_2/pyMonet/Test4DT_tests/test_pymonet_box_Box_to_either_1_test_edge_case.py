
import pytest
from pymonet.box import Box
from pymonet.either import Right

def test_Box_to_either():
    # Create a Box instance with an integer value
    box = Box(42)
    
    # Call the to_either method and check if it returns a Right either monad with the previous value
    result = box.to_either()
    
    # Assert that the result is an instance of Right and contains the original value
    assert isinstance(result, Right)
    assert result.value == 42
