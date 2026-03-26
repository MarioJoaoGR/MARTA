
import pytest
from pytutils.iters import consume

def test_consume():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    
    # Consume all elements by default
    consume(it)
    with pytest.raises(StopIteration):
        next(it)  # The iterator should be advanced beyond the original list.
