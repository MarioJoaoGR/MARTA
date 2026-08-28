
import pytest
from pymonet.box import Box

# Test valid input where Box is initialized with a value of any type
def test_valid_input():
    box = Box(42)
    assert not isinstance(box, Exception)  # Ensure that the initialization does not raise an exception
    assert box.value == 42

# Test invalid input where Box is initialized without a value (should raise TypeError)
def test_invalid_input():
    with pytest.raises(TypeError):
        box = Box()
