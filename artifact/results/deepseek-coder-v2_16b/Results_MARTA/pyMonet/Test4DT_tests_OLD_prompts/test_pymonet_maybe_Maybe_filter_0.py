
import pytest
from pymonet.maybe import Maybe

def test_valid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    assert not maybe_some.is_nothing
    assert maybe_some.value == 42

def test_invalid_input():
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing
    with pytest.raises(AttributeError):
        maybe_none.value

def test_filter_with_valid_value():
    maybe_some = Maybe(value=42, is_nothing=False)
    
    def filterer(x):
        return x > 0
    
    filtered_maybe = maybe_some.filter(filterer)
    assert not filtered_maybe.is_nothing
    assert filtered_maybe.value == 42

def test_filter_with_invalid_value():
    maybe_some = Maybe(value=42, is_nothing=False)
    
    def filterer(x):
        return x < 0
    
    filtered_maybe = maybe_some.filter(filterer)
    assert filtered_maybe.is_nothing
    with pytest.raises(AttributeError):
        filtered_maybe.value

def test_filter_with_none():
    maybe_none = Maybe(value=None, is_nothing=True)
    
    def filterer(x):
        return x > 0
    
    filtered_maybe = maybe_none.filter(filterer)
    assert filtered_maybe.is_nothing
    with pytest.raises(AttributeError):
        filtered_maybe.value
