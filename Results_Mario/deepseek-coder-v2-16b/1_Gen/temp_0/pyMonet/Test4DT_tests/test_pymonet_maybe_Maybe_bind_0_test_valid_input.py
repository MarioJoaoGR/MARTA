
import pytest
from pymonet.maybe import Maybe

def test_valid_input():
    maybe = Maybe(value=42, is_nothing=False)
    def double_value(x): return Maybe(value=x * 2, is_nothing=False)
    
    # Test that bind with a valid mapper function returns the expected result
    doubled_maybe = maybe.bind(double_value)
    assert not doubled_maybe.is_nothing
    assert doubled_maybe.value == 84
    
    # Test that bind with an empty Maybe returns Nothing
    another_maybe = Maybe(value="Hello", is_nothing=True)
    no_value_maybe = another_maybe.bind(double_value)
    assert no_value_maybe.is_nothing
