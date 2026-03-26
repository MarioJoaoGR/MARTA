
import pytest
from pymonet.validation import Validation

def test_invalid_inputs():
    # Setup
    val_invalid = Validation(None, ['InvalidInputError'])
    def add_error_function(value):
        return Validation(None, ['FunctionError'])
    
    # Test invalid inputs and error handling scenarios
    assert len(val_invalid.errors) == 1
    assert 'InvalidInputError' in val_invalid.errors
    
    new_val = val_invalid.ap(add_error_function)
    assert len(new_val.errors) == 2
    assert 'InvalidInputError' in new_val.errors
    assert 'FunctionError' in new_val.errors
