
import pytest
from pytutils.meta import ClassPropertyMeta
from pytutils.ext.rwclassproperty import rwclassproperty

# Define a mock class with the required metaclass for testing
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

# Test cases for rwclassproperty
def test_rwclassproperty_get():
    assert Z.foo == 123
    assert Z.bar is None

def test_rwclassproperty_set():
    Z.bar = 222
    assert Z.bar == 222

# Edge case: Check if TypeError is raised when the metaclass is not ClassPropertyMeta
def test_rwclassproperty_wrong_metaclass():
    class WrongClass(object):
        @rwclassproperty
        def wrong_prop(cls):
            return 456
    
    with pytest.raises(TypeError) as excinfo:
        WrongClass.wrong_prop
    assert str(excinfo.value) == "Class <class 'pytutils.ext.rwclassproperty.WrongClass'> does not extend from the required ClassPropertyMeta metaclass"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_edge_cases
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_edge_cases.py:3:0: E0401: Unable to import 'pytutils.meta' (import-error)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_edge_cases.py:3:0: E0611: No name 'meta' in module 'pytutils' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_edge_cases.py:9:4: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_edge_cases.py:15:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_edge_cases.py:19:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_edge_cases.py:35:8: E0213: Method 'wrong_prop' should have "self" as first argument (no-self-argument)


"""