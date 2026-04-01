
import pytest
from pytutils.ext.rwclassproperty import rwclassproperty
from pytutils.meta import ClassPropertyMeta

# Define a class with the rwclassproperty decorator
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

# Test case for the error scenario
def test_error_case():
    with pytest.raises(TypeError) as excinfo:
        Z.foo  # This should work fine since foo is a class property
    
    assert str(excinfo.value) == f"Class {Z.__class__} does not extend from the required ClassPropertyMeta metaclass"

    with pytest.raises(TypeError) as excinfo:
        Z.bar  # This should raise a TypeError since bar is expected to be accessed via class property but defined without self argument
    
    assert str(excinfo.value) == f"Class {Z.__class__} does not extend from the required ClassPropertyMeta metaclass"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_error_case
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_error_case.py:4:0: E0401: Unable to import 'pytutils.meta' (import-error)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_error_case.py:4:0: E0611: No name 'meta' in module 'pytutils' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_error_case.py:9:4: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_error_case.py:15:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_error_case.py:19:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)


"""