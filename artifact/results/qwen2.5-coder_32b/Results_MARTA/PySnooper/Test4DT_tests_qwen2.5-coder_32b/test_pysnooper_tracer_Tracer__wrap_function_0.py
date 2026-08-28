
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
        prefix='DEBUG: ',
        overwrite=True,
        thread_info=True,
        custom_repr=((int, lambda x: f'Custom: {x}')),
        max_variable_length=None,
        normalize=False,
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
        max_variable_length=100,
        normalize=True,
        relative_time=False
    )
    
    with pytest.raises(TypeError):
        with tracer:
            sample_function(None, None)

def test_invalid_inputs():
    with pytest.raises(AssertionError):
        Tracer(
            output='invalid_path',
            watch=['x'],
            watch_explode=['my_list'],
            depth=-1,
            prefix=123,
            overwrite='string',
            thread_info='not_bool',
            custom_repr=(int, 'not_callable'),
            max_variable_length='not_int',
            normalize='not_bool',
            relative_time='not_bool'
        )
