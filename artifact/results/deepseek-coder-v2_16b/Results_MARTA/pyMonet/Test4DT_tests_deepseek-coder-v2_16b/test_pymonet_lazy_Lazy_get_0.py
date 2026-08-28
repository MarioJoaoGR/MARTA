
import pytest
from pymonet.lazy import Lazy

# Test initialization of Lazy class with a function
def test_lazy_initialization():
    def square(x):
        return x * x
    
    lazy_square = Lazy(square)
    assert callable(lazy_square.constructor_fn)

# Test evaluation of the function within Lazy instance
def test_evaluation():
    def expensive_computation(data):
        return sum(data)
    
    lazy_object = Lazy(expensive_computation)
    result = lazy_object.get([1, 2, 3])
    assert result == 6

# Test memoization of the evaluated value
def test_memoization():
    computations = [0]
    
    def expensive_computation(data):
        computations[0] += 1
        return sum(data)
    
    lazy_object = Lazy(expensive_computation)
    result1 = lazy_object.get([1, 2, 3])
    assert result1 == 6
    result2 = lazy_object.get([1, 2, 3])
    assert result2 == 6
    assert computations[0] == 1

# Test transformation of the evaluated value using map method
def test_transformation():
    def expensive_computation(data):
        return sum(data)
    
    lazy_object = Lazy(expensive_computation)
    
    def square(x):
        return x * x
    
    mapped_lazy = lazy_object.map(square)
    result = mapped_lazy.get([1, 2, 3])
    assert result == 36

# Test application of a function to the evaluated value using ap method