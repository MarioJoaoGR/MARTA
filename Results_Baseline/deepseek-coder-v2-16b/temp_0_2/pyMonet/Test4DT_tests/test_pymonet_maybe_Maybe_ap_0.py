
# Module: pymonet.maybe
import pytest
from pymonet.maybe import Maybe

# Test creating an instance with a value
def test_create_instance_with_value():
    maybe_some = Maybe(value=42, is_nothing=False)  # Creates a Maybe with a value of 42
    assert not maybe_some.is_nothing
    assert maybe_some.value == 42

# Test creating an instance representing nothing
def test_create_instance_representing_nothing():
    maybe_none = Maybe(value=None, is_nothing=True)  # Creates a Maybe representing nothing
    assert maybe_none.is_nothing
    with pytest.raises(AttributeError):
        print(maybe_none.value)  # Should raise AttributeError

# Test checking if the Maybe has a value
def test_check_if_maybe_has_a_value():
    maybe_some = Maybe(value=42, is_nothing=False)  # Creates a Maybe with a value of 42
    assert not maybe_some.is_nothing
    
    maybe_none = Maybe(value=None, is_nothing=True)  # Creates a Maybe representing nothing
    assert maybe_none.is_nothing

# Test accessing the contained value
def test_accessing_the_contained_value():
    maybe_some = Maybe(value=42, is_nothing=False)  # Creates a Maybe with a value of 42
    assert maybe_some.value == 42
    
    maybe_none = Maybe(value=None, is_nothing=True)  # Creates a Maybe representing nothing
    with pytest.raises(AttributeError):
        print(maybe_none.value)  # Should raise AttributeError

# Test applying a function contained within the Maybe to another applicative type
def test_applying_a_function_contained_within_the_maybe():
    maybe_some = Maybe(value=lambda x: x + 1, is_nothing=False)
    result = maybe_some.ap(Maybe(value=5, is_nothing=False))