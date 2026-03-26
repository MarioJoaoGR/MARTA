
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_valid_inputs():
    pool = DummyPool(processes=0)
    assert isinstance(pool, DummyPool)
    
    def add(a, b):
        return a + b
    
    results = pool.starmap(add, [(1, 2), (3, 4)])
    assert results == [3, 7]
