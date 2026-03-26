
# Module: pymonet.lazy
# test_lazy.py
import pytest
from pymonet.lazy import Lazy, Right

def test_lazy_initialization():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    assert not lazy.is_evaluated
    assert lazy.constructor_fn == square

def test_evaluate_function():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    result = lazy.get(5)
    assert lazy.is_evaluated
    assert result == 25

def test_evaluate_function_with_different_args():
    def multiply(x, y):
        return x * y
    
    lazy = Lazy(multiply)
    with pytest.raises(TypeError):
        lazy.get()
    result = lazy.get(3, 4)
    assert lazy.is_evaluated
    assert result == 12

def test_transform_to_either():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    either_value = lazy.to_either(5)
    assert isinstance(either_value, Right)
    assert either_value.value == 25

def test_transform_to_either_with_different_args():
    def multiply(x, y):
        return x * y
    
    lazy = Lazy(multiply)
    with pytest.raises(TypeError):
        lazy.to_either()
    either_value = lazy.to_either(3, 4)
    assert isinstance(either_value, Right)
    assert either_value.value == 12

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_lazy_Lazy_to_either_0
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_either_0.py:5:0: E0611: No name 'Right' in module 'pymonet.lazy' (no-name-in-module)


"""