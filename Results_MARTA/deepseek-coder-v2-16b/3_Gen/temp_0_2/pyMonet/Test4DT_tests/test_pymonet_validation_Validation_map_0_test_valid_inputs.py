
import pytest
from pymonet.validation import Validation

def test_valid_inputs():
    val = Validation(10, [])
    mapped_val = val.map(lambda x: x * x)
    
    assert mapped_val.value == 100
    assert len(mapped_val.errors) == 0
