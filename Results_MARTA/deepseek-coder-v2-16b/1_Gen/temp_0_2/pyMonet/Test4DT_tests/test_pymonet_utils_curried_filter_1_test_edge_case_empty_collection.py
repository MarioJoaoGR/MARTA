
import pytest
from pymonet.utils import curried_filter

def is_even(n):
    return n % 2 == 0

def test_edge_case_empty_collection():
    # Test with an empty collection
    result = curried_filter(is_even, [])
    assert result == []
