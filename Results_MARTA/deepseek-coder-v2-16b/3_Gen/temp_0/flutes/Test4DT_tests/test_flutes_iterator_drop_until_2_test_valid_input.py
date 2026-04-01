
import pytest
from flutes.iterator import drop_until
from itertools import islice
from typing import Callable, Iterable, Iterator, TypeVar

T = TypeVar('T')

def pred(x): return x > 5
test_iterable = range(10)

def test_valid_input():
    result = list(drop_until(pred, test_iterable))
    assert result == [6, 7, 8, 9]
