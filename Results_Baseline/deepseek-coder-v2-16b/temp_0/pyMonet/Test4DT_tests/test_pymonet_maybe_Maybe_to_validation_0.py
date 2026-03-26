
# Module: pymonet.maybe
import pytest
from pymonet.maybe import Maybe
from pymonet.validation import Validation

# Test initialization of Maybe with a value and is_nothing=False
def test_maybe_init_with_value():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42

# Test initialization of Maybe with is_nothing=True
def test_maybe_init_with_is_nothing():
    maybe = Maybe(value=None, is_nothing=True)
    assert maybe.is_nothing