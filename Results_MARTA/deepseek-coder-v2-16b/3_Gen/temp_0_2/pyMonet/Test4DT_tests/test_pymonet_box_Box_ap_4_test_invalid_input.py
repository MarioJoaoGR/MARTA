
import pytest
from pymonet.box import Box

def test_invalid_input():
    with pytest.raises(TypeError):
        box = Box('string')  # Valid initialization
        applicativeBox = Box([1, 2, 3])  # Valid initialization
        
        # Attempt to apply a function on invalid input (should raise TypeError)
        result = box.ap(applicativeBox)
