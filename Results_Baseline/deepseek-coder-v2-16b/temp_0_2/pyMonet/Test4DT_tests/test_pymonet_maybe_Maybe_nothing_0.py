# Module: pymonet.maybe
import pytest
from pymonet.maybe import Maybe

# Test creating a Maybe instance with a value
def test_maybe_with_value():
    maybe_some = Maybe(value=42, is_nothing=False)
    assert not maybe_some.is_nothing
    assert maybe_some.value == 42

# Test creating an empty Maybe instance
def test_empty_maybe():
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing
    with pytest.raises(AttributeError):
        print(maybe_none.value)  # This should raise an AttributeError

# Test checking if the Maybe has a value
def test_check_if_has_value():
    maybe_some = Maybe(value=42, is_nothing=False)
    assert not maybe_some.is_nothing

# Test accessing the contained value when it exists
def test_access_contained_value():
    maybe_some = Maybe(value=42, is_nothing=False)
    assert maybe_some.value == 42

# Test creating an empty Maybe instance using the `nothing` class method
def test_create_empty_maybe():
    maybe_none = Maybe.nothing()
    assert maybe_none.is_nothing
    with pytest.raises(AttributeError):
        print(maybe_none.value)  # This should raise an AttributeError
