
import pytest
from pymonet.validation import Validation

def add_error_function(value):
    return Validation(None, ["An error occurred"])

class TestValidation:
    def test_invalid_inputs(self):
        # Creating a Validation instance that holds a success value
        val = Validation("Success", [])
        
        # Adding an error to the Validation instance using the ap method
        new_val = val.ap(add_error_function)
        
        # Checking if there are any errors
        assert len(new_val.errors) == 1, "Expected one error but got none"
        assert new_val.errors[0] == "An error occurred", "Error message does not match expected value"
