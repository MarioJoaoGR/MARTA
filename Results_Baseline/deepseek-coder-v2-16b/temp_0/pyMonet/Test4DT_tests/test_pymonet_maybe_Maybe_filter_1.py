
import pytest
from pymonet.maybe import Maybe

# Test creating a Maybe with a value
def test_create_maybe_with_value():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42

# Test creating a Maybe that represents nothing
def test_create_maybe_that_represents_nothing():
    maybe = Maybe(value=None, is_nothing=True)
    assert maybe.is_nothing

# Test filter with filterer function returning True
def test_filter_with_filterer_true():
    maybe = Maybe(value=42, is_nothing=False)
    result = maybe.filter(lambda x: isinstance(x, int))
    assert not result.is_nothing
    assert result.value == 42

# Test filter with filterer function returning False
def test_filter_with_filterer_false():
    maybe = Maybe(value=42, is_nothing=False)
    result = maybe.filter(lambda x: not isinstance(x, int))
    assert result.is_nothing