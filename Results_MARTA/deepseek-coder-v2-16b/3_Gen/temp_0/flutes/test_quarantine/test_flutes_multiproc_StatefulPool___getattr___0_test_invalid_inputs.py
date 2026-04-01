
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPool, CustomState

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test initializing with invalid state class type
        StatefulPool(Pool, int, (1, 2), (), {})

    with pytest.raises(ValueError):
        # Test initializing with invalid init args type
        StatefulPool(Pool, CustomState, "invalid", (), {})

    with pytest.raises(TypeError):
        # Test initializing with invalid pool class type
        StatefulPool("InvalidPoolClass", CustomState, (1, 2), (), {})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPool___getattr___0_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool___getattr___0_test_invalid_inputs.py:4:0: E0611: No name 'CustomState' in module 'flutes.multiproc' (no-name-in-module)


"""