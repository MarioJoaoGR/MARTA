
import pytest
from unittest.mock import patch
from pymonet.monad_try import Try

# Test for the basic functionality of the Try class
def test_Try_basic():
    # Initialize a successful Try instance
    try1 = Try(42, True)
    
    # Check if the initialization is correct
    assert try1.value == 42
    assert try1.is_success == True
    
    # Test the map method with a simple function (doubling the value)
    def double(x):
        return x * 2
    
    mapped_try = try1.map(double)
    assert mapped_try.value == 84
    assert mapped_try.is_success == True
    
    # Initialize a failed Try instance
    try2 = Try("error", False)
    
    # Check if the initialization is correct
    assert try2.value == "error"
    assert try2.is_success == False
    
    # Test the map method on a failed instance, it should return itself
    mapped_try_failed = try2.map(double)
    assert mapped_try_failed.value == "error"
    assert mapped_try_failed.is_success == False

# Additional tests can be added here following the same structure and logic
