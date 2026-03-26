
import pytest
from flutes.multiproc import FuncWrapper

# Test initialization with function and positional arguments
def test_func_wrapper_initialization():
    def example_function(a, b=2):
        return a + b

    func_wrapper = FuncWrapper(example_function, (1,), {'b': 3})
    result = func_wrapper()
    assert result == 4, "Expected the function to be called with arguments and return the correct result"

# Test initialization without optional parameter
def test_func_wrapper_initialization_without_optional():
    def example_function(a, b=2):
        return a + b

    func_wrapper = FuncWrapper(example_function, (1,), {'b': 3})
    result = func_wrapper()