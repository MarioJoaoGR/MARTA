
import pytest
from pymonet.utils import curried_filter

# Test cases for the curried_filter function

def test_curried_filter_even_numbers():
    def is_even(n):
        return n % 2 == 0
    
    result = curried_filter(is_even, [1, 2, 3, 4])
    assert result == [2, 4]

def test_curried_filter_strings_longer_than_three_characters():
    result = curried_filter(lambda x: len(x) > 3, ['a', 'cat', 'bird', 'elephant'])