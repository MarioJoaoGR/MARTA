
from pymonet.validation import Validation
import pytest

def add_one(x):
    if x > 0:
        return Validation(x + 1, [])
    else:
        return Validation(None, ["Value must be positive"])

def test_bind():
    val = Validation(5, [])
    result = val.bind(add_one)
    assert result.value == 6
    assert result.errors == []
    
    negative_val = Validation(-1, [])
    result_negative = negative_val.bind(add_one)
    assert result_negative.value is None
    assert result_negative.errors == ["Value must be positive"]
