
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator

def test_edge_cases():
    # Test with None input
    with pytest.raises(TypeError):
        list(scanl(lambda acc, x: acc + x, None, 0))
    
    # Test with empty iterable
    assert list(scanl(lambda acc, x: acc + x, [], 0)) == [0]
    
    # Test with boundary value initial
    assert list(scanl(lambda acc, x: acc + x, [1, 2, 3, 4], float('-inf'))) == [float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf')]
    
    # Test with None function
    with pytest.raises(TypeError):
        list(scanl(None, [1, 2, 3, 4], 0))
