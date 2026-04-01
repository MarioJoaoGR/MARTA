
import pytest
from pymonet.maybe import Maybe
from pymonet.either import Left, Right

def test_invalid_input():
    # Test invalid input where value is None and is_nothing is True
    maybe = Maybe(value=None, is_nothing=True)
    either = maybe.to_either()
    
    assert isinstance(either, Left)
    assert either.value is None

    # Test invalid input where value is not None and is_nothing is False
    maybe = Maybe(value="Hello", is_nothing=False)
    either = maybe.to_either()
    
    assert isinstance(either, Right)
    assert either.value == "Hello"
