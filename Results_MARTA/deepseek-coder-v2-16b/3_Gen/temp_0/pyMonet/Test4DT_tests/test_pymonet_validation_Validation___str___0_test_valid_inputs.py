
import pytest
from pymonet.validation import Validation

def test_valid_inputs():
    val = Validation(42, [])
    assert val.value == 42
    assert len(val.errors) == 0
    assert val.is_success() is True
