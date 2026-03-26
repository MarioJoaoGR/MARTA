
import pytest
from pymonet.validation import Validation

def test_fail():
    # Test that a failed validation returns the correct structure with None value and errors list
    val = Validation.fail(["Error1", "Error2"])
    assert val.value is None
    assert val.errors == ["Error1", "Error2"]
