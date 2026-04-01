
import pytest
from flutes.multiproc import PoolType

def test_edge_case():
    pool = PoolType()
    
    def multiply(a, b):
        return a * b
    
    result = pool.starmap(multiply, [(2, 3), (4, 5)])
    assert result == [6, 20]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_starmap_0_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_0_test_edge_case.py:11:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""