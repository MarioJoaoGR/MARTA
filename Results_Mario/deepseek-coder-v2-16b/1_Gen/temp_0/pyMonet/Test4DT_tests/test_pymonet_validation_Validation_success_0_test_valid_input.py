
import pytest
from pymonet.validation import Validation

def test_valid_input():
    val = Validation.success('Success')
    assert val.value == 'Success'
    assert len(val.errors) == 0
