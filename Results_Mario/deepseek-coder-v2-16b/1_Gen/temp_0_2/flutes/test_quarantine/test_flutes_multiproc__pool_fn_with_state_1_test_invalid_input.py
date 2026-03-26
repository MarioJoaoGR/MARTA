
import pytest
from flutes.multiproc import _pool_fn_with_state
from inspect import currentframe, FrameType
from typing import Callable, TypeVar

R = TypeVar('R')

def test_invalid_input():
    with pytest.raises(TypeError):
        _pool_fn_with_state(lambda: None)  # Invalid function should raise TypeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__pool_fn_with_state_1_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc__pool_fn_with_state_1_test_invalid_input.py:4:0: E0611: No name 'FrameType' in module 'inspect' (no-name-in-module)


"""