
import pytest
from flutes.multiproc import PoolType

def test_invalid_inputs():
    pool = PoolType()
    
    # Test with invalid function (not callable)
    with pytest.raises(TypeError):
        result = pool.map("not a callable", [1, 2, 3])
    
    # Test with invalid iterable (not iterable)
    with pytest.raises(TypeError):
        result = pool.map(lambda x: x ** 2, "not an iterable")
    
    # Test with invalid chunksize (not integer or None)
    with pytest.raises(TypeError):
        result = pool.map(lambda x: x ** 2, [1, 2, 3], chunksize="invalid")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_map_0_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_map_0_test_invalid_inputs.py:10:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_map_0_test_invalid_inputs.py:14:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_map_0_test_invalid_inputs.py:18:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""