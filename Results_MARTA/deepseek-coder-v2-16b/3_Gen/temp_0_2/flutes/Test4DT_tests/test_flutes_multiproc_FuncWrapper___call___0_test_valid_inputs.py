
from flutes.multiproc import FuncWrapper

def test_valid_inputs():
    def add(a, b):
        return a + b
    
    wrapper = FuncWrapper(add, (1,), {'b': 2})
    result = wrapper()
    assert result == 3
