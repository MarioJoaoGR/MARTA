
import pytest
from py_backwards.transformers import yield_from



def test_invalid_exception_type():
    def simple_generator():
        yield 1
        yield 2
        yield 3
    
    with pytest.raises(TypeError):
        gen = yield_from(simple_generator(), ValueError, [4, 5])