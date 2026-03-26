
import pytest
from pytutils.props import roclassproperty

def test_invalid_input():
    with pytest.raises(TypeError):
        class MyClass:
            @roclassproperty
            def my_property(self):  # This should raise a TypeError because the method has no 'self' argument
                return "This is a read-only property"
    
    with pytest.raises(TypeError):
        class MyClass:
            @roclassproperty
            def my_property(cls):  # This should raise a TypeError because the method has no 'cls' argument
                return "This is a read-only property"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_roclassproperty___init___0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___init___0_test_invalid_input.py:13:8: E0102: class already defined line 7 (function-redefined)
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___init___0_test_invalid_input.py:15:12: E0213: Method 'my_property' should have "self" as first argument (no-self-argument)


"""