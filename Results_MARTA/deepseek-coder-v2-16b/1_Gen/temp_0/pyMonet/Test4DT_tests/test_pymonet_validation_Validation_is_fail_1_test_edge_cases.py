
import pytest
from pymonet.validation import Validation

def test_is_fail():
    # Test when errors list is empty
    val = Validation("Success", [])
    assert not val.is_fail(), "Expected is_fail() to return False for an empty errors list"

    # Test when errors list has one error
    val = Validation("Failure", ["Error message"])
    assert val.is_fail(), "Expected is_fail() to return True for a non-empty errors list"

    # Test when errors list has multiple errors
    val = Validation("Failure", ["Error 1", "Error 2"])
    assert val.is_fail(), "Expected is_fail() to return True for a non-empty errors list"
