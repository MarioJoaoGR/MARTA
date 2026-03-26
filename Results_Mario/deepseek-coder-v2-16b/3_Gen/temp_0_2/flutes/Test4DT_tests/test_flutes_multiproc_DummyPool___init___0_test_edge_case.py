
import multiprocessing as mp
from flutes.multiproc import DummyPool
import pytest

@pytest.mark.parametrize("processes", [0])
def test_edge_case(processes):
    pool = DummyPool(processes=processes)
    assert pool._state == mp.pool.RUN
