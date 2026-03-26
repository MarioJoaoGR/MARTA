
import pytest
from flutes.iterator import drop_until
from typing import Callable, Iterable, Iterator, TypeVar

T = TypeVar('T')

def pred_fn(x): return x > 5

def test_valid_input():
    assert list(drop_until(pred_fn, [1, 2, 3, 4, 5, 6, 7, 8, 9])) == [6, 7, 8, 9]
    assert list(drop_until(pred_fn, [6, 7, 8, 9, 10])) == [6, 7, 8, 9, 10]
    assert list(drop_until(pred_fn, [])) == []
    assert list(drop_until(pred_fn, [5, 4, 3, 2, 1])) == []
