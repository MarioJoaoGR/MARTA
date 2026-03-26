
import pytest
from pytutils.ext.rwclassproperty import rwclassproperty

def test_invalid_input():
    with pytest.raises(TypeError):
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

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty__fix_function_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty__fix_function_0_test_invalid_input.py:9:12: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty__fix_function_0_test_invalid_input.py:15:12: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty__fix_function_0_test_invalid_input.py:19:12: E0213: Method 'bar' should have "self" as first argument (no-self-argument)


"""