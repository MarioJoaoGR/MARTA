
import contextlib
from multiprocessing import Pool, DummyPool
from flutes.multiproc import safe_pool, PoolState

def test_edge_case():
    with contextlib.ExitStack() as exit_stack:
        pool = safe_pool(processes=0, state_class=PoolState)
        assert isinstance(pool, DummyPool), f"Expected a DummyPool instance but got {type(pool)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_safe_pool_1_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_1_test_edge_case.py:3:0: E0611: No name 'DummyPool' in module 'multiprocessing' (no-name-in-module)


"""