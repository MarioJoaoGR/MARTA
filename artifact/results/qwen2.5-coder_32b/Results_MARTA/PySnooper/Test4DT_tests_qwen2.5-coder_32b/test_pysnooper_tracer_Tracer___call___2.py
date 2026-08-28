
import pytest
from pysnooper.tracer import Tracer

def sample_function(x, y):
    my_list = [1, 2, 3]
    result = x + y * sum(my_list)
    return result

def test_happy_path():
    tracer = Tracer(
        output='happy_path.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='HAPPY: ',
        overwrite=True,
        thread_info=False,
        custom_repr=((int, lambda x: f'CustomInt({x})')),
        max_variable_length=None,
        normalize=False,
        relative_time=True
    )
    
    with tracer:
        result = sample_function(10, 5)
    
    assert result == 40

def test_sample_function_with_different_values():
    tracer = Tracer(
        output='different_values.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='DIFFERENT: ',
        overwrite=True,
        thread_info=False,
        custom_repr=((int, lambda x: f'CustomInt({x})')),
        max_variable_length=None,
        normalize=False,
        relative_time=True
    )
    
    with tracer:
        result = sample_function(5, 2)
    
    assert result == 17

