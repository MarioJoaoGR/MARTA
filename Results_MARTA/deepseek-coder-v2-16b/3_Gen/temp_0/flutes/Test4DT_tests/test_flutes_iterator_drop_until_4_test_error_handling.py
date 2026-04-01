
import pytest
from flutes.iterator import drop_until
from typing import Callable, Iterable, Iterator, TypeVar

T = TypeVar('T')

def test_error_handling():
    # Test with an empty iterable
    pred_fn = lambda x: x > 5
    iterable = []
    result = list(drop_until(pred_fn, iterable))
    assert result == [], "Expected an empty list for an empty iterable"

    # Test with a non-empty iterable where no element satisfies the predicate
    pred_fn = lambda x: x > 5
    iterable = [1, 2, 3, 4, 5]
    result = list(drop_until(pred_fn, iterable))
    assert result == [], "Expected an empty list for an iterable where no element satisfies the predicate"

    # Test with a non-empty iterable where some elements satisfy the predicate
    pred_fn = lambda x: x > 3
    iterable = [1, 2, 4, 5, 6]
    result = list(drop_until(pred_fn, iterable))
    assert result == [4, 5, 6], "Expected elements starting from the first element that satisfies the predicate"
