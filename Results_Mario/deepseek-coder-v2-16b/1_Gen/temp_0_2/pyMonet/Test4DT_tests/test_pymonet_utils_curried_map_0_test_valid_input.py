
import pytest
from pymonet.utils import curried_map

def test_valid_input():
    # Test case where the mapper is a lambda function multiplying each element by 2
    result = curried_map(lambda x: x * 2, [1, 2, 3])
    assert result == [2, 4, 6]
