
import pytest
from flutes.iterator import chunk
from typing import List, Iterable

def test_empty_iterable():
    iterable = []
    n = 3
    result = list(chunk(n, iterable))
    assert result == [], f"Expected an empty list but got {result}"
