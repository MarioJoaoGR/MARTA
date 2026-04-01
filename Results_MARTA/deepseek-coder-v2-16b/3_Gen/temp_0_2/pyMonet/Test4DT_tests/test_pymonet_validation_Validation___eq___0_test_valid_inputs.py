
import pytest
from pymonet.validation import Validation

def test_valid_inputs():
    # Test when both values and errors are the same
    val1 = Validation(10, [])
    val2 = Validation(10, [])
    assert val1 == val2

    # Test when only values are different
    val3 = Validation(20, [])
    assert val1 != val3

    # Test when only errors are different
    val4 = Validation(10, ["Error"])
    assert val1 != val4

    # Test when both values and errors are different
    val5 = Validation(20, ["Error"])
    assert val3 != val5
