
import pytest
from pymonet.either import Right

# Test valid input where Right is not empty and has a valid value
def test_valid_input():
    right_value = Right(42)
    assert right_value.is_right() == True
    assert right_value.value == 42

# Test edge case where Right is empty (should be considered as not having a value)
def test_edge_case():
    with pytest.raises(TypeError):
        right_empty = Right()
