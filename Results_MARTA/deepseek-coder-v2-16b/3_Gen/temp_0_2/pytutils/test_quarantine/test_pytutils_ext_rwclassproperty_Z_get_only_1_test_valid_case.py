
import pytest
from pytutils.ext.rwclassproperty import sentinel

class Z:
    _get_set = sentinel.nothing
    
    def get_only(cls):
        return sentinel.get_only

def test_valid_case():
    assert Z.get_only() == sentinel.get_only

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_Z_get_only_1_test_valid_case
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_only_1_test_valid_case.py:8:4: E0213: Method 'get_only' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_only_1_test_valid_case.py:12:11: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)


"""