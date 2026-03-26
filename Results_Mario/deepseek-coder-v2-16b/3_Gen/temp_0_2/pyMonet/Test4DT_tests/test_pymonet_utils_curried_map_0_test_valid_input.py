
import pytest
from pymonet.utils import curried_map

def test_valid_input():
    assert curried_map(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]
