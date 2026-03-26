
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_valid_inputs():
    pool = DummyPool(processes=0)
    results = list(pool.gather(lambda x: [x * 2], range(5)))
    assert results == [0, 2, 4, 6, 8]
