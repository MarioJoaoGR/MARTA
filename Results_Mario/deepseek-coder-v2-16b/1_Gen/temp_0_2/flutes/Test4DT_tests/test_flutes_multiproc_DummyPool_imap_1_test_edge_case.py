
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_edge_case():
    # Test with None input
    pool = DummyPool(processes=0)
    with pytest.raises(TypeError):
        list(pool.imap(lambda x: x * 2, None))
    
    # Test with empty list input
    pool = DummyPool(processes=0)
    assert list(pool.imap(lambda x: x * 2, [])) == []
