
import pytest
from pymonet.either import Left, Right
from pymonet.validation import Validation

def test_valid_input():
    right_instance = Right("success message")
    validation = right_instance.to_validation()
    assert isinstance(validation, Validation)
    assert validation.is_success() is True
    assert validation.value == "success message"
