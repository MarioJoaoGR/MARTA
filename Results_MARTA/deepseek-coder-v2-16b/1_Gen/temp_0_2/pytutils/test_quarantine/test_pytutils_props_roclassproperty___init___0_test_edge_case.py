
import pytest
from pytutils.props import roclassproperty

def test_roclassproperty_init():
    """Test the initialization of the roclassproperty."""
    
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
************* Module Test4DT_tests.test_pytutils_props_roclassproperty___init___0_test_edge_case
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___init___0_test_edge_case.py:10:8: E0213: Method 'my_property' should have "self" as first argument (no-self-argument)


"""