
import pytest
from pymonet.validation import Validation

def test_is_fail():
    # Test when there are no errors
    val = Validation(10, [])
    assert not val.is_fail(), "Expected is_fail to return False when there are no errors"

    # Test when there are errors
    val = Validation(None, ['Error message'])
    assert val.is_fail(), "Expected is_fail to return True when there are errors"
