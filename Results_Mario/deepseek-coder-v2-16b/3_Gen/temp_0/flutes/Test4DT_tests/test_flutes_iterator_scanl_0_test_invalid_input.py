
import pytest
from itertools import accumulate
from operator import add
from flutes.iterator import scanl

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test case where func is not callable
        list(scanl(123, [1, 2, 3]))
        
        # Test case where iterable is not an iterable
        list(scanl(add, "not_an_iterable"))
