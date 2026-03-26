
import pytest
from pytutils.props import setterproperty

# Test initialization with function and optional docstring
def test_setterproperty_initialization():
    def my_func(obj, value):
        pass
    
    sp = setterproperty(my_func)
    assert sp.func == my_func
    assert sp.__doc__ == my_func.__doc__

# Test initialization with function and custom docstring
def test_setterproperty_initialization_with_doc():
    def my_func(obj, value):
        pass
    
    doc = "A custom setter property."
    sp = setterproperty(my_func, doc)
    assert sp.func == my_func