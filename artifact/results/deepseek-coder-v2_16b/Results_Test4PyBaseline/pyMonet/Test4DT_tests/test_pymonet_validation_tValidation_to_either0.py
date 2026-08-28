# Module: pymonet.validation
import pytest
from pymonet.validation import Validation
from pymonet.either import Left, Right

# Test initialization with a value and no errors
def test_initialization_with_value_and_no_errors():
    val = Validation(10, [])
    assert val.value == 10
    assert val.errors == []

# Test initialization with None and an error list
def test_initialization_with_none_and_error_list():
    val = Validation(None, ['Error message'])
    assert val.value is None
    assert val.errors == ['Error message']

# Test checking if the validation is successful when it has no errors
def test_is_success_when_no_errors():
    val = Validation(10, [])
    assert val.is_success() is True

# Test checking if the validation is successful when it has errors
def test_is_success_when_has_errors():
    val = Validation(None, ['Error message'])
    assert val.is_success() is False

# Test transforming to Either type when there are no errors (should return Right)
def test_to_either_when_no_errors():
    val = Validation(10, [])
    result = val.to_either()
    assert isinstance(result, Right)
    assert result.value == 10

# Test transforming to Either type when there are errors (should return Left)
def test_to_either_when_has_errors():
    val = Validation(None, ['Error message'])
    result = val.to_either()
    assert isinstance(result, Left)
    assert result.value == ['Error message']
