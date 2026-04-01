
import pytest
from pymonet.validation import Validation

def test_valid_inputs():
    val = Validation("Success", [])
    assert val.is_success() is True
    assert val.value == "Success"
    assert len(val.errors) == 0
