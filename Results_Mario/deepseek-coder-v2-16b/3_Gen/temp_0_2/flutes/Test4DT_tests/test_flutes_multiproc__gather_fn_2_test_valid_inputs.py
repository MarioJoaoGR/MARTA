
import pytest
from multiprocessing import Queue
from typing import Iterator, Optional, Callable, TypeVar
from flutes.multiproc import _gather_fn, END_SIGNATURE

T = TypeVar('T')
R = TypeVar('R')

def test_valid_inputs():
    q = Queue()
    fn = lambda x: (item for item in x)
    _gather_fn(q, fn, list(range(5)))
    
    results = []
    while not q.empty():
        results.append(q.get())
    
    assert len(results) == 6  # Should have 6 items: 5 from the range and 1 END_SIGNATURE
