
import pytest
from itertools import islice, count
import collections
from pytutils.iters import consume

def test_consume_all():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    
    # Consume all elements when n is None
    consume(it)
    with pytest.raises(StopIteration):
        next(it)
