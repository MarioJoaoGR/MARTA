
from pymonet.validation import Validation
import pytest

def test_invalid_inputs():
    # Test invalid inputs by creating a Validation instance with None value and an error message
    val = Validation(None, ["Error 1", "Error 2"])
    
    # Check if the errors list is as expected
    assert len(val.errors) == 2
    assert val.errors == ["Error 1", "Error 2"]
    
    # Check if the value is None as expected
    assert val.value is None
