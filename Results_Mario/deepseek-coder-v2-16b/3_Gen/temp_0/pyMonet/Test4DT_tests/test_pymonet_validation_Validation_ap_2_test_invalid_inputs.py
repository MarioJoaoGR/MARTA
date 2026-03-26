
import pytest
from pymonet.validation import Validation

def test_invalid_inputs():
    def add_error_function(value):
        return Validation(None, ['An error occurred'])
    
    # Test with a valid value
    val = Validation("Success", [])
    new_val = val.ap(add_error_function)
    assert len(new_val.errors) == 1
    assert new_val.errors[0] == 'An error occurred'
    
    # Test with an invalid value
    val_invalid = Validation(None, [])
    new_val_invalid = val_invalid.ap(add_error_function)
    assert len(new_val_invalid.errors) == 1
    assert new_val_invalid.errors[0] == 'An error occurred'
