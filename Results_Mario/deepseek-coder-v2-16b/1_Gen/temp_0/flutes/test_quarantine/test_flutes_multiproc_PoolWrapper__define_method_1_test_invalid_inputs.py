
import pytest
from multiprocessing import Pool
from flutes.multiproc import PoolWrapper

def test_invalid_inputs():
    pool = PoolWrapper()
    
    # Test with a non-callable argument (should raise TypeError)
    with pytest.raises(TypeError):
        pool.map("not_a_function", [1, 2, 3])
        
    # Test with too many arguments (should raise TypeError)
    def func(): pass
    with pytest.raises(TypeError):
        pool.map(func, [1, 2, 3], extra=None)
        
    # Test with invalid keyword arguments (should raise TypeError)
    with pytest.raises(TypeError):
        pool.map(func, [], kwds={"extra": "argument"})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolWrapper__define_method_1_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_1_test_invalid_inputs.py:16:8: E1123: Unexpected keyword argument 'extra' in method call (unexpected-keyword-arg)
flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_1_test_invalid_inputs.py:20:8: E1123: Unexpected keyword argument 'kwds' in method call (unexpected-keyword-arg)


"""