
import pytest
from flutes.iterator import scanr, scanl
import operator

def test_invalid_input():
    with pytest.raises(TypeError):
        scanr("not a function", [1, 2, 3])
