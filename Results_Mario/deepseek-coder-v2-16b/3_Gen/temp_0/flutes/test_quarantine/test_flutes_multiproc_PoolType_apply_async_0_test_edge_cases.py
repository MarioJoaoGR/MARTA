
import multiprocessing as mp
from flutes.multiproc import PoolType

def test_apply_async():
    pool = PoolType()
    
    def multiply(a, b):
        return a * b
    
    result = pool.apply_async(multiply, (2, 3))
    assert result.get() == 6

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_apply_async_0_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_apply_async_0_test_edge_cases.py:11:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""