
import pytest
from pymonet.validation import Validation

def test_edge_cases():
    # Test when no errors are present
    val = Validation("Success", [])
    assert val.is_success() == True
    
    # Test when errors are present
    val = Validation(None, ["Error occurred"])
    assert val.is_success() == False
