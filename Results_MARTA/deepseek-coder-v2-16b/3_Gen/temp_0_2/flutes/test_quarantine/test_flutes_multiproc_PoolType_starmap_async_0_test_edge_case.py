
import pytest
from flutes.multiproc import PoolType

def test_starmap_async():
    pool = PoolType()
    
    def multiply(a, b):
        return a * b
    
    args_list = [(1, 2), (3, 4), (5, 6)]
    result = pool.starmap_async(multiply, args_list)
    
    # Wait for the results to be ready and retrieve them
    results = result.get()
    
    assert results == [2, 12, 30]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_starmap_async_0_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_async_0_test_edge_case.py:12:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""