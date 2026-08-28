
import pytest
from pymonet.maybe import Maybe

# Scenario 1: Test standard input with valid applicative
def test_valid_applicative():
    maybe_some = Maybe(value=lambda x: x + 1, is_nothing=False)
    maybe_some_arg = Maybe(value=42, is_nothing=False)
    
    result = maybe_some.ap(maybe_some_arg)
    assert not result.is_nothing
    assert result.value == 43

# Scenario 2: Test with empty applicative
def test_empty_applicative():
    maybe_none = Maybe(value=None, is_nothing=True)
    maybe_some_arg = Maybe(value=42, is_nothing=False)
    
    result = maybe_none.ap(maybe_some_arg)
    assert result.is_nothing

# Scenario 3: Test with invalid input type for applicative
def test_invalid_input():
    maybe_none = Maybe(value=None, is_nothing=True)
    maybe_invalid = Maybe(value='not a function', is_nothing=False)
    
    result = maybe_none.ap(maybe_invalid)
    assert result.is_nothing
