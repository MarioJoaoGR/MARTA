
import pytest
from pytutils.iters import consume

def test_valid_input_specific_steps():
    lst = [1, 2, 3, 4]
    it = iter(lst)
    
    # Consume the entire iterator
    consume(it)
    
    with pytest.raises(StopIteration):
        next(it)
