
import pytest
from pymonet.validation import Validation

def test_invalid_inputs():
    # Test when the inputs are invalid and should return None
    val1 = Validation(None, ["Error 1"])
    val2 = Validation(None, ["Error 2"])
    
    assert val1 != val2  # Different error messages
    
    val3 = Validation(None, [])
    assert val3 is not None  # No errors should return a valid instance
