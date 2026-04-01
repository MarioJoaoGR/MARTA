
import pytest
from pymonet.maybe import Maybe

def test_valid_input():
    maybe = Maybe(value=42, is_nothing=False)
    filtered_maybe = maybe.filter(lambda x: x > 0)
    
    assert not filtered_maybe.is_nothing
    assert filtered_maybe.value == 42
