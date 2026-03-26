
import pytest
from pytutils.meta import ClassPropertyMeta, rwclassproperty

@pytest.fixture(autouse=True)
def setup_and_teardown():
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

    yield Z

def test_foo():
    assert Z.foo == 123

def test_bar_initial():
    assert Z.bar is None

def test_set_bar():
    Z.bar = 222
    assert Z.bar == 222

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty___set___1_test_edge_case
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___1_test_edge_case.py:3:0: E0401: Unable to import 'pytutils.meta' (import-error)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___1_test_edge_case.py:3:0: E0611: No name 'meta' in module 'pytutils' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___1_test_edge_case.py:9:8: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___1_test_edge_case.py:15:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___1_test_edge_case.py:19:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___1_test_edge_case.py:25:11: E0602: Undefined variable 'Z' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___1_test_edge_case.py:28:11: E0602: Undefined variable 'Z' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___1_test_edge_case.py:31:4: E0602: Undefined variable 'Z' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___1_test_edge_case.py:32:11: E0602: Undefined variable 'Z' (undefined-variable)


"""