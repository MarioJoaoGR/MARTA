
import pytest
from flutes.multiproc import FuncWrapper

def test_valid_inputs():
    def add(a, b):
        return a + b
    
    wrapper = FuncWrapper(add, (1, 2), {'b': 3})
    assert wrapper is not None
    assert callable(wrapper.fn)
    assert wrapper.args == (1, 2)
    assert wrapper.kwds == {'b': 3}
