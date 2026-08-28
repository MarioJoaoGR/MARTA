
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
        prefix='TEST ',
        overwrite=True,
        thread_info=False,
        custom_repr=((int, lambda x: f'CustomInt({x})')),
        max_variable_length=150,
        normalize=True,
        relative_time=True
    )
    
    with tracer:
        result = sample_function(10, 20)
    
    assert result == 130

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
        normalize=False,
        relative_time=False
    )
    
    with pytest.raises(TypeError):
        with tracer:
            result = sample_function(None, None)

def test_invalid_inputs():
    with pytest.raises(AssertionError):
        Tracer(
            output='invalid_path',
            watch=('x',),
            watch_explode=['my_list'],  # This should be a tuple, not a list
            depth=-1,  # Depth must be >= 1
            prefix=123,  # Prefix must be a string
            overwrite='string',  # Overwrite must be a boolean
            thread_info='not_bool',  # Thread info must be a boolean
            custom_repr=(int,),  # Custom repr must be a tuple of tuples
            max_variable_length='not_int',  # Max variable length must be an int or None
            normalize='not_bool',  # Normalize must be a boolean
            relative_time='not_bool'  # Relative time must be a boolean
        )
