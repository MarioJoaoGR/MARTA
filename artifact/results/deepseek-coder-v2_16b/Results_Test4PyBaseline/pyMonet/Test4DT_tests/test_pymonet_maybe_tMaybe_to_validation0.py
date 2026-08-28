# Module: pymonet.maybe
# test_maybe.py
from pymonet.maybe import Maybe
import pytest

@pytest.fixture
def maybe_some():
    return Maybe(value=42, is_nothing=False)

@pytest.fixture
def maybe_nothing():
    return Maybe(value=None, is_nothing=True)

def test_to_validation_with_value(maybe_some):
    validation = maybe_some.to_validation()
    assert validation.value == 42

def test_to_validation_empty(maybe_nothing):
    validation = maybe_nothing.to_validation()
    assert validation.value is None
