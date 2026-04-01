
from pymonet.validation import Validation
import pytest

def test_edge_cases():
    # Create a Validation instance with a success value and no errors
    val = Validation("Success", [])
    
    # Define a function that returns a new Validation with an error
    def add_error_function(value):
        return Validation(None, ["An error occurred"])
    
    # Call the ap method to accumulate errors
    new_val = val.ap(add_error_function)
    
    # Check if there are any errors in the accumulated result
    assert len(new_val.errors) == 1
    assert new_val.errors[0] == "An error occurred"
