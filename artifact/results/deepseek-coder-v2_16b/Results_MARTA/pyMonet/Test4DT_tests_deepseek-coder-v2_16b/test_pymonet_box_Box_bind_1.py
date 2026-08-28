
import pytest
from pymonet.box import Box

# Test valid input scenario
def test_valid_input():
    int_box = Box(42)
    assert int_box.value == 42

# Test edge case with None as input scenario
def test_edge_case():
    none_box = Box(None)
    assert none_box.value is None

# Test invalid input raising TypeError scenario
def test_invalid_input():
    with pytest.raises(TypeError):
        invalid_box = Box()
