
import pytest
from pytutils.props import roclassproperty

def test_invalid_input():
    class MyClass:
        @roclassproperty
        def my_prop(cls):
            return "This is a read-only property"
    
    obj = MyClass()
    with pytest.raises(AttributeError):
        obj.my_prop = "Attempt to modify the property"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_roclassproperty___get___0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___get___0_test_invalid_input.py:8:8: E0213: Method 'my_prop' should have "self" as first argument (no-self-argument)


"""