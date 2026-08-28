
import pytest
from pymonet.box import Box

# Scenario 1: Test valid input
def test_valid_input():
    box_int = Box(42)
    mapped_box = box_int.map(lambda x: x * 2)
    assert mapped_box.value == 84

# Scenario 2: Test edge case with None as the input value
def test_edge_case_none():
    box_none = Box(None)
    mapped_box = box_none.map(lambda x: x * 2 if x is not None else 0)
    assert mapped_box.value == 0

# Scenario 3: Test invalid input by passing a non-callable object to map function
def test_invalid_input():
    box_str = Box("Hello, World!")
    with pytest.raises(TypeError):
        box_str.map('not_a_function')
