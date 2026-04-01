
import pytest
from pymonet.validation import Validation

def test_invalid_inputs():
    # Test with invalid inputs (None as value)
    val = Validation(None, ["Error occurred"])
    assert not val.is_success(), "Expected failure due to errors"
