
import pytest
from pymonet.validation import Validation

def test_is_success():
    # Test when there are no errors
    val = Validation("Success", [])
    assert val.is_success() == True

    # Test when there are errors
    val = Validation(None, ["Error occurred"])
    assert val.is_success() == False
