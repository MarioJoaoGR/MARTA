
import pytest
from pytutils.props import roclassproperty

# Define a sample class with a read-only property
class MyClass:
    @roclassproperty
    def my_property(cls):
        return "This is a read-only property"

def test_read_only_property():
    obj = MyClass()
    
    # Check the initial value of the property
    assert obj.my_property == "This is a read-only property"
    
    # Attempt to set the property, which should raise an AttributeError
    with pytest.raises(AttributeError):
        obj.my_property = "Try to set it"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_roclassproperty___init___0_test_valid_case
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___init___0_test_valid_case.py:8:4: E0213: Method 'my_property' should have "self" as first argument (no-self-argument)


"""