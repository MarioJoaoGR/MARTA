
# Module: pymonet.lazy
import pytest
from pymonet.lazy import Lazy
try:
    from some_module import Box  # Assuming a module where Box might be defined
except ImportError:
    class Box:  # Placeholder for the actual Box class definition if it doesn't exist in some_module
        def __init__(self, value):
            self.value = value

try:
    from some_module import Either  # Assuming a module where Either might be defined
except ImportError:
    class Either:  # Placeholder for the actual Either class definition if it doesn't exist in some_module
        def __init__(self, value):
            self.value = value

# Test creating a Lazy object with a function
def test_lazy_creation():
    def square(x):
        return x * x
    
    lazy_square = Lazy(square)
    assert callable(lazy_square.constructor_fn)
    assert not lazy_square.is_evaluated

# Test forcing evaluation of a Lazy object
def test_compute_value():
    def square(x):
        return x * x
    
    lazy_square = Lazy(square)
    result = lazy_square._compute_value(5)
    assert result == 25
    assert lazy_square.is_evaluated
    assert lazy_square.value == 25

# Test mapping a function over the stored function
def test_map():
    def square(x):
        return x * x
    
    lazy_square = Lazy(square)
    
    def double(x):
        return 2 * x
    
    mapped_lazy = lazy_square.map(double)
    result = mapped_lazy._compute_value(5)