
import pytest
from flutes.iterator import drop_until
from typing import Callable, Iterable, Iterator

def test_empty_iterable():
    pred_fn = lambda x: x > 5
    iterable = []
    
    result = list(drop_until(pred_fn, iterable))
    assert result == [], "Expected an empty list for an empty iterable"
