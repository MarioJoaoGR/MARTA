
import pytest
from multiprocessing import PoolState
from flutes.multiproc import safe_pool

def test_invalid_inputs():
    # Test with None for state_class (should raise ValueError)
    with pytest.raises(ValueError):
        with safe_pool(processes=0, state_class=None):
            pass

    # Test with invalid state_class type (should raise ValueError)
    class InvalidStateClass:
        pass

    with pytest.raises(ValueError):
        with safe_pool(processes=0, state_class=InvalidStateClass):
            pass

    # Test with non-list for closing argument (should raise ValueError)
    with pytest.raises(ValueError):
        with safe_pool(processes=0, closing="not a list"):
            pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_safe_pool_0_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_0_test_invalid_inputs.py:3:0: E0611: No name 'PoolState' in module 'multiprocessing' (no-name-in-module)


"""