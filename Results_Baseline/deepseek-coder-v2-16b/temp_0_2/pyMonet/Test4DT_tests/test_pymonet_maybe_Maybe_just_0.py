
import pytest
from pymonet.maybe import Maybe

# Test creating a Maybe with a value
def test_create_maybe_with_value():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42

# Test creating a Maybe representing nothing
def test_create_maybe_representing_nothing():
    maybe = Maybe(value=None, is_nothing=True)
    assert maybe.is_nothing
    with pytest.raises(AttributeError):
        print(maybe.value)  # This should raise an AttributeError

# Test checking if the Maybe has a value
def test_check_if_maybe_has_value():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    
    maybe_none = Maybe(value=None, is_nothing=True)