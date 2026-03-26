
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator

def test_scanl_invalid_inputs():
    # Test with None as func
    with pytest.raises(TypeError):
        list(scanl(None, [1, 2, 3], 0))
    
    # Test with None as iterable
    with pytest.raises(TypeError):
        list(scanl(lambda acc, x: acc + x, None, 0))
    
    # Test with None as initial value
    with pytest.raises(TypeError):
        list(scanl(lambda acc, x: acc + x, [1, 2, 3], None))
    
    # Test with non-callable func
    with pytest.raises(TypeError):
        list(scanl("not a callable", [1, 2, 3], 0))
    
    # Test with non-iterable iterable
    with pytest.raises(TypeError):
        list(scanl(lambda acc, x: acc + x, 12345, 0))
