
import pytest
from pymonet.validation import Validation

# Test valid input scenario
def test_valid_input():
    val = Validation(10, [])
    assert val.value == 10
    assert val.errors == []

# Test edge case with None value and empty errors list
def test_edge_case():
    val = Validation(None, [])
    assert val.value is None
    assert val.errors == []

# Test handling invalid input by raising TypeError
def test_invalid_input():
    with pytest.raises(TypeError):
        val = Validation()
