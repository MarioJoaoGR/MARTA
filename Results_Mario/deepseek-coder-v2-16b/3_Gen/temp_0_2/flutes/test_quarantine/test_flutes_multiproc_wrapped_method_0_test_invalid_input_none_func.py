
import pytest
from flutes.multiproc import wrapped_method, pool_method
from unittest.mock import MagicMock

def test_invalid_input_none_func():
    # Test that wrapped_method raises a TypeError when func is None
    with pytest.raises(TypeError):
        wrapped_method(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_wrapped_method_0_test_invalid_input_none_func
flutes/Test4DT_tests/test_flutes_multiproc_wrapped_method_0_test_invalid_input_none_func.py:3:0: E0611: No name 'wrapped_method' in module 'flutes.multiproc' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_multiproc_wrapped_method_0_test_invalid_input_none_func.py:3:0: E0611: No name 'pool_method' in module 'flutes.multiproc' (no-name-in-module)


"""