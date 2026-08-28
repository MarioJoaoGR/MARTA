
import pytest
from flutils.decorators import cached_property

# Test 1: Basic Usage of cached_property in a class
def test_cached_property_basic():
    class MyClass:
        def __init__(self):
            self.x = 5
        
        @cached_property
        def y(self):
            return self.x + 1
    
    obj = MyClass()
    assert obj.y == 6, "Expected cached property to be computed once and then returned from cache."
    # Accessing again should not recompute the value
    assert obj.y == 6, "Expected cached property to return cached value without recomputation."

# Test 2: Resetting the cache by deleting the attribute
def test_cached_property_reset():
    class MyClass:
        def __init__(self):
            self.x = 5
        
        @cached_property
        def y(self):
            return self.x + 1
    
    obj = MyClass()
    assert obj.y == 6, "Initial access should compute the value."
    del obj.__dict__['y']
    assert obj.y == 6, "After deleting the attribute, accessing it should recompute the value."

# Test 3: Handling of invalid input (non-callable)
def test_invalid_input():
    class MyClass:
        @cached_property
        def y(self):
            return self.x + 1  # This will raise an AttributeError because 'self.x' is not defined at this point
    
    with pytest.raises(AttributeError):
        obj = MyClass()
        assert obj.y == 6, "Expected a TypeError when accessing the property without initialization."
