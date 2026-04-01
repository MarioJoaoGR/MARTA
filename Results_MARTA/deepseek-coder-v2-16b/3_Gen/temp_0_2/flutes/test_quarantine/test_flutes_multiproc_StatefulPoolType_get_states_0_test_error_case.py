
# flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_get_states_0_test_error_case.py
import pytest
from multiprocessing import Pool, Manager
from multiprocessing_stateful import StatefulPoolType, PoolState

@pytest.fixture(scope="module")
def pool():
    manager = Manager()
    pool = StatefulPoolType(manager.Queue(), PoolState)
    yield pool
    pool.terminate()

def test_get_states(pool):
    states = pool.get_states()
    assert isinstance(states, list), "Expected a list of states"
    assert all(isinstance(state, PoolState) for state in states), "All elements should be instances of PoolState"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPoolType_get_states_0_test_error_case
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_get_states_0_test_error_case.py:5:0: E0401: Unable to import 'multiprocessing_stateful' (import-error)


"""