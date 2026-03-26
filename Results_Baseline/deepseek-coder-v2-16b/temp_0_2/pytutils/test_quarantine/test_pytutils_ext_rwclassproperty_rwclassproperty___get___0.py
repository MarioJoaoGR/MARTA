
# Module: pytutils.ext.rwclassproperty
import pytest
from classproperty import ClassPropertyMeta, rwclassproperty

# Define a test class with ClassPropertyMeta as metaclass
@pytest.fixture(scope="module")
def TestClass():
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
    return Z

def test_read_foo(TestClass):
    assert TestClass.foo == 123

def test_read_bar(TestClass):
    assert TestClass.bar is None

def test_write_bar(TestClass):
    TestClass.bar = 222
    assert TestClass.bar == 222

def test_invalid_class():
    with pytest.raises(TypeError) as e:
        class InvalidClass(metaclass=object):
            @rwclassproperty
            def invalid_prop(cls):
                return "Invalid Property"
    assert str(e.value) == f"Class {InvalidClass.__name__} does not extend from the required ClassPropertyMeta metaclass"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty___get___0
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:4:0: E0401: Unable to import 'classproperty' (import-error)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:11:8: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:17:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:21:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:37:8: E1139: Invalid metaclass 'object' used (invalid-metaclass)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:39:12: E0213: Method 'invalid_prop' should have "self" as first argument (no-self-argument)


"""