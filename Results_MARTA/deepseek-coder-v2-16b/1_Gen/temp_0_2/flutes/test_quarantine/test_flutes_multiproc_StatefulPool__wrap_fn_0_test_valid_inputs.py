
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPool, MyState

@pytest.fixture
def pool():
    return StatefulPool(Pool, MyState, (1, 2), (), {})

def test_valid_inputs(pool):
    assert isinstance(pool._pool, Pool)
    assert pool._state_class is MyState
    assert pool._class_methods == {id(MyState.__init__)}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPool__wrap_fn_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool__wrap_fn_0_test_valid_inputs.py:4:0: E0611: No name 'MyState' in module 'flutes.multiproc' (no-name-in-module)


"""