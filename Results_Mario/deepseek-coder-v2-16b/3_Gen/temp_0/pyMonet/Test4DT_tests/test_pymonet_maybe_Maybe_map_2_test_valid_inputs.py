
import pytest
from pymonet.maybe import Maybe

def test_valid_inputs():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42
    
    mapped_value = maybe.map(lambda x: x * 2)
    assert not mapped_value.is_nothing
    assert mapped_value.value == 84
