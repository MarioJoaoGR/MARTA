
# Module: pytutils.props
from pytutils.props import lazyperclassproperty

def test_lazyperclassproperty():
    # Define a property-generating function that performs an expensive calculation
    def expensive_calculation(cls):
        return sum(range(1, 1000))
    
    # Apply the lazyperclassproperty decorator to define a class property
    @lazyperclassproperty(expensive_calculation)
    def cached_calculation(cls):
        pass
    
    # Define a base class and a subclass to test separate instances per class/inheritor
    class MyClass:
        def __init__(self, value):
            self.value = value
        
        @classmethod
        def get_cached_calculation(cls):
            return cached_calculation  # Corrected the attribute access
    
    class SubClass(MyClass):
        pass
    
    # Check the cached calculation for MyClass and SubClass
    assert MyClass.get_cached_calculation() == sum(range(1, 1000)), "MyClass's cached calculation should be computed once"
    assert SubClass.get_cached_calculation() != MyClass.get_cached_calculation(), "SubClass should have a separate instance of the property"
    
    # Test that the property is lazy and only computed once per class
    class AnotherClass(MyClass):
        pass
    assert AnotherClass.get_cached_calculation() == sum(range(1, 1000)), "AnotherClass should have its own separate instance of the property"
    
    # Test that the property is not affected by changes to the calculation function's implementation
    def new_expensive_calculation(cls):
        return sum(range(1, 2000))
    
    @lazyperclassproperty(new_expensive_calculation)
    def cached_calculation(cls):
        pass
    
    class YetAnotherClass(MyClass):
        pass
    
    assert YetAnotherClass.get_cached_calculation() == sum(range(1, 2000)), "YetAnotherClass's cached calculation should reflect the new expensive calculation"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_lazyperclassproperty_0
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0.py:41:4: E0102: function already defined line 12 (function-redefined)


"""