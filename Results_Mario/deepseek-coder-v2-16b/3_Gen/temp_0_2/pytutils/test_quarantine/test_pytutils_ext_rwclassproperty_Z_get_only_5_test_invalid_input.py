
import pytest
from pytutils.ext.rwclassproperty import sentinel

def test_invalid_input():
    with pytest.raises(TypeError):  # Since get_only expects a class, passing an instance will raise a TypeError
        Z().get_only()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_Z_get_only_5_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_only_5_test_invalid_input.py:7:8: E0602: Undefined variable 'Z' (undefined-variable)


"""