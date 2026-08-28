# Module: pymonet.utils
import pytest
from pymonet.utils import curried_filter

# Test cases for curried_filter function

def test_curried_filter_even():
    def is_even(n):
        return n % 2 == 0
    
    numbers = [1, 2, 3, 4, 5]
    expected = [2, 4]
    result = curried_filter(is_even, numbers)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_curried_filter_startswith_a():
    def starts_with_a(s):
        return s.startswith('a')
    
    words = ['apple', 'banana', 'apricot']
    expected = ['apple', 'apricot']
    result = curried_filter(starts_with_a, words)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_curried_filter_lambda_even():
    numbers = [1, 2, 3, 4, 5]
    expected = [2, 4]
    result = curried_filter(lambda n: n % 2 == 0, numbers)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_curried_filter_lambda_startswith_a():
    words = ['apple', 'banana', 'apricot']
    expected = ['apple', 'apricot']
    result = curried_filter(lambda s: s.startswith('a'), words)
    assert result == expected, f"Expected {expected}, but got {result}"
