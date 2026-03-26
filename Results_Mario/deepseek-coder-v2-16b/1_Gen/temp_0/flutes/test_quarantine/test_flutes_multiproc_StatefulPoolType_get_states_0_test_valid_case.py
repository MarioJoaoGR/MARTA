
import pytest
from multiprocessing import Pool, Manager
from flutes.multiproc import StatefulPoolType, PoolState

@pytest.fixture(scope="function")
def setup_stateful_pool():
    manager = Manager()
    pool = StatefulPoolType(manager=manager)
    yield pool
    # Teardown if necessary

def test_get_states(setup_stateful_pool):
    pool = setup_stateful_pool
    states = pool.get_states()
    assert isinstance(states, list), "Expected a list of states"
    assert all(isinstance(state, PoolState) for state in states), "All items should be instances of PoolState"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPoolType_get_states_0_test_valid_case
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_get_states_0_test_valid_case.py:9:11: E1123: Unexpected keyword argument 'manager' in constructor call (unexpected-keyword-arg)


"""