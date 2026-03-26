
import pytest
from unittest.mock import patch, sentinel

class Z:
    _get_set = sentinel.nothing
    
    def get_only(cls):
        return sentinel.get_only

def test_error_case():
    with pytest.raises(Exception) as e:
        Z.get_only()
    assert str(e.value) == 'This method requires an instance'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_Z_get_only_2_test_error_case
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_only_2_test_error_case.py:8:4: E0213: Method 'get_only' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_only_2_test_error_case.py:13:8: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)


"""