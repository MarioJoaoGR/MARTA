
import pytest
from pytutils.ext.rwclassproperty import rwclassproperty, ClassPropertyMeta

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

def test_valid_case():
    assert Z.foo == 123
    assert Z.bar is None
    Z.bar = 222
    assert Z.bar == 222

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty___set___0_test_valid_case
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___0_test_valid_case.py:7:4: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___0_test_valid_case.py:13:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___0_test_valid_case.py:17:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)


"""