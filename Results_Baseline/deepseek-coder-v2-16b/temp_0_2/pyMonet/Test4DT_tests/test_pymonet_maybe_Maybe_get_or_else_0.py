
import pytest
from pymonet.maybe import Maybe

# Test creating a Maybe instance with a value and checking its attributes
def test_create_maybe_with_value():
    maybe = Maybe(value=42, is_nothing=False)
    assert maybe.is_nothing == False
    assert maybe.value == 42

# Test creating a Maybe instance representing nothing and checking its attribute
def test_create_maybe_representing_nothing():
    maybe = Maybe(value=None, is_nothing=True)
    assert maybe.is_nothing == True
    with pytest.raises(AttributeError):
        print(maybe.value)  # This should raise an AttributeError

# Test accessing the value when Maybe is not empty
def test_access_value_when_not_empty():
    maybe = Maybe(value=42, is_nothing=False)
    assert maybe.get_or_else(default_value=0) == 42

# Test returning default value when Maybe is empty
def test_return_default_value_when_empty():
    maybe = Maybe(value=None, is_nothing=True)
    assert maybe.get_or_else(default_value=0) == 0

# Test function that uses Maybe to handle optional values
def test_maybe_function():
    result = maybe_function(42)
    assert result.is_nothing == False
    assert result.value == 84

    result_none = maybe_function(None)
    assert result_none.is_nothing == True
    with pytest.raises(AttributeError):
        print(result_none.value)  # This should raise an AttributeError

# Helper function for testing Maybe with a function
def maybe_function(input_value):
    if input_value is None:
        return Maybe(value=None, is_nothing=True)
    else:
        return Maybe(value=input_value * 2, is_nothing=False)
