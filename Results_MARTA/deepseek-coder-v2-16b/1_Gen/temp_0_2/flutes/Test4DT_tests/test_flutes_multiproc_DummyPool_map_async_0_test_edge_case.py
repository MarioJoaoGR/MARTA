
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool, DummyApplyResult

def test_edge_case():
    # Test None input
    pool = DummyPool(processes=0)
    with pytest.raises(TypeError):
        pool.map(lambda x: x * 2, None)
    
    # Test empty list input
    results = pool.map(lambda x: x * 2, [])
    assert results == []
    
    # Test boundary value input (e.g., a single element in the list)
    results = pool.map(lambda x: x * 2, [1])
    assert results == [2]
