
import pytest
from pymonet.validation import Validation
from pymonet.either import Left, Right

def test_edge_case_none():
    # Test when value is None and errors are empty
    val = Validation(None, [])
    either_val = val.to_either()
    
    assert isinstance(either_val, Right)
    assert either_val.value is None

    # Test when value is not None and errors are empty
    val = Validation("Success", [])
    either_val = val.to_either()
    
    assert isinstance(either_val, Right)
    assert either_val.value == "Success"

    # Test when value is None and there are errors
    val = Validation(None, ["Error occurred"])
    either_val = val.to_either()
    
    assert isinstance(either_val, Left)
    assert either_val.value == ["Error occurred"]
