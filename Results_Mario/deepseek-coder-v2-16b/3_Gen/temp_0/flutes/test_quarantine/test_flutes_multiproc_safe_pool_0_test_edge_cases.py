
import contextlib
from multiprocessing import PoolState, Pool as MPool
from flutes.multiproc import safe_pool

class MyPoolState(PoolState):
    def __init__(self):
        self.data = []

def test_edge_cases():
    with contextlib.ExitStack() as exit_stack:
        # Test sequential execution when processes == 0
        with safe_pool(processes=0, state_class=MyPoolState) as pool:
            assert isinstance(pool, DummyPool), "Expected a DummyPool instance"
        
        # Test stateful process
        with safe_pool(processes=4, state_class=MyPoolState) as pool:
            results = pool.map(lambda x: x * 2, range(10))
            assert isinstance(pool._state, MyPoolState), "Expected the pool to have a state of type MyPoolState"
        
        # Test without stateful processes
        with safe_pool(processes=4) as pool:
            results = pool.map(lambda x: x * 2, range(10))
            assert not hasattr(pool._state, 'data'), "Expected the pool to have no state"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_safe_pool_0_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_0_test_edge_cases.py:3:0: E0611: No name 'PoolState' in module 'multiprocessing' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_0_test_edge_cases.py:14:36: E0602: Undefined variable 'DummyPool' (undefined-variable)


"""