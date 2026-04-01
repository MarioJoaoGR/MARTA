
import pytest
from pytutils.ext.rwclassproperty import rwclassproperty
from classproperty import ClassPropertyMeta

# Test fixture to ensure the metaclass is applied correctly
@pytest.fixture(autouse=True)
def setup_class():
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
    globals()['Z'] = Z

def test_invalid_inputs():
    with pytest.raises(TypeError) as excinfo:
        class InvalidClass(object):
            @rwclassproperty
            def invalid_prop(cls):
                return 456
    
    assert "does not extend from the required" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_invalid_inputs
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_invalid_inputs.py:4:0: E0401: Unable to import 'classproperty' (import-error)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_invalid_inputs.py:11:8: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_invalid_inputs.py:17:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_invalid_inputs.py:21:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0_test_invalid_inputs.py:29:12: E0213: Method 'invalid_prop' should have "self" as first argument (no-self-argument)


"""