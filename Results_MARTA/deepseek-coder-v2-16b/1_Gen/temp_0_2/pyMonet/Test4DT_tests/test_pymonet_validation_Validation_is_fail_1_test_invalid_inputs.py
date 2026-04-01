
import pytest
from pymonet.validation import Validation

def test_invalid_inputs():
    # Test with a valid value
    val = Validation(10, [])
    assert not val.is_fail(), "Expected no errors for a valid input"
    
    # Test with an invalid value and added error
    val = Validation(None, ['Error message'])
    assert val.is_fail(), "Expected errors for an invalid input"
