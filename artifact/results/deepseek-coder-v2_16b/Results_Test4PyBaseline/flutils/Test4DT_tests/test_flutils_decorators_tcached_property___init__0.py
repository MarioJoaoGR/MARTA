
# Module: flutils.decorators
# test_cached_property.py
from flutils.decorators import cached_property
import pytest

class MyClass:
    def __init__(self):
        self.x = 5
        
    @cached_property
    def y(self):
        return self.x + 1

# Test Case 1: Simple Usage of cached_property
def test_simple_usage():
    obj = MyClass()
    assert obj.y == 6, "Expected the first access to compute and cache the value."
    assert obj.y == 6, "Expected subsequent accesses to retrieve the cached value."

# Test Case 2: Using cached_property with a method that performs some computation
class AnotherClass:
    def __init__(self, value):
        self.value = value
        
    @cached_property
    def computed_value(self):
        return self.value * 2

def test_computation():
    instance = AnotherClass(10)
    assert instance.computed_value == 20, "Expected the first access to compute and cache the value."
    assert instance.computed_value == 20, "Expected subsequent accesses to retrieve the cached value."

# Test Case 3: Using cached_property with a class method
class YetAnotherClass:
    def __init__(self, multiplier):
        self.multiplier = multiplier
        
    @cached_property
    def computed_multiplication(self):
        return 10 * self.multiplier

def test_method_with_computation():
    instance = YetAnotherClass(2)
    assert instance.computed_multiplication == 20, "Expected the first access to compute and cache the value."
    assert instance.computed_multiplication == 20, "Expected subsequent accesses to retrieve the cached value."

# Test Case 4: Resetting the property by deleting it
def test_reset_property():
    obj = MyClass()
    y_value = obj.y
    delattr(obj, 'y')