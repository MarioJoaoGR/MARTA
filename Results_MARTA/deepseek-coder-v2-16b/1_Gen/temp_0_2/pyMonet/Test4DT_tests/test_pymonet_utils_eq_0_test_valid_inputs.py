
import pytest
from pymonet.utils import eq

def test_valid_inputs():
    # Test cases where values are equal
    assert eq(5, 5) == True
    assert eq("hello", "hello") == True
    assert eq(None, None) == True
    
    # Test cases where values are not equal
    assert eq(5, 10) == False
    assert eq("hello", "world") == False
    assert eq(True, False) == False
