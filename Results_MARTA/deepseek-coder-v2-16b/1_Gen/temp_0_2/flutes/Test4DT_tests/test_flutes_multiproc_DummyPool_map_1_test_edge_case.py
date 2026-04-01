
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_edge_case():
    pool = DummyPool(processes=0)
    
    # Test with an empty iterable
    result = list(pool.imap(lambda x: x, []))
    assert result == []

    # Test with a non-empty iterable but no processes
    result = list(pool.imap(lambda x: x, [1, 2, 3]))
    assert result == [1, 2, 3]
