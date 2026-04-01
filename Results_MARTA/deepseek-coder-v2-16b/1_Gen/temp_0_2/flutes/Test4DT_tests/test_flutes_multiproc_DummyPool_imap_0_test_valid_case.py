
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_valid_case():
    def process_item(x):
        return x * 2
    
    pool = DummyPool(processes=0)
    results = list(pool.imap(process_item, [1, 2, 3, 4]))
    
    assert results == [2, 4, 6, 8]
