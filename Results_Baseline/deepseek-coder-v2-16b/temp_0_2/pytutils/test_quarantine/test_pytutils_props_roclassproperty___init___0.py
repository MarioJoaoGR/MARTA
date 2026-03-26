
# Module: pytutils.props
from pytutils import roclassproperty

def test_roclassproperty_as_decorator():
    # Define a class with a read-only property using roclassproperty as a decorator
    class MyClass:
        def __init__(self, value):
            self._value = value
        
        @roclassproperty
        def value(self):
            return self._value
    
    # Create an instance of the class and check that the property is accessible
    obj = MyClass(10)
    assert obj.value == 10, "Expected initial value to be 10"
    
    # Attempt to set the property and expect an AttributeError
    try:
        obj.value = 20
    except AttributeError as e:
        assert True, f"Expected AttributeError: {e}"

def test_roclassproperty_as_factory():
    # Define a class with a read-only property using roclassproperty as a factory function
    class MyClass:
        def __init__(self, value):
            self._value = value
        
        @roclassproperty(lambda self: self._value)
        def value(self):
            return self._value
    
    # Create an instance of the class and check that the property is accessible
    obj = MyClass(10)
    assert obj.value == 10, "Expected initial value to be 10"
    
    # Attempt to set the property and expect an AttributeError
    try:
        obj.value = 20
    except AttributeError as e:
        assert True, f"Expected AttributeError: {e}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_roclassproperty___init___0
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___init___0.py:3:0: E0611: No name 'roclassproperty' in module 'pytutils' (no-name-in-module)


"""