
import pytest
from pymonet.box import Box

def test_valid_input():
    box = Box(123)
    applicativeBox = Box(lambda x: x + 1)
    
    # Applying the function in applicativeBox to the value in box
    result = applicativeBox.ap(box)
    
    # Assert that the result is a new Box with the expected value
    assert isinstance(result, Box)
    assert result.value == 124
