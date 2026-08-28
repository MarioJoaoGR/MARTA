
import pytest
from pysnooper.tracer import Tracer

# Test valid inputs scenario
def test_valid_inputs():
    tracer = Tracer(output='/my/log/file.log', watch=('self.x', 'foo.bar'), depth=2, prefix='ZZZ ', thread_info=True)
    assert isinstance(tracer, Tracer), "Tracer instance should be created successfully"

# Test edge cases scenario
def test_edge_cases():
    with pytest.raises(Exception) as exc_info:
        tracer = Tracer(output=None, watch=(), watch_explode=(), depth=1, prefix='', overwrite=True, thread_info=False, custom_repr=(), max_variable_length=100, normalize=True, relative_time=False)
    assert str(exc_info.value) == '`overwrite=True` can only be used when writing content to file.'
