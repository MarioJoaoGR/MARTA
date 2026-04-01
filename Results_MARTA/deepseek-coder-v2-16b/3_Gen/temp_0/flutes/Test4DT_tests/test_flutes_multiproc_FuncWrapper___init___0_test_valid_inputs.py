
import pytest
from flutes.multiproc import FuncWrapper

def example_function(a, b=None):
    return a + (b or 0)

@pytest.fixture
def wrapper():
    return FuncWrapper(example_function, args=(1,), kwds={'b': 2})

def test_valid_inputs(wrapper):
    result = wrapper.fn(*wrapper.args, **wrapper.kwds)
    assert result == 3
