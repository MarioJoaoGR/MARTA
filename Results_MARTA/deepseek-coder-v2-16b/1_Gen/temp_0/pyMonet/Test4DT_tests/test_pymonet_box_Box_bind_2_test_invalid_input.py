
import pytest
from pymonet.box import Box

def test_invalid_input():
    box = Box('string')
    with pytest.raises(TypeError):
        invalid_function = 123  # This is a non-callable function
        mapped_value = box.bind(invalid_function)
