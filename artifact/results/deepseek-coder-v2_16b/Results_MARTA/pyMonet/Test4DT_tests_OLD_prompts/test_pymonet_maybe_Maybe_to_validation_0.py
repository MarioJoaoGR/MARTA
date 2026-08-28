
import pytest
from pymonet.maybe import Maybe
from pymonet.validation import Validation

def test_valid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    validation = maybe_some.to_validation()
    assert isinstance(validation, Validation)
    assert validation.is_success() is True
    assert validation.value == 42

def test_invalid_input():
    maybe_none = Maybe(value=None, is_nothing=True)
    validation = maybe_none.to_validation()
    assert isinstance(validation, Validation)
    assert validation.is_success() is True
    assert validation.value is None
