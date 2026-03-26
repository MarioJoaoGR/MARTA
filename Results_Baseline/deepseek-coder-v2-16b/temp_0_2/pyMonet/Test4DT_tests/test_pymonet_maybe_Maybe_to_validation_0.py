# Module: pymonet.maybe
import pytest
from pymonet.maybe import Maybe
from pymonet.validation import Validation

# Test initialization with a value
def test_init_with_value():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42

# Test initialization representing nothing
def test_init_representing_nothing():
    maybe = Maybe(value=None, is_nothing=True)
    assert maybe.is_nothing
    with pytest.raises(AttributeError):
        print(maybe.value)

# Test to_validation method when Maybe has a value
def test_to_validation_with_value():
    maybe = Maybe(value=42, is_nothing=False)
    validation = maybe.to_validation()
    assert isinstance(validation, Validation)
    assert validation.value == 42

# Test to_validation method when Maybe is empty
def test_to_validation_empty():
    maybe = Maybe(value=None, is_nothing=True)
    validation = maybe.to_validation()
    assert isinstance(validation, Validation)
    assert validation.value is None

# Test to_validation method when Maybe has a value after modification
def test_to_validation_after_modification():
    maybe = Maybe(value=42, is_nothing=False)
    maybe.is_nothing = True
    validation = maybe.to_validation()
    assert isinstance(validation, Validation)
    assert validation.value is None
