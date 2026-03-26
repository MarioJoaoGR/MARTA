
import pytest
from typing import Callable, Iterable, List

# Assuming the module 'flutes.iterator' has been imported correctly
from flutes.iterator import scanr

def test_invalid_input_none():
    # Arrange
    func = lambda x, y: x + y  # Example function to use in scanr
    
    # Act and Assert
    with pytest.raises(TypeError):
        result = scanr(func, None)
