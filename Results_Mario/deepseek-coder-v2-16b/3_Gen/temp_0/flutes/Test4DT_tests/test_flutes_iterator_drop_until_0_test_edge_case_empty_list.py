
import pytest
from flutes.iterator import drop_until
from typing import Callable, Iterable, Iterator, TypeVar

T = TypeVar('T')

def test_edge_case_empty_list():
    # Test with an empty list as input
    result = list(drop_until(lambda x: x > 5, []))
    assert result == [], "Expected an empty list when the iterable is empty"
