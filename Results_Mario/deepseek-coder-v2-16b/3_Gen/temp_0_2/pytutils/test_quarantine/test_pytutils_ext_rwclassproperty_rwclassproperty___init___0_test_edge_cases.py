
from pytutils.ext.rwclassproperty import rwclassproperty
import pytest

def test_edge_cases():
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

    # Test initial values
    assert Z.foo == 123
    assert Z.bar is None

    # Set new value and test it
    Z.bar = 222
    assert Z.bar == 222

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty___init___0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0_test_edge_cases.py:8:8: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0_test_edge_cases.py:14:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0_test_edge_cases.py:18:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0_test_edge_cases.py:6:4: E0602: Undefined variable 'ClassPropertyMeta' (undefined-variable)


"""