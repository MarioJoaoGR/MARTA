# Module: pymonet.either
# test_right.py
import pytest
from pymonet.either import Right
from pymonet.validation import Validation

def test_to_validation():
    right_instance = Right("success")
    validation_monad = right_instance.to_validation()
    assert isinstance(validation_monad, Validation)
    assert validation_monad.is_success()
    assert validation_monad.value == "success"

def test_to_validation_with_different_value():
    right_instance = Right(42)
    validation_monad = right_instance.to_validation()
    assert isinstance(validation_monad, Validation)
    assert validation_monad.is_success()
    assert validation_monad.value == 42

def test_to_validation_returns_successful_validation():
    from pymonet.validation import Validation

    right_instance = Right("success")
    validation_monad = right_instance.to_validation()
    assert isinstance(validation_monad, Validation)
    assert validation_monad.is_success()
    assert validation_monad.value == "success"

def test_integration_with_function():
    from pymonet.validation import Validation

    def some_function(data):
        return Right(data).to_validation()

    result = some_function("some data")
    assert isinstance(result, Validation)
    assert result.is_success()
    assert result.value == "some data"
