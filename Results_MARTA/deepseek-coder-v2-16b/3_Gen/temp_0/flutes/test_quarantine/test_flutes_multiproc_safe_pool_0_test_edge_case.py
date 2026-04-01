
import pytest
from multiprocessing import PoolState
from flutes.multiproc import safe_pool

@pytest.mark.parametrize("processes", [0, 1, 4])
def test_safe_pool(processes):
    with safe_pool(processes=processes) as pool:
        if processes == 0:
            assert isinstance(pool, DummyPool), "Expected a DummyPool instance when processes is 0"
        else:
            assert isinstance(pool, PoolWrapper), f"Expected a PoolWrapper instance for {processes} processes"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_safe_pool_0_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_0_test_edge_case.py:3:0: E0611: No name 'PoolState' in module 'multiprocessing' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_0_test_edge_case.py:10:36: E0602: Undefined variable 'DummyPool' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_0_test_edge_case.py:12:36: E0602: Undefined variable 'PoolWrapper' (undefined-variable)


"""