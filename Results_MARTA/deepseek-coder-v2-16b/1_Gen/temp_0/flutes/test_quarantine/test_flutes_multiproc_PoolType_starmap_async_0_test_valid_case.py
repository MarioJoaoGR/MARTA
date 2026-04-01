
import pytest
from flutes.multiproc import PoolType

def test_valid_case():
    pool = PoolType()
    def multiply(a, b):
        return a * b
    
    args_list = [(1, 2), (3, 4), (5, 6)]
    result = pool.starmap_async(multiply, args_list)
    
    # Assuming the function `get` is available on mp.pool.ApplyResult
    results = result.get()  # Retrieve the results when done
    
    assert len(results) == len(args_list)
    for r in results:
        assert isinstance(r, int)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_starmap_async_0_test_valid_case
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_async_0_test_valid_case.py:11:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""