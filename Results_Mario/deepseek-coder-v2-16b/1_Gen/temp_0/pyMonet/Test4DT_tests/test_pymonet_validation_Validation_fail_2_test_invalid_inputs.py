
import pytest
from pymonet.validation import Validation

def test_invalid_inputs():
    # Test that a failed validation is created correctly when invalid inputs are provided
    val = Validation.fail(["Error1", "Error2"])
    
    assert val.value is None
    assert len(val.errors) == 2
    assert val.errors == ["Error1", "Error2"]
