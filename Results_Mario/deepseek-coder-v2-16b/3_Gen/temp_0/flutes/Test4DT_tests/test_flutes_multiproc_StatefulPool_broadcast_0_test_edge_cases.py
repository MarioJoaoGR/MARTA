
import pytest
from multiprocessing import Pool, TimeoutError
from flutes.multiproc import StatefulPool

# Assuming that stateful_pool is a valid module containing the necessary classes and functions
try:
    from stateful_pool import State, StatefulPool  # Adjust this import based on your actual module path
except ImportError:
    pytestmark = pytest.mark.skip(reason="stateful_pool module not available")

@pytest.fixture
def setup_stateful_pool():
    pool_class = Pool
    state_class = State  # Adjust this based on your actual implementation
    args = ()
    kwargs = {}
    return StatefulPool(pool_class, state_class, (), args, kwargs)

def test_broadcast(setup_stateful_pool):
    pool = setup_stateful_pool
    
    def fn(state):
        return sum([1, 2, 3])

    results = pool.broadcast(fn, args=((),), kwds={})
    assert len(results) == 4  # Assuming the pool has 4 processes
    for result in results:
        assert result == 6
