
import pytest
from itertools import islice, count
import collections

def consume(iterator, n=None):
    """
    Efficiently advance an iterator n-steps ahead. If n is none, consume entirely.
    Consumes at C level (and therefore speed) in cpython.
    """
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)

def test_valid_input_none():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    
    consume(it)
    
    with pytest.raises(StopIteration):
        next(it)
