
from unittest.mock import patch, sentinel
import pytest
from pytutils.ext.rwclassproperty import get_only

@pytest.mark.parametrize("cls", [None, 1, "string"])
def test_invalid_input(cls):
    with pytest.raises(TypeError):
        get_only(cls)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_Z_get_only_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_only_0_test_invalid_input.py:4:0: E0611: No name 'get_only' in module 'pytutils.ext.rwclassproperty' (no-name-in-module)


"""