
import contextlib
from multiprocessing import Pool, PoolState
from flutes.multiproc import safe_pool

class MyPoolState(PoolState):
    def __init__(self):
        self.data = []

def test_valid_case():
    with safe_pool(processes=4, state_class=MyPoolState) as pool:
        results = pool.map(lambda x: x * 2, range(10))
        assert results == list(range(0, 20, 2)), "Test failed: Results do not match expected values."

    with safe_pool(processes=4) as pool:
        results = pool.map(lambda x: x * 2, range(10))
        assert results == list(range(0, 20, 2)), "Test failed: Results do not match expected values."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_safe_pool_0_test_valid_case
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_0_test_valid_case.py:3:0: E0611: No name 'PoolState' in module 'multiprocessing' (no-name-in-module)


"""