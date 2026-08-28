
import inspect
import collections
from pysnooper.tracer import get_local_reprs

def example_function():
    x = 10
    y = [1, 2, 3]
    frame = inspect.currentframe()
    return get_local_reprs(frame)



def test_no_custom_repr():
    frame = inspect.currentframe()
    result = get_local_reprs(frame)
    expected = collections.OrderedDict([('frame', "<frame at ...>")])  # Frame object representation will vary
    assert list(result.items())[0][0] == 'frame'  # We can only check the key name here


