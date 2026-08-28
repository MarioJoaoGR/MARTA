
import pytest
from pymonet.validation import Validation

# Test valid inputs
def test_valid_inputs():
    val = Validation(value=10, errors=[])
    assert val.value == 10
    assert len(val.errors) == 0

# Test edge cases
def test_edge_cases():
    invalid_none = Validation(value=None, errors=['Error message'])
    assert invalid_none.value is None
    assert invalid_none.errors == ['Error message']
    
    invalid_empty = Validation(value=0, errors=[])
    assert invalid_empty.value == 0
    assert len(invalid_empty.errors) == 0

# Test error handling
def test_error_handling():
    failed_validation = Validation.fail(errors=['Error message 1', 'Error message 2'])
    assert failed_validation.value is None
    assert failed_validation.errors == ['Error message 1', 'Error message 2']
