
import pytest
from flutes.multiproc import PoolType

def test_error_handling():
    pool = PoolType()
    
    def multiply(a, b):
        return a * b
    
    args_list = [(1, 2), (3, 4), (5, 6)]
    
    with pytest.raises(ZeroDivisionError):
        # This will raise an error because of the division by zero in the callback
        result = pool.starmap_async(lambda x: x[0] / x[1], args_list, callback=lambda x: 1 / (x[0] - 3))
        result.get()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_starmap_async_0_test_error_handling
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_async_0_test_error_handling.py:15:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""