# Module: pymonet.maybe
import pytest
from pymonet.maybe import Maybe

# Test creating a Maybe with a value
def test_maybe_with_value():
    maybe_some = Maybe(value=42, is_nothing=False)  # Creates a Maybe with the value 42.
    assert not maybe_some.is_nothing
    assert maybe_some.value == 42

# Test creating a Maybe that represents nothing
def test_maybe_none():
    maybe_none = Maybe(value=None, is_nothing=True)  # Creates a Maybe that represents nothing.
    assert maybe_none.is_nothing
    with pytest.raises(AttributeError):
        print(maybe_none.value)  # This should raise an AttributeError since it's not present.

# Test applying a function to the contained value if it exists
def test_map_function():
    maybe_some = Maybe(value=42, is_nothing=False)  # Creates a Maybe with the value 42.
    def double_value(x): return x * 2
    doubled_maybe = maybe_some.map(double_value)
    assert not doubled_maybe.is_nothing
    assert doubled_maybe.value == 84

# Test filtering based on a provided function
def test_filter_function():
    maybe_some = Maybe(value=42, is_nothing=False)  # Creates a Maybe with the value 42.
    filtered_maybe = maybe_some.filter(lambda x: x > 50)
    assert filtered_maybe.is_nothing
    with pytest.raises(AttributeError):
        print(filtered_maybe.value)  # This should raise an AttributeError since it's not present.
