
import pytest
from multiprocessing import Pool, Manager
from flutes.multiproc import StatefulPool, MyState

@pytest.fixture(scope="module")
def pool():
    return StatefulPool(Pool, MyState, (1, 2), (), {})

def test_apply_broadcast(pool):
    def broadcast_fn(state):
        state.value = "test"
        return state.value

    result = pool._apply_broadcast(broadcast_fn)
    assert result is not None
    assert result[0] == "test"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPool__apply_broadcast_0_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__apply_broadcast_0_test_edge_cases.py:4:0: E0611: No name 'MyState' in module 'flutes.multiproc' (no-name-in-module)


"""