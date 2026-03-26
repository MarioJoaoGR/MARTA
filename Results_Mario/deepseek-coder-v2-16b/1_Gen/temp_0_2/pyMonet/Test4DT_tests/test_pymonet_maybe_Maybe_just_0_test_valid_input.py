
import pytest
from pymonet.maybe import Maybe

def test_valid_input():
    # Test creating a not empty Maybe object
    maybe = Maybe.just(42)
    
    assert isinstance(maybe, Maybe)
    assert maybe.is_nothing is False
    assert maybe.value == 42
