
import pytest
from flutes.iterator import scanr

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test invalid input type for func (not callable)
        result = scanr("not a function", [1, 2, 3, 4])
