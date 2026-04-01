
import pytest
from pymonet.utils import eq

def test_valid_inputs():
    # Test cases for valid inputs
    assert eq(5, 5) == True
    assert eq("hello", "world") == False
    assert eq([1, 2], [1, 2]) == True
    assert eq(None, None) == True
