
import pytest
from typing import Iterable, List, Tuple, Callable, TypeVar

T = TypeVar('T')

def split_iterable(iterable: Iterable[T], key: Callable[[T], bool]) -> Tuple[List[T], List[T]]:
    left, right = [], []
    for item in iterable:
        if key(item):
            left.append(item)
        else:
            right.append(item)
    return left, right

def test_invalid_input():
    with pytest.raises(TypeError):
        split_iterable("not an iterable", lambda x: x % 2 == 0)
