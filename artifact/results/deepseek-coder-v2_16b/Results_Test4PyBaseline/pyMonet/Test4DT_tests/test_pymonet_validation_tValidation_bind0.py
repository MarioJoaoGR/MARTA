# Module: pymonet.validation
import pytest
from pymonet.validation import Validation

# Test initialization of Validation class
def test_validation_initialization():
    val_success = Validation(10, [])
    assert val_success.value == 10
    assert val_success.errors == []

    val_failure = Validation(None, ['Error message'])
    assert val_failure.value is None
    assert val_failure.errors == ['Error message']

# Test bind method with a successful function
def test_bind_method_successful():
    def add_one(x):
        if x > 0:
            return Validation(x + 1, [])
        else:
            return Validation(None, ["Value must be positive"])

    val = Validation(5, [])
    result = val.bind(add_one)
    assert result.value == 6
    assert result.errors == []

# Test bind method with a failing function
def test_bind_method_failing():
    def add_one(x):
        if x > 0:
            return Validation(x + 1, [])
        else:
            return Validation(None, ["Value must be positive"])

    val = Validation(-1, [])
    result = val.bind(add_one)
    assert result.value is None
    assert result.errors == ['Value must be positive']

# Test bind method with a function that returns another Validation instance
def test_bind_method_returns_validation():
    class AnotherValidation:
        def __init__(self, value, errors):
            self.value = value
            self.errors = errors

        def bind(self, folder):
            return folder(self.value)

    def add_one(x):
        if x > 0:
            return AnotherValidation(x + 1, [])
        else:
            return AnotherValidation(None, ["Value must be positive"])

    val = AnotherValidation(5, [])
    result = val.bind(add_one)
    assert result.value == 6
    assert result.errors == []

# Test bind method with a function that returns another Validation instance and fails
def test_bind_method_returns_validation_failing():
    class AnotherValidation:
        def __init__(self, value, errors):
            self.value = value
            self.errors = errors

        def bind(self, folder):
            return folder(self.value)

    def add_one(x):
        if x > 0:
            return AnotherValidation(x + 1, [])
        else:
            return AnotherValidation(None, ["Value must be positive"])

    val = AnotherValidation(-1, [])
    result = val.bind(add_one)
    assert result.value is None
    assert result.errors == ['Value must be positive']
