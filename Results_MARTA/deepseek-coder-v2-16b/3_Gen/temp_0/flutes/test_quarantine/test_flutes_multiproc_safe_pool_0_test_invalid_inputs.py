
import pytest
from multiprocessing import PoolState
from flutes.multiproc import safe_pool

def test_invalid_inputs():
    # Test when state_class is not a subclass of PoolState
    with pytest.raises(ValueError):
        with safe_pool(processes=0, state_class=int) as pool:
            pass

    # Test when closing contains an invalid object
    class InvalidCloseObject:
        def __init__(self):
            self.closed = False
        
        def close(self):
            self.closed = True
    
    with pytest.raises(ValueError):
        with safe_pool(processes=1, closing=[InvalidCloseObject()]) as pool:
            pass

    # Test when processes is not an integer
    with pytest.raises(TypeError):
        with safe_pool(processes="invalid", state_class=PoolState) as pool:
            pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_safe_pool_0_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_0_test_invalid_inputs.py:3:0: E0611: No name 'PoolState' in module 'multiprocessing' (no-name-in-module)


"""