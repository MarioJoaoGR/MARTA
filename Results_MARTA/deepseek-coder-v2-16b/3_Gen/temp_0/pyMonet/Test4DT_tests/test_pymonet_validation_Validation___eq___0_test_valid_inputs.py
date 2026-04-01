
import pytest
from pymonet.validation import Validation

def test_valid_inputs():
    val = Validation('success', [])
    assert val.value == 'success'
    assert len(val.errors) == 0
