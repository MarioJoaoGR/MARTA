
import pytest
from pymonet.either import Left, Right
from pymonet.validation import Validation

def test_valid_input():
    # Create a Validation instance with a success value and an empty errors list
    val = Validation("Success", [])
    
    # Call the to_either method
    either_val = val.to_either()
    
    # Assert that the result is a Right with the correct value
    assert isinstance(either_val, Right)
    assert either_val.value == "Success"

def test_invalid_input():
    # Create a Validation instance with an initial error message
    val = Validation(None, ["Error occurred"])
    
    # Call the to_either method
    either_val = val.to_either()
    
    # Assert that the result is a Left with the correct errors list
    assert isinstance(either_val, Left)
    assert either_val.value == ["Error occurred"]
