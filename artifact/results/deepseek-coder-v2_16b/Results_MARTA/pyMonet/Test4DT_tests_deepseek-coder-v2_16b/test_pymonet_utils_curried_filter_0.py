
import pytest
from pymonet.utils import curried_filter

# Test valid input where filterer is a callable and collection is an iterable
def test_valid_input():
    def is_even(n):
        return n % 2 == 0
    filtered_list = curried_filter(is_even, [1, 2, 3, 4])
    assert filtered_list == [2, 4]

# Test invalid input where filterer is not callable and collection is an iterable
def test_invalid_input():
    with pytest.raises(TypeError):
        curried_filter(42, [1])

# Test edge case where filterer is a callable but collection is not iterable
def test_edge_case():
    def is_even(n):
        return n % 2 == 0
    with pytest.raises(TypeError):
        curried_filter(is_even, None)
