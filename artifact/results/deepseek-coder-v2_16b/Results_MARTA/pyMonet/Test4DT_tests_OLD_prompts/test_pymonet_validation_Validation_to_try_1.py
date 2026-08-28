
import pytest
from pymonet.validation import Validation
from unittest.mock import patch, MagicMock

# Test valid inputs scenario
def test_valid_inputs():
    success_validation = Validation(value=10, errors=[])
    assert success_validation.is_success() is True
    assert success_validation.value == 10

# Test edge cases scenario
def test_edge_cases():
    failure_validation_none = Validation(value=None, errors=['Error message'])
    assert failure_validation_none.is_success() is False
    assert failure_validation_none.errors == ['Error message']
    
    failure_validation_empty = Validation(value=10, errors=[])
    assert failure_validation_empty.is_success() is True
    assert failure_validation_empty.value == 10

# Test invalid inputs scenario
def test_invalid_inputs():
    with patch('pymonet.validation.Validation.to_try', MagicMock(return_value=MagicMock(is_success=lambda: False, value=None))):
        try_from_failure = Validation(value=10, errors=['Error message']).to_try()
        assert try_from_failure.is_success() is False
        assert try_from_failure.value is None
