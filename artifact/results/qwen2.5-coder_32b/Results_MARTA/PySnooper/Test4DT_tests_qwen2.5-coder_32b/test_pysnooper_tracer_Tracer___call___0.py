
import pytest
from pysnooper.tracer import Tracer

def sample_function(x, y):
    my_list = [1, 2, 3]
    result = x + y * sum(my_list)
    return result

def test_happy_path():
    tracer = Tracer(
        output='trace.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='TEST:',
        overwrite=True,
        thread_info=False,  # Set to False to avoid NotImplementedError
        custom_repr=((int, lambda x: f'CustomInt:{x}')),
        max_variable_length=None,
        normalize=True,
        relative_time=True
    )
    with tracer:
        result = sample_function(10, 5)
    assert result == 40

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
        max_variable_length=100,
        normalize=False,
        relative_time=False
    )
    with pytest.raises(TypeError):
        with tracer:
            result = sample_function(None, None)

def test_with_thread_info():
    tracer = Tracer(
        output='trace.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='TEST:',
        overwrite=True,
        thread_info=True,  # Enabled thread info
        custom_repr=((int, lambda x: f'CustomInt:{x}')),
        max_variable_length=None,
        normalize=False,  # Set to False to avoid NotImplementedError
        relative_time=True
    )
    with tracer:
        result = sample_function(10, 5)
    assert result == 40

def test_custom_repr():
    tracer = Tracer(
        output='trace.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='TEST:',
        overwrite=True,
        thread_info=False,
        custom_repr=((int, lambda x: f'CustomInt:{x}')),
        max_variable_length=None,
        normalize=True,
        relative_time=True
    )
    with tracer:
        result = sample_function(10, 5)
    assert result == 40

def test_relative_time():
    tracer = Tracer(
        output='trace.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='TEST:',
        overwrite=True,
        thread_info=False,
        custom_repr=((int, lambda x: f'CustomInt:{x}')),
        max_variable_length=None,
        normalize=True,
        relative_time=True
    )
    with tracer:
        result = sample_function(10, 5)
    assert result == 40

def test_no_normalize():
    tracer = Tracer(
        output='trace.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='TEST:',
        overwrite=True,
        thread_info=False,
        custom_repr=((int, lambda x: f'CustomInt:{x}')),
        max_variable_length=None,
        normalize=False,
        relative_time=True
    )
    with tracer:
        result = sample_function(10, 5)
    assert result == 40

def test_no_relative_time():
    tracer = Tracer(
        output='trace.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='TEST:',
        overwrite=True,
        thread_info=False,
        custom_repr=((int, lambda x: f'CustomInt:{x}')),
        max_variable_length=None,
        normalize=True,
        relative_time=False
    )
    with tracer:
        result = sample_function(10, 5)
    assert result == 40
