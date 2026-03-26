
import pytest
from pymonet.maybe import Maybe

# Test creating a Maybe with a value
def test_create_maybe_with_value():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42

# Test creating a Maybe that represents nothing
def test_create_maybe_representing_nothing():
    another_maybe = Maybe(value=None, is_nothing=True)
    assert another_maybe.is_nothing

# Test ap method with an empty Maybe
def test_ap_with_empty_maybe():
    maybe = Maybe(value=42, is_nothing=False)
    applicative = Maybe(value=None, is_nothing=True)
    result = maybe.ap(applicative)