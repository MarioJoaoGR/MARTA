
import pytest
from pymonet.maybe import Maybe
from pymonet.either import Left, Right

def test_to_either():
    maybe_none = Maybe(value=None, is_nothing=True)
    maybe_true = Maybe(value='Hello', is_nothing=False)
    
    # Test case for None value in Maybe
    assert maybe_none.to_either() == Left(None)
    
    # Test case for non-None value in Maybe
    assert maybe_true.to_either() == Right('Hello')
