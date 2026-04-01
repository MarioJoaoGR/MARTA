
import pytest
from pytutils.props import roclassproperty

def test_valid_input():
    class MyClass:
        @roclassproperty
        def my_property(cls):
            return "This is a read-only property"
    
    obj = MyClass()
    assert obj.my_property == "This is a read-only property"
    
    with pytest.raises(AttributeError):
        obj.my_property = "Try to set it"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_roclassproperty___get___0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___get___0_test_valid_input.py:8:8: E0213: Method 'my_property' should have "self" as first argument (no-self-argument)


"""