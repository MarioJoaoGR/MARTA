
import pytest
from pysnooper.tracer import Tracer

# Define a simple sample function to be traced
def sample_function():
    x = 10
    y = 20
    my_list = [1, 2, 3]
    result = x + y * sum(my_list)
    return result

# Test the happy path with valid configuration
def test_happy_path():
    tracer = Tracer(
        output='trace.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='TEST ',
        overwrite=True,
        thread_info=False,  # Set to False to avoid NotImplementedError
        custom_repr=((int, lambda x: f'CustomInt({x})')),
        max_variable_length=None,
        normalize=False,    # Set to False to avoid conflict with thread_info
        relative_time=True
    )
    
    with tracer:
        result = sample_function()
    
    assert result == 130

# Test edge cases with different configurations
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
    
    with tracer:
        result = sample_function()
    
    assert result == 130

# Test invalid inputs and expected exceptions
def test_invalid_inputs():
    with pytest.raises(AssertionError):
        Tracer(
            output='invalid_path',
            watch=('x',),
            watch_explode=('y',),
            depth=-1,  # Invalid depth
            prefix=123,
            overwrite='string',
            thread_info='not_bool',
            custom_repr=(('int', 'not_callable')),
            max_variable_length='not_int',
            normalize='not_bool',
            relative_time='not_bool'
        )

# Test with thread_info enabled and valid configuration
def test_thread_info_enabled():
    tracer = Tracer(
        output='trace.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='TEST ',
        overwrite=True,
        thread_info=True,  # Enable thread info
        custom_repr=((int, lambda x: f'CustomInt({x})')),
        max_variable_length=None,
        normalize=False,    # Set to False to avoid conflict with thread_info
        relative_time=True
    )
    
    with tracer:
        result = sample_function()
    
    assert result == 130

# Test with custom representation function
def test_custom_repr():
    tracer = Tracer(
        output='trace.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='TEST ',
        overwrite=True,
        thread_info=False,
        custom_repr=((int, lambda x: f'CustomInt({x})')),
        max_variable_length=None,
        normalize=False,
        relative_time=True
    )
    
    with tracer:
        result = sample_function()
    
    assert result == 130

# Test with normalized paths disabled
def test_no_normalize():
    tracer = Tracer(
        output='trace.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='TEST ',
        overwrite=True,
        thread_info=False,
        custom_repr=((int, lambda x: f'CustomInt({x})')),
        max_variable_length=None,
        normalize=False,  # Normalization disabled
        relative_time=True
    )
    
    with tracer:
        result = sample_function()
    
    assert result == 130

# Test with relative time enabled
def test_relative_time():
    tracer = Tracer(
        output='trace.log',
        watch=('x', 'y'),
        watch_explode=('my_list',),
        depth=2,
        prefix='TEST ',
        overwrite=True,
        thread_info=False,
        custom_repr=((int, lambda x: f'CustomInt({x})')),
        max_variable_length=None,
        normalize=False,
        relative_time=True  # Relative time enabled
    )
    
    with tracer:
        result = sample_function()
    
    assert result == 130
