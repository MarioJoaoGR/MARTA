
import pytest
from pymonet.maybe import Maybe

def test_invalid_input():
    # Test that filter returns an empty Maybe when input is invalid
    maybe = Maybe(value=42, is_nothing=False)
    filterer = lambda x: False  # Always return False
    
    result = maybe.filter(filterer)
    assert isinstance(result, Maybe)
    assert result.is_nothing
