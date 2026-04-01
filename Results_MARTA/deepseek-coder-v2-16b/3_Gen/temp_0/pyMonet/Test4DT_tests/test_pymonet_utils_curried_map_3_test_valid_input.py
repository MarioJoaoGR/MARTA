
import pytest
from pymonet.utils import curried_map

def test_valid_input():
    # Define a simple mapper function
    def square(x):
        return x ** 2
    
    # Test case with list of numbers
    assert curried_map(square, [1, 2, 3, 4]) == [1, 4, 9, 16]
    
    # Define another mapper function
    def to_uppercase(s):
        return s.upper()
    
    # Test case with list of strings
    assert curried_map(to_uppercase, ['hello', 'world']) == ['HELLO', 'WORLD']
