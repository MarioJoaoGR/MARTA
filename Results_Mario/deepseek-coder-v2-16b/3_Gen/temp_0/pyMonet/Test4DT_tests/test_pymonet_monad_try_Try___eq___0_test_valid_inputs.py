
import pytest
from pymonet.monad_try import Try

def test_valid_inputs():
    # Test equality with another Try object of the same value and success status
    try1 = Try(42, True)
    try2 = Try(42, True)
    assert try1 == try2
    
    # Test inequality with a different Try object (different value or success status)
    try3 = Try("error", False)
    assert not try1 == try3
    
    # Test equality with the same Try object
    assert try1 == try1
    
    # Test equality with an instance of a subclass
    class SubTry(Try):
        pass
    sub_try = SubTry(42, True)
    assert not (try1 == sub_try)  # Should be False because the types are different
