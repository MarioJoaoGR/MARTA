
import pytest
from pymonet.validation import Validation
from pymonet.either import Left

def test_to_validation():
    left_instance = Left(value="error")
    validation_result = left_instance.to_validation()
    assert isinstance(validation_result, Validation)
    assert validation_result.is_fail()
    assert validation_result.errors == ["error"]
