
import pytest
from multiprocessing import Pool

def test_invalid_input():
    with pytest.raises(TypeError):
        pool = DummyPool(processes='string')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_DummyPool_map_async_1_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_map_async_1_test_invalid_input.py:7:15: E0602: Undefined variable 'DummyPool' (undefined-variable)


"""