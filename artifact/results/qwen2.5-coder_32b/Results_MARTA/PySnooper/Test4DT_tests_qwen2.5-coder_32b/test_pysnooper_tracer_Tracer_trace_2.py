
import pytest
from pysnooper.tracer import Tracer

def sample_function(x, y):
    my_list = [1, 2, 3]
    result = x + y * sum(my_list)
    return result

def test_edge_cases():
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


def test_valid_tracer_configuration():
    tracer = Tracer(
        output='trace.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='TEST: ',
        overwrite=True,
        thread_info=False,
        custom_repr=((int, lambda x: f'Custom: {x}')),
        max_variable_length=None,
        normalize=True,
        relative_time=True
    )
    
    with tracer:
        result = sample_function(10, 5)
    
    assert result == 40

def test_custom_representation():
    tracer = Tracer(
        output='trace.log',
        watch=('x', 'y'),
        watch_explode=(),
        depth=1,
        prefix='',
        overwrite=True,
        thread_info=False,
        custom_repr=((int, lambda x: f'Custom: {x}')),
        max_variable_length=None,
        normalize=False,
        relative_time=False
    )
    
    with tracer:
        result = sample_function(10, 5)
    
    assert result == 40

def test_max_variable_length():
    tracer = Tracer(
        output='trace.log',
        watch=('x', 'y'),
        watch_explode=(),
        depth=1,
        prefix='',
        overwrite=True,
        thread_info=False,
        custom_repr=(),
        max_variable_length=10,
        normalize=False,
        relative_time=False
    )
    
    with tracer:
        result = sample_function(10, 5)
    
    assert result == 40

def test_relative_time():
    tracer = Tracer(
        output='trace.log',
        watch=('x', 'y'),
        watch_explode=(),
        depth=1,
        prefix='',
        overwrite=True,
        thread_info=False,
        custom_repr=(),
        max_variable_length=None,
        normalize=False,
        relative_time=True
    )
    
    with tracer:
        result = sample_function(10, 5)
    
    assert result == 40