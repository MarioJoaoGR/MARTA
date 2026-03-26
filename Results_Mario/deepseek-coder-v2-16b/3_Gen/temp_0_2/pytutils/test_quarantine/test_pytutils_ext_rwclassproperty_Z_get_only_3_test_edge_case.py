
from unittest.mock import patch
from pytutils.ext.rwclassproperty import sentinel
import pytest

@pytest.mark.parametrize("cls", [Z()])
def test_edge_case(cls):
    with patch('pytutils.ext.rwclassproperty.sentinel', sentinel):
        assert cls.get_only() == sentinel.get_only

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_Z_get_only_3_test_edge_case
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_only_3_test_edge_case.py:6:33: E0602: Undefined variable 'Z' (undefined-variable)


"""