
import pytest
from flutes.multiproc import DummyPool
import multiprocessing as mp

def test_valid_inputs():
    # Test initialization with valid parameters
    pool = DummyPool(processes=0)
    assert pool._process_state is None
    assert pool._state == mp.pool.RUN  # Assuming mp.pool.RUN is represented by the value 1 in your implementation
