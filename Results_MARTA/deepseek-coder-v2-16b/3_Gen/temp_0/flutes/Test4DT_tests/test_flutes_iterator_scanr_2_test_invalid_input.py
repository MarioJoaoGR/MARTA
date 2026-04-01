
import pytest
from flutes.iterator import scanr

def test_invalid_input():
    with pytest.raises(TypeError):
        scanr("not a function", [1, 2, 3])
