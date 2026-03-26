# Module: pymonet.maybe
import pytest
from pymonet.maybe import Maybe
from pymonet.either import Left, Right

# Test creating an instance of Maybe with a value
def test_maybe_with_value():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42

# Test creating an instance of Maybe representing nothing
def test_maybe_representing_nothing():
    maybe = Maybe(value=None, is_nothing=True)
    assert maybe.is_nothing
    with pytest.raises(AttributeError):
        print(maybe.value)  # This should raise an AttributeError

# Test transforming Maybe to Either when it has a value
def test_transform_to_either_with_value():
    maybe = Maybe(value=42, is_nothing=False)
    either_instance = maybe.to_either()
    assert isinstance(either_instance, Right)
    assert either_instance.value == 42

# Test transforming Maybe to Either when it represents nothing
def test_transform_to_either_representing_nothing():
    maybe = Maybe(value=None, is_nothing=True)
    either_instance = maybe.to_either()
    assert isinstance(either_instance, Left)
    assert either_instance.value is None
