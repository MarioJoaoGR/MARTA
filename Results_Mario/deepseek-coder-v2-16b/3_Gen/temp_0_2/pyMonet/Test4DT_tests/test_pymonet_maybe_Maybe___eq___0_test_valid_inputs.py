
import pytest
from pymonet.maybe import Maybe

def test_valid_inputs():
    maybe1 = Maybe(value=42, is_nothing=False)
    maybe2 = Maybe(value=None, is_nothing=True)
    another_maybe = Maybe(value=42, is_nothing=False)
    
    assert maybe1 == maybe1
    assert maybe1 == another_maybe
    assert not (maybe1 == maybe2)
