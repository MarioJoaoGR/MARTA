
import pytest
from multiprocessing import Pool, PoolError
from flutes.multiproc import safe_pool

def test_invalid_inputs():
    # Test that safe_pool raises a ValueError when processes is negative
    with pytest.raises(ValueError):
        with safe_pool(-1) as pool:
            pass

    # Test that safe_pool raises a ValueError when state_class is not a subclass of PoolState
    class NotPoolState(object):
        pass

    with pytest.raises(ValueError):
        with safe_pool(processes=4, state_class=NotPoolState) as pool:
            pass

    # Test that safe_pool raises a ValueError when closing contains an invalid object
    class InvalidCloseable:
        def close(self):
            pass

    with pytest.raises(ValueError):
        with safe_pool(processes=4, closing=[InvalidCloseable()]) as pool:
            pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_safe_pool_2_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_2_test_invalid_inputs.py:3:0: E0611: No name 'PoolError' in module 'multiprocessing' (no-name-in-module)


"""