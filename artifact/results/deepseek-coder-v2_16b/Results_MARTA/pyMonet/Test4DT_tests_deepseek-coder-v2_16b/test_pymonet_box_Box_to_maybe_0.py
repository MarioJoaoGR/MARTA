
import pytest
from pymonet.box import Box

# Test valid input scenario
def test_valid_input():
    box = Box(value=42)
    assert box.value == 42

# Test edge case with None as input
def test_edge_case():
    box = Box(value=None)
    assert box.value is None

# Test handling invalid input by raising an appropriate error
def test_invalid_input():
    try:
        box = Box()
    except Exception as e:
        assert str(e) == "Box.__init__() missing 1 required positional argument: 'value'"
