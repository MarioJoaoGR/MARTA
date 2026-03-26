
import pytest
from flutes.multiproc import StatefulPoolType, PoolState  # Assuming this module exists and contains the required classes

def test_invalid_input():
    pool = StatefulPoolType()
    
    # Non-callable function as input
    non_callable = None
    
    with pytest.raises(TypeError):
        results = pool.imap(non_callable, range(10), chunksize=2)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPoolType_imap_0_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_invalid_input.py:12:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""