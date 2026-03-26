
# Test case  
# Module: flutes.multiproc
import pytest
from flutes.multiproc import FuncWrapper

# Example function to use in tests
def example_function(a, b=None):
    return a + (b or 0)

@pytest.fixture
def func_wrapper():
    return FuncWrapper(example_function, args=(1,), kwds={'b': 2})

# Test cases for __init__ method
def test_func_wrapper_init():
    wrapper = FuncWrapper(example_function, args=(1,), kwds={'b': 2})
    assert wrapper.fn == example_function
    assert wrapper.args == (1,)
    assert wrapper.kwds == {'b': 2}

# Test cases for __call__ method
def test_func_wrapper_call(func_wrapper):
    result = func_wrapper()
    assert result == 3  # example_function(1, b=2) should return 3

def test_func_wrapper_call_with_additional_args(func_wrapper):
    with pytest.raises(TypeError):
        result = func_wrapper(3)  # This should raise a TypeError because of the extra positional argument

def test_func_wrapper_call_with_different_arguments(func_wrapper):
    with pytest.raises(TypeError):
        result = func_wrapper(3, b=4)  # This should raise a TypeError because of the keyword argument 'b'
