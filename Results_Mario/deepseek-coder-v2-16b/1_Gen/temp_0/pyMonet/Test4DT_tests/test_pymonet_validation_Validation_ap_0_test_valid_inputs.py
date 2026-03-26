
import pytest
from pymonet.validation import Validation

def test_valid_inputs():
    val = Validation("Success", [])
    
    def add_error_function(value):
        return Validation(None, ["An error occurred"])
    
    new_val = val.ap(add_error_function)
    
    assert len(new_val.errors) == 1
    assert new_val.errors[0] == "An error occurred"
