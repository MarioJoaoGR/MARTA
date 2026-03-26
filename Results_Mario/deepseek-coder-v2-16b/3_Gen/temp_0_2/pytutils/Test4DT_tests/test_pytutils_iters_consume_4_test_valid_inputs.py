
import pytest
from pytutils.iters import consume

def test_valid_inputs():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    
    consume(it)
    with pytest.raises(StopIteration):
        next(it)
