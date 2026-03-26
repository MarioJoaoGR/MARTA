
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator

def test_error_handling():
    # Test case 1: func is not callable
    with pytest.raises(TypeError):
        list(scanl("not a function", [1, 2, 3], 0))
    
    # Test case 2: iterable is not an Iterable
    with pytest.raises(TypeError):
        list(scanl(lambda acc, x: acc + x, "not an iterable", 0))
    
    # Test case 3: initial value is missing
    with pytest.raises(TypeError):
        list(scanl(lambda acc, x: acc + x, [1, 2, 3], None))
