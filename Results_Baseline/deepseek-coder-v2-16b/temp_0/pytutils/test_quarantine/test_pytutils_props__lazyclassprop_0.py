
# Module: pytutils.props
import pytest
from pytutils.props import _lazyclassprop

# Test Case 1: Defining a Lazy Class Property
def test_lazyclassprop_definition():
    def compute_value(cls):
        return "computed value"
    
    class MyClass:
        pass
    
    # Define the lazy property
    MyClass.my_property = _lazyclassprop(compute_value)
    
    assert hasattr(MyClass, 'my_property')
    assert callable(getattr(MyClass, 'my_property'))
    assert getattr(MyClass, 'my_property') == "computed value"

# Test Case 2: Using `setterproperty` to Create a Setter Property
def test_setterproperty():
    class MyClass:
        def __init__(self, initial_value):
            self._value = initial_value
        
        @setterproperty
        def value(self, new_value):
            self._value = new_value
        
        def get_value(self):
            return self._value
    
    # Creating an instance of MyClass
    obj = MyClass(10)
    
    assert obj.get_value() == 10
    
    # Setting the property using an attribute
    obj.value = 20
    
    # Accessing the property again to verify the change
    assert obj.get_value() == 20

# Test Case 3: Defining a Read-Only Class Property with `roclassproperty`
def test_roclassproperty():
    def compute_value(cls):
        return "read only value"
    
    class MyClass:
        pass
    
    # Define the read-only property
    MyClass.my_attribute = _lazyclassprop(compute_value)
    
    # Creating an instance of MyClass
    obj = MyClass()
    
    assert hasattr(MyClass, 'my_attribute')
    assert callable(getattr(MyClass, 'my_attribute'))
    assert getattr(MyClass, 'my_attribute') == "read only value"
    
    # Attempting to set the property (this will raise an AttributeError)
    with pytest.raises(AttributeError):
        obj.my_attribute = "new value"

# Test Case 4: Using `roclassproperty` with a Class Method
def test_roclassproperty_with_classmethod():
    def compute_value(cls):
        return cls.__name__
    
    class MyClass:
        pass
    
    # Define the read-only property using a class method
    MyClass.my_attribute = _lazyclassprop(compute_value)
    
    assert hasattr(MyClass, 'my_attribute')
    assert callable(getattr(MyClass, 'my_attribute'))
    assert getattr(MyClass, 'my_attribute') == "MyClass"

# Run the tests
if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props__lazyclassprop_0
pytutils/Test4DT_tests/test_pytutils_props__lazyclassprop_0.py:4:0: E0611: No name '_lazyclassprop' in module 'pytutils.props' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_props__lazyclassprop_0.py:27:9: E0602: Undefined variable 'setterproperty' (undefined-variable)


"""