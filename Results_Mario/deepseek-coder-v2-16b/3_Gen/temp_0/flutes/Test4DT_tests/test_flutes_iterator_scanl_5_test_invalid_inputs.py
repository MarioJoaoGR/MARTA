
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test case where func is not a callable
        list(scanl("not_a_function", [1, 2, 3], 0))
    
    with pytest.raises(TypeError):
        # Test case where iterable is not an iterable
        list(scanl(lambda x, y: x + y, "not_an_iterable", 0))
    
    with pytest.raises(TypeError):
        # Test case where initial value is not of the expected type
        list(scanl(lambda x, y: x + y, [1, 2, 3], "not_a_number"))
