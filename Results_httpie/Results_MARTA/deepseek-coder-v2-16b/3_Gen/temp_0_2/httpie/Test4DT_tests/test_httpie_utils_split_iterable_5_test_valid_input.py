
import pytest
from typing import List, Tuple, Iterable, Callable, TypeVar
from unittest.mock import patch

T = TypeVar('T')

def split_iterable(iterable: Iterable[T], key: Callable[[T], bool]) -> Tuple[List[T], List[T]]:
    left, right = [], []
    for item in iterable:
        if key(item):
            left.append(item)
        else:
            right.append(item)
    return left, right

def test_valid_input():
    # Test with a list of numbers and a lambda function to check for even numbers
    result = split_iterable([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
    assert result == ([2, 4], [1, 3, 5])
    
    # Test with a list of strings and a lambda function to check the length of strings
    result = split_iterable(['apple', 'banana', 'cherry'], lambda x: len(x) > 5)
    assert result == (['banana', 'cherry'], ['apple'])
    
    # Test with an empty list, should return two empty lists
    result = split_iterable([], lambda x: True)
    assert result == ([], [])
