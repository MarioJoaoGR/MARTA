
import pytest
from pymonet.maybe import Maybe
from pymonet.either import Left, Right

def test_valid_input():
    maybe = Maybe(value=42, is_nothing=False)
    either = maybe.to_either()
    
    assert isinstance(either, Right)
    assert either.value == 42

def test_empty_input():
    maybe = Maybe(value=None, is_nothing=True)
    either = maybe.to_either()
    
    assert isinstance(either, Left)
    assert either.value is None
