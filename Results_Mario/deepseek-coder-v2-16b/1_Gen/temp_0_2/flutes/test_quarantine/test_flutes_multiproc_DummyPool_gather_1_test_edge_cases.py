
import pytest
from multiprocessing import Pool, Manager

@pytest.fixture(scope="module")
def pool():
    return DummyPool(processes=0)

def test_gather(pool):
    def multiply_by_two(x):
        return x * 2

    iterable = [0, 1, 2, 3, 4]
    results = list(pool.gather(multiply_by_two, iterable))
    assert results == [0, 2, 4, 6, 8]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_DummyPool_gather_1_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_gather_1_test_edge_cases.py:7:11: E0602: Undefined variable 'DummyPool' (undefined-variable)


"""