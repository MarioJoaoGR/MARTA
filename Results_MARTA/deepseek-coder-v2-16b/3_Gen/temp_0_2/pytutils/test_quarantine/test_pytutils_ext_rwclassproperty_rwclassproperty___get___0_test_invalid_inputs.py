
import pytest
from pytutils.ext.rwclassproperty import rwclassproperty

# Define a mock ClassPropertyMeta to simulate the metaclass behavior
class MockClassPropertyMeta(type):
    pass

@pytest.fixture
def ValidClass():
    class ValidClass(object, metaclass=MockClassPropertyMeta):
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
    return ValidClass

def test_invalid_inputs(ValidClass):
    with pytest.raises(TypeError) as excinfo:
        class InvalidClass(object):
            @rwclassproperty
            def foo(cls):
                return 123

    assert "does not extend from the required" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_invalid_inputs
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_invalid_inputs.py:13:8: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_invalid_inputs.py:19:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_invalid_inputs.py:23:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_invalid_inputs.py:31:12: E0213: Method 'foo' should have "self" as first argument (no-self-argument)


"""