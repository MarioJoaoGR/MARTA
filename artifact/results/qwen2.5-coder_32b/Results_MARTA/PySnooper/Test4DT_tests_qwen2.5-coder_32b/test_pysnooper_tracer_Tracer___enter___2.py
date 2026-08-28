
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
        custom_repr=((int, lambda x: f'Custom: {x}')),
        max_variable_length=None,
        normalize=False,
        relative_time=True
    )
    
    with tracer:
        result = sample_function(5, 6)
    
    assert result == 41

def test_thread_info():
    tracer = Tracer(
        output='thread_info.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='THREAD: ',
        overwrite=True,
        thread_info=True,
        custom_repr=((int, lambda x: f'Custom: {x}')),
        max_variable_length=None,
        normalize=False,
        relative_time=True
    )
    
    with tracer:
        result = sample_function(5, 6)
    
    assert result == 41

def test_normalize():
    tracer = Tracer(
        output='normalize.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='NORMALIZE: ',
        overwrite=True,
        thread_info=False,
        custom_repr=((int, lambda x: f'Custom: {x}')),
        max_variable_length=None,
        normalize=True,
        relative_time=True
    )
    
    with tracer:
        result = sample_function(5, 6)
    
    assert result == 41

def test_custom_repr():
    tracer = Tracer(
        output='custom_repr.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='CUSTOM_REPR: ',
        overwrite=True,
        thread_info=False,
        custom_repr=((int, lambda x: f'Custom: {x}')),
        max_variable_length=None,
        normalize=False,
        relative_time=True
    )
    
    with tracer:
        result = sample_function(5, 6)
    
    assert result == 41

def test_relative_time():
    tracer = Tracer(
        output='relative_time.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='RELATIVE_TIME: ',
        overwrite=True,
        thread_info=False,
        custom_repr=((int, lambda x: f'Custom: {x}')),
        max_variable_length=None,
        normalize=False,
        relative_time=True
    )
    
    with tracer:
        result = sample_function(5, 6)
    
    assert result == 41
