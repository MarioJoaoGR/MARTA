
import multiprocessing as mp
from flutes.multiproc import DummyPool

def test_edge_case():
    pool = DummyPool(processes=0)
    assert pool._state == mp.pool.RUN
    
    with pool:
        pass  # No tasks to run, just checking the state changes on exit
    
    assert pool._state == mp.pool.TERMINATE
