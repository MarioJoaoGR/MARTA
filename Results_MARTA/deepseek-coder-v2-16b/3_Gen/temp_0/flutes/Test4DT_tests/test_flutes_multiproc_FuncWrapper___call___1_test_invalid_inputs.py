
import pytest
from flutes.multiproc import FuncWrapper

def test_invalid_inputs():
    with pytest.raises(TypeError):
        wrapper = FuncWrapper(lambda x, y: None, args=(1,), kwds={'a': 2})
        wrapper()
