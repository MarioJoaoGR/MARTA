
import pytest
from pymonet.validation import Validation

def test_valid_input():
    val = Validation(5, [])
    
    def add_one(x):
        return Validation(x + 1, [])
    
    result = val.bind(add_one)
    
    assert result.value == 6
    assert result.errors == []
