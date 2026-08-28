# Module: pymonet.maybe
import pytest
from pymonet.maybe import Maybe

# Test creating a Maybe with a value
def test_create_maybe_with_value():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42

# Test creating an empty Maybe
def test_create_empty_maybe():
    nothing = Maybe(value=None, is_nothing=True)
    assert nothing.is_nothing
    with pytest.raises(AttributeError):
        print(nothing.value)

# Test using the helper method to create an empty Maybe
def test_create_empty_maybe_using_helper():
    maybe_empty = Maybe.nothing()
    assert maybe_empty.is_nothing
    with pytest.raises(AttributeError):
        print(maybe_empty.value)

# Test checking if the Maybe contains a value and retrieving it safely
def test_check_and_retrieve_value():
    maybe = Maybe(value=42, is_nothing=False)
    if not maybe.is_nothing:
        assert maybe.value == 42
