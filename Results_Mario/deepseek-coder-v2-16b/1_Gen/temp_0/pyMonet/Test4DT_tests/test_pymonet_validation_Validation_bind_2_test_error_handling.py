
import pytest
from pymonet.validation import Validation

def test_error_handling():
    val = Validation(10, [])
    
    def add_five(x):
        if x > 5:
            return Validation(x + 5, [])
        else:
            return Validation(None, ["Value must be greater than 5"])
    
    result = val.bind(add_five)
    
    assert result.value == 15
    assert len(result.errors) == 0
