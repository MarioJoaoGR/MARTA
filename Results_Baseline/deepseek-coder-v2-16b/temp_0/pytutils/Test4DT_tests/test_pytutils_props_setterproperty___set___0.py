
import pytest
from pytutils.props import setterproperty

# Example usage of the setterproperty class
class MyClass:
    def __init__(self, value):
        self._value = value
    
    @setterproperty
    def value(self, new_value):
        self._value = new_value
    
    def get_value(self):
        return self._value

# Test cases for the setterproperty class
def test_setterproperty_initialization():
    """Test initialization of setterproperty with a function and optional documentation."""
    def func(obj, value):
        obj._value = value
    
    sp = setterproperty(func)
    assert hasattr(sp, 'func'), "The setterproperty instance should have a 'func' attribute."
    assert sp.func == func, f"Expected func to be {func}, but got {sp.func}."

def test_setterproperty_with_doc():
    """Test initialization of setterproperty with documentation."""
    def func(obj, value):
        obj._value = value
    
    sp = setterproperty(func, "A property that allows setting a value through an attribute.")
    assert sp.__doc__ == "A property that allows setting a value through an attribute.", \
        f"Expected documentation to be 'A property that allows setting a value through an attribute.', but got {sp.__doc__}."

def test_setterproperty_set_value():
    """Test setting a value using the setterproperty."""
    obj = MyClass(10)
    assert obj.get_value() == 10, "Initial value should be 10."
    
    obj.value = 20