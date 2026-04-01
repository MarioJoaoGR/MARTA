
import pytest
from flutes.multiproc import FuncWrapper

def test_invalid_inputs():
    with pytest.raises(TypeError):
        wrapper = FuncWrapper(lambda x, y: x + y, args=(1,), kwds={'b': 2})
        result = wrapper()
