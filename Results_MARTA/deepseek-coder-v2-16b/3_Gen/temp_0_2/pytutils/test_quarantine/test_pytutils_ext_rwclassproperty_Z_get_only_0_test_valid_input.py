
from unittest.mock import patch, sentinel
import pytest
from pytutils.ext.rwclassproperty import Z

def test_get_only():
    with patch('pytutils.ext.rwclassproperty.sentinel', new=sentinel):
        z = Z()
        assert z.get_only() == sentinel.get_only

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_Z_get_only_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_only_0_test_valid_input.py:4:0: E0611: No name 'Z' in module 'pytutils.ext.rwclassproperty' (no-name-in-module)


"""