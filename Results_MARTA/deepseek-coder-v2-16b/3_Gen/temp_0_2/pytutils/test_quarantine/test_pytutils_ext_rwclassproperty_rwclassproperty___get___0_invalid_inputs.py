
from pytutils.ext.rwclassproperty import rwclassproperty
import pytest

# Assuming ClassPropertyMeta is defined in the same module or can be imported correctly
from pytutils.meta import ClassPropertyMeta

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

def test_rwclassproperty():
    assert Z.foo == 123
    assert Z.bar is None
    
    Z.bar = 222
    assert Z.bar == 222

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_invalid_inputs
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_invalid_inputs.py:6:0: E0401: Unable to import 'pytutils.meta' (import-error)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_invalid_inputs.py:6:0: E0611: No name 'meta' in module 'pytutils' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_invalid_inputs.py:10:4: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_invalid_inputs.py:16:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_invalid_inputs.py:20:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)


"""