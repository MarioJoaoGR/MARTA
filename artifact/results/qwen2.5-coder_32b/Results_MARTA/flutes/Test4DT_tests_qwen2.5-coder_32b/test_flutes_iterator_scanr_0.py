
import pytest
from flutes.iterator import scanr


def test_scanr_with_single_element():
    # Test with a single element
    result = scanr(lambda x, y: x + y, [1])
    assert result == [1]


def test_scanr_with_numbers_sum():
    # Test with numbers using sum
    result = scanr(lambda x, y: x + y, [1, 2, 3, 4])
    assert result == [10, 9, 7, 4]


def test_scanr_with_max():
    # Test with max
    result = scanr(max, [3, 1, 4, 1, 5, 9, 2, 6, 5])
    assert result == [9, 9, 9, 9, 9, 9, 6, 6, 5]

def test_scanr_with_product():
    # Test with product
    from operator import mul
    result = scanr(mul, [1, 2, 3, 4])
    assert result == [24, 24, 12, 4]