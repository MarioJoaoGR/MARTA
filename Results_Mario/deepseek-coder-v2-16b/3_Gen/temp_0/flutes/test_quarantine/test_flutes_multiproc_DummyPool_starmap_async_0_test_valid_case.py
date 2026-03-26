
import pytest
from multiprocessing import Pool
from dummy_pool import DummyPool

@pytest.mark.parametrize("fn, iterable", [
    (lambda x, y: x + y, [(1, 2), (3, 4)]),
    (lambda a, b: a * b, [(5, 6), (7, 8)]),
])
def test_valid_case(fn, iterable):
    dummy_pool = DummyPool(processes=0)
    result = dummy_pool.starmap_async(fn, iterable).get()
    expected_result = [fn(*args) for args in iterable]
    assert result == expected_result

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_DummyPool_starmap_async_0_test_valid_case
flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_starmap_async_0_test_valid_case.py:4:0: E0401: Unable to import 'dummy_pool' (import-error)


"""