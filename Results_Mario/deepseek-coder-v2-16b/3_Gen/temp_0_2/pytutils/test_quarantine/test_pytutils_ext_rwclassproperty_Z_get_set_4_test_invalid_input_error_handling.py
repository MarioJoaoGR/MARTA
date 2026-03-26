
from unittest.mock import patch
from pytutils.ext.rwclassproperty import get_set_set_cls
import pytest

@pytest.mark.parametrize("value", [None, 'some_value'])
def test_get_set(value):
    class Z:
        _get_set = sentinel.nothing
    
    if value is None:
        assert Z.get_set(cls=Z) == sentinel.nothing
    else:
        Z.get_set(cls=Z, value=value)
        assert Z._get_set == value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_Z_get_set_4_test_invalid_input_error_handling
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_set_4_test_invalid_input_error_handling.py:3:0: E0611: No name 'get_set_set_cls' in module 'pytutils.ext.rwclassproperty' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_set_4_test_invalid_input_error_handling.py:9:19: E0602: Undefined variable 'sentinel' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_set_4_test_invalid_input_error_handling.py:12:15: E1101: Class 'Z' has no 'get_set' member; maybe '_get_set'? (no-member)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_set_4_test_invalid_input_error_handling.py:12:35: E0602: Undefined variable 'sentinel' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_set_4_test_invalid_input_error_handling.py:14:8: E1101: Class 'Z' has no 'get_set' member; maybe '_get_set'? (no-member)


"""