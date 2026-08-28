
import pytest
from pymonet.box import Box
from pymonet.either import Right

# Test valid input where Maybe is not nothing and has a valid value
def test_valid_input():
    box = Box(42)
    either_box = box.to_either()
    assert isinstance(either_box, Right)
    assert either_box.value == 42

# Test edge case where Maybe is empty (is_nothing is True)
def test_edge_case():
    with pytest.raises(TypeError):
        box = Box()
