
import pytest
from flutes.multiproc import PoolType

def test_invalid_inputs():
    pool = PoolType()
    
    # Test with None as func (should raise TypeError)
    with pytest.raises(TypeError):
        result = pool.apply_async(None, args=(1, 2))
    
    # Test with non-callable func (should raise TypeError)
    with pytest.raises(TypeError):
        result = pool.apply_async("not a callable", args=(1, 2))
    
    # Test with invalid callback type (should raise TypeError)
    with pytest.raises(TypeError):
        result = pool.apply_async(lambda x: x, args=(1,), callback="not a callable")
    
    # Test with invalid error_callback type (should raise TypeError)
    with pytest.raises(TypeError):
        result = pool.apply_async(lambda x: x, args=(1,), error_callback="not an exception handler")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_apply_async_0_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_apply_async_0_test_invalid_inputs.py:10:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_apply_async_0_test_invalid_inputs.py:14:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_apply_async_0_test_invalid_inputs.py:18:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_apply_async_0_test_invalid_inputs.py:22:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""