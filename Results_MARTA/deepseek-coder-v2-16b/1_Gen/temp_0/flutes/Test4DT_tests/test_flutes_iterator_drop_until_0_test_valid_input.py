
import pytest
from typing import Callable, Iterable, Iterator
from flutes.iterator import drop_until

def test_valid_input():
    # Test case where the predicate is satisfied after some elements
    pred_fn = lambda x: x > 5
    iterable = [3, 4, 6, 7, 8]
    expected_output = [6, 7, 8]
    
    result = list(drop_until(pred_fn, iterable))
    assert result == expected_output
