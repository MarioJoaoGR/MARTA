
import pytest
from pymonet.box import Box

# Test valid input where Box is not empty and has a valid value
def test_valid_input():
    box = Box(value=42)
    assert not isinstance(box, type(None))
    assert box.value == 42

# Test edge case where Box is empty (is_nothing is True)
def test_edge_case():
    with pytest.raises(TypeError):
        Box()
