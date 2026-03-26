
import pytest
from pymonet.utils import identity

def test_valid_input():
    # Test with integer input
    assert identity(5) == 5
    
    # Test with string input
    assert identity("hello") == "hello"
    
    # Test with list input
    assert identity([1, 2, 3]) == [1, 2, 3]
    
    # Test with dictionary input
    assert identity({"key": "value"}) == {"key": "value"}
    
    # Test with float input
    assert identity(3.14) == 3.14
