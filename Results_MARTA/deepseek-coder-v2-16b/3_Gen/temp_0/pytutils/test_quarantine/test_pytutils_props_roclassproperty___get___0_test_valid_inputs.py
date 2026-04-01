
import pytest
from pytutils.props import roclassproperty

# Define a class with a read-only property
class MyClass:
    @roclassproperty
    def my_attribute(cls):
        return cls.__name__

def test_valid_inputs():
    obj = MyClass()
    assert obj.my_attribute == 'MyClass'  # Accessing the property should work without raising an error
    
    with pytest.raises(AttributeError):
        obj.my_attribute = "new value"  # Attempting to set the property should raise an AttributeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_roclassproperty___get___0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___get___0_test_valid_inputs.py:8:4: E0213: Method 'my_attribute' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___get___0_test_valid_inputs.py:9:15: E1101: Instance of 'MyClass' has no '__name__' member (no-member)


"""