
import pytest
from flutes.iterator import scanr

def test_scanr():
    # Test case for valid input
    result = list(scanr(lambda s, x: x + s, ['a', 'b', 'c', 'd']))
    assert result == ['abcd', 'bcd', 'cd', 'd']
    
    # Additional test cases can be added here to ensure the function works correctly for different inputs and functions.
