
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator

def test_edge_case_empty_list():
    # Test that scanl returns an iterator when given an empty list
    func = lambda x, y: x + y
    iterable = []
    
    result = scanl(func, iterable)
    
    assert isinstance(result, Iterator)
