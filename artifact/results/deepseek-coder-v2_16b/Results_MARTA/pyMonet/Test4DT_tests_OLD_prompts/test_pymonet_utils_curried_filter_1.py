
import pytest
from pymonet.utils import curried_filter

def test_curried_filter_with_valid_filterer():
    def is_even(n):
        return n % 2 == 0
    
    result = curried_filter(is_even, [1, 2, 3, 4])
    assert result == [2, 4]
