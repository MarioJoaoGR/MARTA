
import pytest
from flutes.multiproc import FuncWrapper

def test_func_wrapper_init():
    def my_function(a, b, c=None):
        return a + b + (c or 0)
    
    func_wrapper = FuncWrapper(my_function, args=(1, 2), kwds={'c': 3})
    
    assert func_wrapper.fn == my_function
    assert func_wrapper.args == (1, 2)
    assert func_wrapper.kwds == {'c': 3}
