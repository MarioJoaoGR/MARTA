
import pytest
from pytutils.meta import ClassPropertyMeta, rwclassproperty

def test_rwclassproperty():
    class Z(object, metaclass=ClassPropertyMeta):
        @rwclassproperty
        def foo(cls):
            return 123
        
        _bar = None
        
        @rwclassproperty
        def bar(cls):
            return cls._bar
        
        @bar.setter
        def bar(cls, value):
            cls._bar = value
    
    assert Z.foo == 123
    assert Z.bar is None
    Z.bar = 222
    assert Z.bar == 222

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty__fix_function_0_test_edge_case
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty__fix_function_0_test_edge_case.py:3:0: E0401: Unable to import 'pytutils.meta' (import-error)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty__fix_function_0_test_edge_case.py:3:0: E0611: No name 'meta' in module 'pytutils' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty__fix_function_0_test_edge_case.py:8:8: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty__fix_function_0_test_edge_case.py:14:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty__fix_function_0_test_edge_case.py:18:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)


"""