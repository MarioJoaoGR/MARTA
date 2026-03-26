
# Module: pymonet.maybe
import pytest
from pymonet.maybe import Maybe

# Test creating a Maybe with a value
def test_create_maybe_with_value():
    maybe = Maybe(value=42, is_nothing=False)  # Creates a Maybe with the value 42.
    assert not maybe.is_nothing
    assert maybe.value == 42

# Test creating a Maybe that represents nothing
def test_create_maybe_with_nothing():
    maybe = Maybe(value="Hello", is_nothing=True)  # Creates a Maybe that represents nothing.
    assert maybe.is_nothing
    with pytest.raises(AttributeError):
        maybe.value  # This should raise an AttributeError because the value attribute does not exist when is_nothing is True.

# Test mapping a function over the contained value
def test_map_function_over_maybe():
    def double_value(x): return x * 2
    maybe = Maybe(value=42, is_nothing=False)
    mapped_maybe = maybe.map(double_value)
    assert not mapped_maybe.is_nothing
    assert mapped_maybe.value == 84

# Test mapping a function over an empty Maybe
def test_map_function_over_empty_maybe():
    def double_value(x): return x * 2
    maybe = Maybe(value=None, is_nothing=True)
    mapped_maybe = maybe.map(double_value)
    assert mapped_maybe.is_nothing