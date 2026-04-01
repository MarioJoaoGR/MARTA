
import pytest
from pytutils.props import roclassproperty

def test_invalid_inputs():
    class MyClass:
        @roclassproperty
        def value(cls):
            return cls._value
    
    obj = MyClass()
    with pytest.raises(AttributeError):
        obj.value = 20

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_roclassproperty___get___0_test_invalid_inputs
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___get___0_test_invalid_inputs.py:8:8: E0213: Method 'value' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___get___0_test_invalid_inputs.py:9:19: E1101: Instance of 'MyClass' has no '_value' member; maybe 'value'? (no-member)


"""