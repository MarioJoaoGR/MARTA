
import pytest
from pymonet.box import Box

# Test valid input where Maybe is not nothing and has a valid value
def test_valid_input():
    maybe_some = Box(value=42)
    assert maybe_some.value == 42

# Test edge case where Maybe is empty (is_nothing is True)
def test_edge_case():
    with pytest.raises(TypeError):
        box = Box()
