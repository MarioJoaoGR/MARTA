
from pymonet.box import Box
import pytest

def test_invalid_input():
    box = Box(123)  # Create a valid Box instance with an integer value
    with pytest.raises(TypeError):
        result = box.bind("not a callable")  # Attempt to bind with a non-callable object, which should raise TypeError
