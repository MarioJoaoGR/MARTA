
import pytest
from flutes.multiproc import PoolType

def test_apply():
    pool = PoolType()
    result = pool.apply(lambda x, y: x + y, args=(1, 2))
    assert result == 3

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_apply_0_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_apply_0_test_edge_cases.py:7:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""