
import pytest
from pymonet.validation import Validation

def test_edge_cases():
    # Test case for edge cases where the validation might fail or succeed
    
    # Success case with no errors
    val_success = Validation("Success", [])
    assert val_success.value == "Success"
    assert len(val_success.errors) == 0
    
    # Failure case with an error
    val_failure = Validation(None, ["Error message"])
    assert val_failure.value is None
    assert val_failure.errors == ["Error message"]
    
    # Test equality between two validations
    val1 = Validation("success", [])
    val2 = Validation("success", [])
    assert val1 == val2  # Should be true since both have the same value and no errors
    
    # Test inequality due to different values
    val3 = Validation("failure", [])
    assert not (val1 == val3)  # Should be false since values are different
    
    # Test inequality due to different errors
    val4 = Validation(None, ["Another error"])
    assert not (val_failure == val4)  # Should be false since errors are different
