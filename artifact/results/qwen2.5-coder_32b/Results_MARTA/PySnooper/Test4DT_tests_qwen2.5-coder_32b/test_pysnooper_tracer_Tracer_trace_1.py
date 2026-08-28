
import pytest
from pysnooper.tracer import Tracer

def sample_function(x, y):
    my_list = [1, 2, 3]
    result = x + y * sum(my_list)
    return result





def test_normalize_with_thread_info():
    tracer = Tracer(
        output=None,
        watch=('x', 'y'),
        watch_explode=(),
        depth=1,
        prefix='',
        overwrite=False,
        thread_info=True,
        custom_repr=(),
        max_variable_length=100,
        normalize=True,
        relative_time=False
    )
    with pytest.raises(NotImplementedError) as e:
        with tracer:
            result = sample_function(4, 6)
    assert str(e.value) == "normalize is not supported with thread_info"


