
import pytest
from multiprocessing import Pool
from dummy_pool import DummyPool  # Assuming the DummyPool class is in a file named dummy_pool.py

def test_valid_inputs():
    def my_function(x):
        return x * 2
    
    pool = DummyPool(processes=0)
    iterable = [1, 2, 3, 4]
    results = list(pool.imap(my_function, iterable))
    
    assert results == [2, 4, 6, 8]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_DummyPool_imap_1_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_imap_1_test_valid_inputs.py:4:0: E0401: Unable to import 'dummy_pool' (import-error)

"""