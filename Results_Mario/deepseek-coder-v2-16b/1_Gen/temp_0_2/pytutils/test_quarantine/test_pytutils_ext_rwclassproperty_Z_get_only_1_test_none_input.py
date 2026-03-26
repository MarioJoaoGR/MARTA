
from pytutils.ext.rwclassproperty import sentinel

class Z:
    _get_set = sentinel.nothing
    
    def get_only(self):
        get_only_cls(self)
        return sentinel.get_only

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_Z_get_only_1_test_none_input
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_Z_get_only_1_test_none_input.py:8:8: E0602: Undefined variable 'get_only_cls' (undefined-variable)


"""