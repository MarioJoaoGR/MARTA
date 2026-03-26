
import pytest
from pymonet.either import Right
from pymonet.validation import Validation

def test_right_to_validation():
    right = Right(value="test_value")
    validation = right.to_validation()
    
    assert isinstance(validation, Validation)
    assert validation.is_success()
    assert validation.value == "test_value"
