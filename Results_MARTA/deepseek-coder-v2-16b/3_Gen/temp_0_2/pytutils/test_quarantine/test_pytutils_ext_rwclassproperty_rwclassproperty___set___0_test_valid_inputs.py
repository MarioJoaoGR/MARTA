
import pytest
from pytutils.ext.rwclassproperty import rwclassproperty, ClassPropertyMeta

def test_valid_inputs():
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

    # Set the property and test again
    Z.bar = 222
    assert Z.bar == 222

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty___set___0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___0_test_valid_inputs.py:8:8: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___0_test_valid_inputs.py:14:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___0_test_valid_inputs.py:18:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)


"""