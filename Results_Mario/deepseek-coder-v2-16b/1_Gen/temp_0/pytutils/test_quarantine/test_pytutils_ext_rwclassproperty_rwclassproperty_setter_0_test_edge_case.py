
from pytutils.ext.rwclassproperty import rwclassproperty
import pytest

@pytest.mark.parametrize("cls", [Z])
def test_rwclassproperty(cls):
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
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0_test_edge_case
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0_test_edge_case.py:5:33: E0602: Undefined variable 'Z' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0_test_edge_case.py:9:8: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0_test_edge_case.py:15:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0_test_edge_case.py:19:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0_test_edge_case.py:7:4: E0602: Undefined variable 'ClassPropertyMeta' (undefined-variable)


"""