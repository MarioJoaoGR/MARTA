
import pytest
from flutes.multiproc import PoolType

def test_invalid_input():
    pool = PoolType()
    
    with pytest.raises(TypeError):  # Expecting a TypeError since map is not supposed to return anything
        result = pool.map("not_a_function", [1, 2, 3])  # Providing an invalid function

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_map_0_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_map_0_test_invalid_input.py:9:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""