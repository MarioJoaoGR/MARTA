
import pytest
from pymonet.maybe import Maybe

def test_valid_input():
    maybe = Maybe(value=lambda x: x + 1, is_nothing=False)
    applicative = Maybe(value=42, is_nothing=False)
    
    result = maybe.ap(applicative)
    
    assert not result.is_nothing
    assert result.value == 43
