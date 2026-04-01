
import pytest
from pymonet.utils import curried_filter

def test_valid_input():
    def is_even(n):
        return n % 2 == 0
    
    assert curried_filter(is_even, [1, 2, 3, 4]) == [2, 4]
    assert curried_filter(is_even, [2, 4, 6, 8]) == [2, 4, 6, 8]
    assert curried_filter(is_even, [1, 3, 5, 7]) == []
    
    def starts_with_a(s):
        return s.startswith('a')
    
    assert curried_filter(starts_with_a, ['apple', 'banana', 'apricot']) == ['apple', 'apricot']
    assert curried_filter(starts_with_a, ['ball', 'cat', 'dog']) == []
