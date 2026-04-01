
import pytest
from pymonet.validation import Validation

def test_edge_cases():
    # Test case for edge cases where the validation might fail or succeed
    
    # Success case with no errors
    val_success = Validation("Success", [])
    assert val_success == Validation("Success", [])
    
    # Failure case with one error
    val_failure = Validation(None, ["Error message"])
    assert not (val_failure == Validation(None, []))
    
    # Another failure case with different errors
    val_different_errors = Validation(None, ["Another error"])
    assert not (val_failure == val_different_errors)
    
    # Test equality with another type to ensure it doesn't match
    assert not (val_success == "Not a Validation")
