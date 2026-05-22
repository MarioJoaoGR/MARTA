
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

def test_edge_case_empty_list():
    with patch('builtins.print') as mock_print:
        result = split_iterable([], lambda x: x % 2 == 0)
        assert result == ([], [])
        mock_print.assert_not_called()
