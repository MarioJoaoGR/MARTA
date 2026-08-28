
import pytest
from pymonet.utils import find
from typing import List, Optional, Callable, TypeVar

T = TypeVar('T')



def test_find_match():
    numbers = [1, 2, 3, 4, 5]
    is_even = lambda x: x % 2 == 0
    assert find(numbers, is_even) == 2

def test_empty_collection():
    collection: List[int] = []
    key = lambda x: x > 0
    assert find(collection, key) is None