
# Module: pymonet.lazy
import pytest
from pymonet.lazy import Lazy

# Test initialization with a function
def test_lazy_initialization():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    assert not lazy.is_evaluated
    result = lazy.get(5)  # Now the function is evaluated and stored in 'value'
    assert lazy.is_evaluated
    assert result == 25

# Test using map to transform a function
def test_lazy_map():
    def square(x):
        return x * x
    
    def double(x):
        return x * 2
    
    lazy = Lazy(square)
    transformed_lazy = lazy.map(double)
    result = transformed_lazy.get(5)  # The function is now transformed and evaluated
    assert result == 50

# Test using bind to chain operations
def test_lazy_bind():
    def square(x):
        return x * x
    
    def add_one(x):
        return x + 1
    
    lazy = Lazy(square)
    chained_lazy = lazy.bind(add_one)
    result = chained_lazy.get(5)  # The function is transformed and then the transformation is applied
    assert result == 26

# Test using get method
def test_lazy_get():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    result = lazy.get(5)  # The function is evaluated with the provided argument
    assert result == 25

# Test using to_either method
def test_lazy_to_either():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    either_result = lazy.to_either(5)  # The function is evaluated with the provided argument and encapsulated in a Right monad
    assert either_result.is_right()
    assert either_result.get_or_else("Error") == 25

# Test using fold method
def test_lazy_fold():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    result = lazy.fold()  # The function is evaluated and the result is stored in 'value'
    assert result == 25

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_lazy_Lazy_to_either_0
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_either_0.py:60:11: E1101: Instance of 'Right' has no 'get_or_else' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_either_0.py:68:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""