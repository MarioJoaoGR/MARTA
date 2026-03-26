
# Module: pytutils.props
# test_roclassproperty.py
import pytest
from pytutils.props import roclassproperty

# Example Usage Scenario 1: Defining a Read-Only Property in a Class
@pytest.fixture(scope="module")
def define_my_class():
    class MyClass:
        @roclassproperty
        def my_prop(cls):
            return "This is a read-only property"
    return MyClass

# Test case for accessing the property
def test_accessing_readonly_property(define_my_class):
    obj = define_my_class()
    assert obj.my_prop == "This is a read-only property"

# Test case for attempting to set the property (should raise AttributeError)
def test_attempting_to_set_readonly_property(define_my_class):
    obj = define_my_class()
    with pytest.raises(AttributeError):
        obj.my_prop = "Attempt to modify the property"

# Example Usage Scenario 2: Defining Multiple Read-Only Properties in a Class
@pytest.fixture(scope="module")
def define_multiple_props():
    class MyClass:
        @roclassproperty
        def prop1(cls):
            return "Property 1 value"
        
        @roclassproperty
        def prop2(cls):
            return "Property 2 value"
    return MyClass

# Test case for accessing multiple properties
def test_accessing_multiple_readonly_properties(define_multiple_props):
    obj = define_multiple_props()
    assert obj.prop1 == "Property 1 value"
    assert obj.prop2 == "Property 2 value"

# Example Usage Scenario 3: Using roclassproperty with a Class Method
@pytest.fixture(scope="module")
def define_class_method_prop():
    class MyClass:
        @roclassproperty
        def class_method_prop(cls):
            return cls.__name__
    return MyClass

# Test case for accessing the property from the class method perspective
def test_accessing_readonly_property_from_classmethod(define_class_method_prop):
    assert define_class_method_prop.class_method_prop == "MyClass"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_roclassproperty___init___0
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___init___0.py:12:8: E0213: Method 'my_prop' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___init___0.py:32:8: E0213: Method 'prop1' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___init___0.py:36:8: E0213: Method 'prop2' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___init___0.py:51:8: E0213: Method 'class_method_prop' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___init___0.py:52:19: E1101: Instance of 'MyClass' has no '__name__' member (no-member)


"""