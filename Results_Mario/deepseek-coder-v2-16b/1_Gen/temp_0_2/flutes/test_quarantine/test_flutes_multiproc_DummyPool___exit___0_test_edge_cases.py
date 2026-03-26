
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

@pytest.fixture
def dummy_pool():
    return DummyPool(processes=0)

def test_dummy_pool_exit(dummy_pool):
    assert dummy_pool._state == mp.pool.RUN
    dummy_pool.__exit__(None, None, None)
    assert dummy_pool._state == mp.pool.TERMINATE

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_DummyPool___exit___0_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_DummyPool___exit___0_test_edge_cases.py:11:32: E0602: Undefined variable 'mp' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc_DummyPool___exit___0_test_edge_cases.py:13:32: E0602: Undefined variable 'mp' (undefined-variable)


"""