
from pymonet.validation import Validation

def test_valid_inputs():
    value = "Success"
    errors = []
    
    # Create an instance of Validation with valid inputs
    validation = Validation(value, errors)
    
    # Check if the initialization was successful
    assert validation.value == value
    assert len(validation.errors) == 0
