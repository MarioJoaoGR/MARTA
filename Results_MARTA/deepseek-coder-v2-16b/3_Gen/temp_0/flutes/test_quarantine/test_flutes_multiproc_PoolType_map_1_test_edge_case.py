
import pytest
from flutes.multiproc import PoolType

def test_map():
    pool = PoolType()
    
    def square(x: int) -> int:
        return x ** 2
    
    result = pool.map(square, [1, 2, 3, 4])
    assert result == [1, 4, 9, 16]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_map_1_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_map_1_test_edge_case.py:11:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""