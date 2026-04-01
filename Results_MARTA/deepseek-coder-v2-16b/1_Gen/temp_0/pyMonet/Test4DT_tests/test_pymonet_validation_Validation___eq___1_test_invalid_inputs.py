
import pytest
from pymonet.validation import Validation

def test_invalid_inputs():
    # Test with invalid inputs
    val1 = Validation(None, ["Error 1"])
    val2 = Validation(None, ["Error 2"])
    
    assert not (val1 == val2), "Expected different errors to be considered unequal"
