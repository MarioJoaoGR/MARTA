
import pytest
from pysnooper.tracer import Tracer

def sample_function(x, y):
    my_list = [1, 2, 3]
    result = x + y * sum(my_list)
    return result


def test_tracer_with_watch_and_watch_explode():
    tracer = Tracer(
        output=None,
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='',
        overwrite=False,
        thread_info=False,
        custom_repr=((int, lambda x: f'Custom: {x}')),
        max_variable_length=None,
        normalize=True,
        relative_time=False
    )
    
    with tracer:
        result = sample_function(1, 2)
    
    assert result == 13

def test_tracer_with_custom_repr():
    tracer = Tracer(
        output=None,
        watch=(),
        watch_explode=(),
        depth=1,
        prefix='',
        overwrite=False,
        thread_info=False,
        custom_repr=((int, lambda x: f'Custom: {x}')),
        max_variable_length=None,
        normalize=True,
        relative_time=False
    )
    
    with tracer:
        result = sample_function(1, 2)
    
    assert result == 13

def test_tracer_no_truncation():
    tracer = Tracer(
        output=None,
        watch=(),
        watch_explode=(),
        depth=1,
        prefix='',
        overwrite=False,
        thread_info=False,
        custom_repr=(),
        max_variable_length=None,
        normalize=True,
        relative_time=False
    )
    
    with tracer:
        result = sample_function(1, 2)
    
    assert result == 13

def test_tracer_relative_time():
    tracer = Tracer(
        output=None,
        watch=(),
        watch_explode=(),
        depth=1,
        prefix='',
        overwrite=False,
        thread_info=False,
        custom_repr=(),
        max_variable_length=100,
        normalize=True,
        relative_time=True
    )
    
    with tracer:
        result = sample_function(1, 2)
    
    assert result == 13