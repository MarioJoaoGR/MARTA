
import pytest
from pytutils.ext.rwclassproperty import sentinel

class Z:
    _get_set = sentinel.nothing
    
    def get_only(cls):
        return sentinel.get_only

def test_valid_input():
    z_instance = Z()
    assert z_instance.get_only() == sentinel.get_only

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_Z_get_only_5_test_valid_input
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_only_5_test_valid_input.py:8:4: E0213: Method 'get_only' should have "self" as first argument (no-self-argument)


"""