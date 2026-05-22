
import pytest
from typing import List, Iterable, Tuple, Callable, TypeVar
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

def test_edge_case_empty_list():
    with patch('builtins.len', side_effect=lambda x: len([1, 2, 3])):
        result = split_iterable([], lambda x: True)
        assert result == ([], [])
