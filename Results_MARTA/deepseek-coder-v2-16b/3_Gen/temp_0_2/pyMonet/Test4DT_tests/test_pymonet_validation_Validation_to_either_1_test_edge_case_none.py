
import pytest
from pymonet.validation import Validation
from pymonet.either import Left, Right

def test_edge_case_none():
    # Create a Validation instance with a value and an empty list of errors
    val = Validation("Success", [])
    
    # Convert the Validation to Either
    either_val = val.to_either()
    
    # Assert that it is a Right with the correct value
    assert isinstance(either_val, Right)
    assert either_val.value == "Success"

def test_edge_case_none_with_errors():
    # Create a Validation instance with an initial error
    val = Validation("Success", ["Initial Error"])
    
    # Convert the Validation to Either
    either_val = val.to_either()
    
    # Assert that it is a Left with the correct errors
    assert isinstance(either_val, Left)
    assert either_val.value == ["Initial Error"]
