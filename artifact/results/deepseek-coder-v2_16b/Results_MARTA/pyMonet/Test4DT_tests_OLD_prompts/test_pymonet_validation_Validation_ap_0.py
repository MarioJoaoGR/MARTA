
import pytest
from unittest.mock import patch
from pymonet.validation import Validation

# Test valid inputs scenario
def test_valid_inputs():
    val = Validation(value=10, errors=[])
    assert val.value == 10
    assert len(val.errors) == 0

# Test edge cases scenario
def test_edge_cases():
    invalid = Validation(None, ['Error message'])
    assert invalid.value is None
    assert invalid.errors == ['Error message']

    invalid2 = Validation(10, [])
    assert invalid2.value == 10
    assert len(invalid2.errors) == 0

# Test error handling scenario
def test_error_handling():
    def add_one(x): return Validation(x + 1, [])
    with pytest.raises(TypeError):
        invalid = Validation(None, ['Error message'])
        invalid.ap(add_one)
