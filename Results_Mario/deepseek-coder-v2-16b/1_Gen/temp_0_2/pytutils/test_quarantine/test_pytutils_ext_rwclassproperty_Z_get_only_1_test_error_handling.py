
from pytutils.ext.rwclassproperty import sentinel

class Z:
    _get_set = sentinel.nothing
    
    def get_only(cls):
        if hasattr(cls, '_get_set'):
            return getattr(cls, '_get_set')
        else:
            raise AttributeError("Class Z does not have a '_get_set' attribute")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_Z_get_only_1_test_error_handling
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_only_1_test_error_handling.py:7:4: E0213: Method 'get_only' should have "self" as first argument (no-self-argument)


"""