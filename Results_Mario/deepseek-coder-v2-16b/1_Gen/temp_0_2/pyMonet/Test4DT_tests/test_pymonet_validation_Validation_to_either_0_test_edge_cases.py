
import pytest
from pymonet.validation import Validation
from pymonet.either import Left, Right

def test_to_either():
    # Test when there are no errors
    val = Validation(10, [])
    either_val = val.to_either()
    assert isinstance(either_val, Right)
    assert either_val.value == 10

    # Test when there are errors
    val = Validation(None, ['Error message'])
    either_val = val.to_either()
    assert isinstance(either_val, Left)
    assert either_val.value == ['Error message']
