
import pytest
from pymonet.utils import find



def test_single_match():
    numbers = [1, 2, 3, 4, 5]
    is_even = lambda x: x % 2 == 0
    result = find(numbers, is_even)
    assert result == 2

def test_multiple_matches():
    numbers = [1, 2, 3, 4, 5, 6]
    is_odd = lambda x: x % 2 != 0
    result = find(numbers, is_odd)
    assert result == 1