
# Module: pymonet.lazy
import pytest
from pymonet.lazy import Lazy

# Test initialization with a function
def test_init_with_function():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    assert callable(lazy.constructor_fn)
    assert not lazy.is_evaluated
    assert lazy.value is None

# Test initialization with a lambda function
def test_init_with_lambda():
    lazy_lambda = Lazy(lambda x: x * x)
    result = lazy_lambda.fold(5)  # Evaluates the lambda function with argument 5
    assert result == 25
    assert lazy_lambda.is_evaluated
    assert lazy_lambda.value == 25

# Test using map to transform the result
def test_map():
    def add_one(x):
        return x + 1
    
    lazy = Lazy(lambda x: x * x)
    mapped_lazy = lazy.map(add_one)
    result = mapped_lazy.fold()  # Transforms the result of the lambda function using `add_one`
    assert result == 26
    assert mapped_lazy.is_evaluated
    assert mapped_lazy.value == 26

# Test comparing two Lazy instances
def test_eq():
    lazy1 = Lazy(lambda x: x * 2)
    lazy2 = Lazy(lambda x: x * 2)
    assert lazy1 == lazy2
    
    lazy3 = Lazy(lambda x: x * 3)
    assert not (lazy1 == lazy3)

# Test using of to create a Lazy instance with a constant function
def test_of():
    constant_lazy = Lazy.of(42)  # Creates a Lazy instance that always returns 42
    result = constant_lazy.fold()
    assert result == 42
    assert constant_lazy.is_evaluated
    assert constant_lazy.value == 42

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_lazy_Lazy___eq___0
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy___eq___0.py:19:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy___eq___0.py:31:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy___eq___0.py:48:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""