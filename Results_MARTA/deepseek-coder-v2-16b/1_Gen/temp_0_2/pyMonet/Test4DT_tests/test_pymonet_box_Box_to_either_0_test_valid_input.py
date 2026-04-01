
import pytest
from pymonet.box import Box
from pymonet.either import Right

def test_valid_input():
    # Create a Box instance with a valid input
    box = Box(42)
    
    # Call the to_either method and check if it returns a Right either monad with the correct value
    result = box.to_either()
    
    # Assert that the result is an instance of Right and has the expected value
    assert isinstance(result, Right)
    assert result.value == 42
