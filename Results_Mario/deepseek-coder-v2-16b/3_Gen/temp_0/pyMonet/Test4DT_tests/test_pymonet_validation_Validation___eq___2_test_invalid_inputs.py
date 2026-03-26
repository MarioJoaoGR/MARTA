
import pytest
from pymonet.validation import Validation

def test_invalid_inputs():
    # Test with invalid inputs
    val1 = Validation(None, ["Error 1"])
    val2 = Validation(None, [])
    
    assert not (val1 == val2), "Expected different errors"
