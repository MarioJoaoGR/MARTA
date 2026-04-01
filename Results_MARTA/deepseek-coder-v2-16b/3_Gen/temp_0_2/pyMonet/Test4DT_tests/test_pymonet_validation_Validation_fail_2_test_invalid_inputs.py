
import pytest
from pymonet.validation import Validation

def test_invalid_inputs():
    # Test that a failed validation is returned when invalid inputs are provided
    value = None  # Invalid input example
    expected_errors = ["Error due to invalid input"]  # Expected error message
    
    result = Validation.fail(errors=expected_errors)
    
    assert result.value is None
    assert result.errors == expected_errors
