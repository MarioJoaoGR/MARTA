
import pytest
from pysnooper.tracer import Tracer

def sample_function(x):
    if x is None:
        return "None provided"
    return x * 2

def test_edge_cases():
    tracer = Tracer(output=None, watch=(), watch_explode=(), depth=1, prefix='', overwrite=False, thread_info=False, custom_repr=((int, lambda x: str(x)),), max_variable_length=None, normalize=False, relative_time=True)
    
    with tracer:
        result_none = sample_function(None)
    
    assert result_none == "None provided"

def test_invalid_inputs():
    with pytest.raises(AssertionError):
        Tracer(output='invalid.log', watch=('x',), depth=0, prefix='', overwrite=False, thread_info=True, custom_repr=((int, 'not a function'),), max_variable_length=-1, normalize=False, relative_time=False)

def test_valid_custom_repr():
    tracer = Tracer(custom_repr=((int, lambda x: f"CustomInt({x})"),))
    
    with tracer:
        result = sample_function(5)
    
    assert result == 10

def test_thread_info_enabled():
    tracer = Tracer(thread_info=True)
    
    with tracer:
        result = sample_function(3)
    
    assert result == 6

def test_max_variable_length():
    tracer = Tracer(max_variable_length=5)
    
    with tracer:
        result = sample_function(1234567890)
    
    assert result == 2469135780

def test_relative_time_enabled():
    tracer = Tracer(relative_time=True)
    
    with tracer:
        result = sample_function(4)
    
    assert result == 8
