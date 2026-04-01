
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test case where func is not a callable
        list(scanl(42, [1, 2, 3], 0))  # Should raise TypeError

    with pytest.raises(TypeError):
        # Test case where iterable is not an iterable
        list(scanl(lambda acc, x: acc + x, 42, 0))  # Should raise TypeError

    with pytest.raises(TypeError):
        # Test case where initial value is not provided for a callable that takes two arguments
        list(scanl(lambda acc, x: acc + x, [1, 2, 3], None))  # Should raise TypeError
