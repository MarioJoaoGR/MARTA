
import pytest
from pymonet.maybe import Maybe

def test_invalid_input():
    maybe = Maybe(value=5, is_nothing=False)
    filtered_maybe = maybe.filter(lambda x: x < 0)  # This lambda always returns False
    
    assert filtered_maybe.is_nothing is True
