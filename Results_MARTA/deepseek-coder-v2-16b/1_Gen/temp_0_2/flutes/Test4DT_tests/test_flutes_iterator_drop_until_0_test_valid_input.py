
import pytest
from flutes.iterator import drop_until
from typing import Callable, Iterable, Iterator

def test_valid_input():
    pred_fn = lambda x: x > 5
    iterable = range(10)
    
    result = list(drop_until(pred_fn, iterable))
    assert result == [6, 7, 8, 9]
