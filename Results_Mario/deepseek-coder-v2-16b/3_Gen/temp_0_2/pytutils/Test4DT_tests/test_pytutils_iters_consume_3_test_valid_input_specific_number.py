
import pytest
from pytutils.iters import consume

def test_valid_input_specific_number():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    
    # Test consuming all elements
    consume(it)
    with pytest.raises(StopIteration):
        next(it)
