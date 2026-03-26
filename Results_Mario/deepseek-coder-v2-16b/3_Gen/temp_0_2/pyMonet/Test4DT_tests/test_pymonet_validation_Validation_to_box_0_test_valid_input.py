
import pytest
from pymonet.validation import Validation

def test_valid_input():
    val = Validation(10, [])
    assert val.value == 10
    assert not val.errors
