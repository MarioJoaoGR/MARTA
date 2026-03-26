
import pytest
from flutes.multiproc import PoolType

def test_valid_inputs():
    pool = PoolType()
    
    def square(x):
        return x ** 2
    
    result = pool.map_async(square, [1, 2, 3, 4])
    
    while not result.ready():
        pass
    
    assert result.get() == [1, 4, 9, 16]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_map_async_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_map_async_0_test_valid_inputs.py:11:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""