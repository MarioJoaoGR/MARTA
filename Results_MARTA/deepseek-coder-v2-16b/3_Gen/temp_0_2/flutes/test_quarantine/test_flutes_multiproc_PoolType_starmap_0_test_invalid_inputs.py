
import pytest
from flutes.multiproc import PoolType

def test_invalid_inputs():
    pool = PoolType()
    
    # Test with invalid inputs (none iterable)
    with pytest.raises(TypeError):
        result = pool.starmap(lambda x: x, 2)  # Invalid input type for iterable

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_starmap_0_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_0_test_invalid_inputs.py:10:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""