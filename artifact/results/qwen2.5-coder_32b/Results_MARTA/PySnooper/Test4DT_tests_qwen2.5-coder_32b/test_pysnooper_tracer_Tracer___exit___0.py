
import pytest
from pysnooper.tracer import Tracer

def sample_function(x):
    y = x * 2
    return y + 3

def test_happy_path():
    tracer = Tracer(output='happy_path.log', watch=('x',), depth=1, prefix='HAPPY: ', overwrite=True)
    with tracer:
        result = sample_function(5)
    assert result == 13

def test_edge_cases():
    tracer = Tracer(output=None, watch=(), watch_explode=(), depth=1, prefix='', overwrite=False)
    with tracer:
        result = sample_function(0)
    assert result == 3

def test_invalid_inputs():
    with pytest.raises(AssertionError):
        tracer = Tracer(output='invalid.log', watch=('x',), watch_explode=(), depth=-1, prefix='', overwrite=False)
        with tracer:
            result = sample_function(5)
