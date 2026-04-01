
import pytest
from pytutils.props import roclassproperty

def test_invalid_input():
    with pytest.raises(AttributeError):
        class MyClass:
            @roclassproperty
            def my_property(cls):
                return "This is a read-only property"
        
        obj = MyClass()
        obj.my_property  # This should raise an AttributeError due to the invalid input

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_roclassproperty___get___0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___get___0_test_invalid_input.py:9:12: E0213: Method 'my_property' should have "self" as first argument (no-self-argument)


"""